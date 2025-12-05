🚀 Features
1. AI-Powered Resume Builder

Technology: Amazon Bedrock (Claude/Titan)

Functionality:

Generates a professional, clean, ATS-friendly resume from user input.

Converts bullet points, skills, and project descriptions into HR-grade phrasing.

Structures resume sections automatically:
✓ Summary
✓ Skills
✓ Education
✓ Projects
✓ Certifications

Benefits:

Saves time

Ensures ATS compliance

Removes formatting burden

2. Corporate-Grade UI

Technology: Streamlit + Custom CSS

UI Features:

Clean corporate gradient background

White glass-style cards

Modern blue-accent buttons

Professional input structure

Download link interface

User Experience:

Simple, elegant, and business-ready.

3. Resume PDF Generation

Technology: Python (ReportLab/FPDF)

Functionality:

Converts AI-generated text into a well-formatted PDF

Ensures ATS readability (no tables/images)

Clear spacing, font consistency, hierarchy

Module: pdfgen.py

Handles line-by-line PDF construction.

4. Serverless Backend Architecture

Technology: AWS Lambda + API Gateway

Functionality:

Accepts user data from frontend

Calls Bedrock for resume generation

Generates PDF

Uploads resume to S3

Returns downloadable URL to the frontend

Benefits:

Fully serverless

Scalable

Cost-efficient

5. Secure Resume Storage

Technology: Amazon S3

Functionality:

Stores generated PDF securely

Provides temporary or public URL to download

Ensures privacy of user data

🛠️ Tech Stack
Frontend

Streamlit

HTML/CSS (Custom Theme)

Form-based UI

Backend

AWS Lambda (Python)

API Gateway

Amazon Bedrock (Generative AI)

Amazon S3 (PDF storage)

Libraries

requests

boto3

FPDF or ReportLab

Python 3.10+

🧩 Project Architecture
User → Streamlit UI → API Gateway → Lambda → Bedrock (AI)
                                            ↓
                                         pdfgen.py
                                            ↓
                                           S3
                                            ↓
                           Streamlit shows downloadable PDF link

⚙️ Setup Instructions
1. Clone Repository
git clone <repo-url>
cd career-copilot-resume

2. Create Virtual Environment (Optional but Recommended)
python -m venv .venv
source .venv/bin/activate    # macOS/Linux
.venv\Scripts\activate       # Windows

3. Install Frontend Dependencies
cd frontend
pip install -r requirements.txt

4. Set Up Backend for AWS Lambda
Navigate to backend folder:
cd backend
pip install -r requirements.txt -t .
zip -r resume_lambda.zip .


Upload resume_lambda.zip to AWS Lambda.

5. Configure Environment Variables (AWS Credentials)

You need IAM permissions for:

AmazonBedrockFullAccess

AmazonS3FullAccess

AWSLambdaBasicExecutionRole

Inside Lambda → Configuration → Environment Variables:

AWS_REGION=ap-south-1
S3_BUCKET=your-resume-bucket

6. Run the Frontend
cd frontend
streamlit run streamlit_app.py


Streamlit output:

Local URL: http://localhost:8503
Network URL: http://10.x.x.x:8503

📂 Project Structure
career-copilot-resume/
│
├── backend/
│   ├── lambda_function.py        # Main Lambda Handler
│   ├── bedrock_client.py         # AI integration logic
│   ├── pdfgen.py                 # PDF generator
│   ├── utils.py                  # Helper methods
│   ├── requirements.txt
│   └── resume_lambda.zip         # Lambda deployment package
│
├── frontend/
│   └── streamlit_app.py          # Streamlit corporate UI
│
├── deploy/
│   └── template.yaml             # AWS SAM deployment template
│
└── README.md

🔒 Security Note

This project handles user resume data.
To protect privacy:

Use private S3 buckets

Enable least-privilege IAM roles

Do NOT log sensitive user info

URLs can be presigned URLs for temporary access

🌟 Future Enhancements

Multiple resume design templates

Job description → auto-optimized resume

ATS score calculator

Real-time grammar checking

Cover letter generator

Built-in LinkedIn profile importer

User account system
