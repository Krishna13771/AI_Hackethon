import os
import json
import boto3

# 🚀 IMPORTANT FIX:
# Lambda already provides AWS_REGION internally.
# We read it directly from boto3 session instead of env variables.
AWS_REGION = boto3.session.Session().region_name or "us-east-1"

BEDROCK_MODEL_ID = "amazon.titan-text-express-v1"   # ✔ TITAN MODEL

# Initialize Bedrock Runtime client
bedrock = boto3.client("bedrock-runtime", region_name=AWS_REGION)

def call_bedrock_model(prompt: str, max_tokens: int = 500) -> str:
    body = {
        "inputText": prompt,
        "textGenerationConfig": {
            "maxTokenCount": max_tokens,
            "temperature": 0.7,
            "topP": 0.9
        }
    }

    try:
        response = bedrock.invoke_model(
            modelId=BEDROCK_MODEL_ID,
            contentType="application/json",
            accept="application/json",
            body=json.dumps(body)
        )

        output = response["body"].read().decode("utf-8")
        parsed = json.loads(output)

        # Titan returns generated text here:
        return parsed["results"][0]["outputText"]

    except Exception as e:
        return f"Error calling Titan: {str(e)}"
