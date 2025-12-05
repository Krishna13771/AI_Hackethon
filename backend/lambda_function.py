import os
import json
import uuid
import boto3
from pdfgen import text_to_pdf
from bedrock_client import call_bedrock_model

# FIXED REGION HANDLING FOR LAMBDA
AWS_REGION = boto3.session.Session().region_name or "us-east-1"

# Load env variables
S3_BUCKET = os.getenv("S3_BUCKET", "ai-hackethon-01")

s3 = boto3.client("s3", region_name=AWS_REGION)

def build_prompt(payload: dict) -> str:
    return f"""
You are an expert professional resume writer.

Create a clean, ATS-friendly resume using ALL the user details below.

The resume MUST start with:

Full Name: {payload.get('name')}
Email: {payload.get('email')}
Phone: {payload.get('phone')}

After that, include these clearly labeled sections:

1. Professional Summary  
2. Skills  
3. Education  
4. Projects  
5. Certifications  
6. Achievements  

User details in JSON form:
{json.dumps(payload, indent=2)}

RULES:
- The student's full name should ALWAYS appear as the first line.
- Contact information MUST appear directly beneath the name.
- Use ATS-friendly, simple formatting.
- Do NOT skip any section even if empty.
- Keep sentences short, clean, and professional.
"""

def generate_resume(payload):
    prompt = build_prompt(payload)
    resume_text = call_bedrock_model(prompt)

    # Save to temp file
    pdf_path = f"/tmp/{uuid.uuid4().hex}.pdf"
    text_to_pdf(resume_text, pdf_path)

    # Upload to S3
    s3_key = f"resumes/{uuid.uuid4().hex}.pdf"
    s3.upload_file(pdf_path, S3_BUCKET, s3_key)

    # Generate presigned URL
    url = s3.generate_presigned_url(
        "get_object",
        Params={"Bucket": S3_BUCKET, "Key": s3_key},
        ExpiresIn=3600
    )

    return {"resume_url": url}

# ---------------------------- LAMBDA HANDLER ---------------------------- #

def lambda_handler(event, context):
    try:
        body = event.get("body")
        if isinstance(body, str):
            payload = json.loads(body)
        else:
            payload = body

        result = generate_resume(payload)

        return {
            "statusCode": 200,
            "body": json.dumps(result),
            "headers": {"Content-Type": "application/json"}
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
            "headers": {"Content-Type": "application/json"}
        }
