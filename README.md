🚀 AI Resume Generator – Career Copilot

This project is a Generative AI–powered Resume Builder that automatically creates ATS-friendly PDF resumes based on user inputs.
It uses a Streamlit frontend, a serverless AWS backend, and AI content generation via Amazon Bedrock.

Users simply enter their details → The system generates → A downloadable PDF resume is instantly created and stored in S3.

⭐ Features (Exactly Your Project)
1️⃣ Streamlit Frontend (Corporate UI)

Clean, professional design

Gradient corporate background

Card-based form layout

User inputs:

Name

Email

Phone

Summary

Skills

Education

Projects

Certifications

2️⃣ AI Resume Generation (Amazon Bedrock)

Takes user inputs

Enhances content using AI

Produces professional, HR-friendly resume sections

Ensures ATS-optimized writing (clear structure, bullet points, no images)

3️⃣ PDF Generation (pdfgen.py)

Converts AI-generated text → Beautiful PDF

Uses simple, ATS-safe formatting

Handles:

Line spacing

Font formatting

Section separators

4️⃣ AWS Lambda Backend

Your Lambda performs the pipeline:

Receive user input

Call Bedrock for AI content

Generate PDF using pdfgen.py

Upload final PDF to S3

Return a resume download URL to Streamlit

5️⃣ Amazon S3 Storage

Stores generated PDF safely

Provides public or presigned URL for download

Files named dynamically using username

🏗️ Architecture Overview
Streamlit UI (User Form)
        ↓
API Gateway
        ↓
AWS Lambda (lambda_function.py)
        ↓
Bedrock (AI Text Generation)
        ↓
pdfgen.py (PDF Creator)
        ↓
Amazon S3 (Stores Resume)
        ↓
Streamlit (Download Resume Link)

📂 Project Structure
career-copilot-resume/
│
├── backend/
│   ├── lambda_function.py        # Main Lambda logic
│   ├── bedrock_client.py         # Bedrock API call logic
│   ├── pdfgen.py                 # Converts AI output into PDF
│   ├── utils.py                  # Helper functions
│   ├── requirements.txt          # Python libs for Lambda
│   └── resume_lambda.zip         # Deployment package
│
├── frontend/
│   └── streamlit_app.py          # UI and API request handler
│
├── deploy/
│   └── template.yaml             # (Optional) SAM deployment file
│
└── README.md

⚙️ Setup Instructions
🛠️ 1. Clone the Repository
git clone <your-repo-url>
cd career-copilot-resume

🛠️ 2. Backend (AWS Lambda Setup)
Install dependencies inside backend folder:
cd backend
pip install -r requirements.txt -t .
zip -r resume_lambda.zip .


Upload this ZIP to AWS Lambda.

Lambda Environment Variables:
AWS_REGION=ap-south-1
S3_BUCKET=<your-s3-bucket>

Required IAM Permissions:

AmazonBedrockFullAccess

AmazonS3FullAccess

AWSLambdaBasicExecutionRole

🖥️ 3. Frontend (Streamlit UI Setup)
Install dependencies:
cd frontend
pip install -r requirements.txt

Run app:
streamlit run streamlit_app.py

📡 API Request / Response Example
Request sent by Streamlit:
{
  "name": "Krishna",
  "email": "krishna@example.com",
  "phone": "9876543210",
  "summary": "Enthusiastic cloud developer...",
  "skills": "Python, AWS, Streamlit",
  "education": "B.Tech CSE",
  "projects": "Resume Builder - AI-powered - Python/CSS",
  "certifications": "AWS Cloud Practitioner"
}

Lambda Response:
{
  "resume_url": "https://your-bucket.s3.amazonaws.com/krishna_resume.pdf"
}

🔮 Future Enhancements

You can mention these in viva/hackathon:

Multiple resume templates

Resume ATS Scoring

Cover Letter Generator

Job Description Matching

LinkedIn Data Import

Dark/Light Theme

Multi-language resume support

📝 Conclusion

Your project is a complete, production-style GenAI Resume Builder featuring:

✔ AI content generation
✔ Serverless backend
✔ Clean corporate frontend
✔ Automated PDF generation
✔ Secure cloud storage

This is a strong, real-world portfolio project demonstrating skills in:

AWS

Generative AI

Python

Streamlit

PDF Automation

Serverless Architecture
