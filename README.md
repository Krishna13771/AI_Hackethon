🚀 AWS Career Guide – GenAI Powered Career Copilot

A full-stack Generative AI career assistant built on AWS, designed for students and professionals to prepare for jobs using secure authentication, AI-driven interview coaching, resume verification, and resume creation.

This project uses Amazon Bedrock, Amazon Rekognition, Amazon Textract, and AWS S3 to deliver an end-to-end personalized career preparation platform.

🌟 Key Features
1. 🔐 Secure Face-Based Login

Technology: Amazon Rekognition

Functionality: Matches a live selfie with a stored reference image.

Security: Ensures login is restricted to the registered user only.

Prevents impersonation and enhances identity security.

2. 🤖 AI Interview Coach

Powered by Amazon Bedrock (Claude / Titan)
Supports multiple modes:

Technical Interview → Role-specific coding & cloud questions

DSA Mode → Questions on Data Structures & Algorithms

HR Mode → Behavioral, teamwork, and communication questions

Mock Interview Mode

User types answers

AI gives instant feedback on:
✓ Correctness
✓ Clarity
✓ Completeness
✓ Improvement suggestions

3. 📄 Document Verification

Technology: Amazon Textract + Bedrock reasoning

Features:

OCR extraction from resumes, marksheets, degrees

Intelligent name-matching using chain-of-thought reasoning

Validates document consistency

Generates a Credibility Score for the user

Ensures authenticity of academic documents.

4. 📑 AI Resume Builder

Technology: Amazon Bedrock

Converts user details into a professional, ATS-friendly resume

Supports multiple formats and job roles

🛠️ Tech Stack
Frontend

Next.js 15

React 19

Tailwind CSS

Framer Motion

Backend

Next.js API Routes (Serverless Architecture)

AWS Services

Rekognition → Face login

Bedrock → Interview, feedback, resume generation

Textract → Document extraction

S3 → Secure storage (images / documents)

Libraries

@aws-sdk/client-*

lucide-react

framer-motion

⚙️ Setup Instructions
Prerequisites

Node.js 18+

AWS Account with enabled access to:

Bedrock

Rekognition

Textract

S3

AWS CLI configured (optional)

1. Clone the Repository
git clone <your-repo-url>
cd carreerguide

2. Install Dependencies
npm install

3. AWS Configuration
Create an IAM User

Give access to the following:

AmazonRekognitionFullAccess

AmazonBedrockFullAccess

AmazonTextractFullAccess

AmazonS3FullAccess

Then generate:

Access Key ID

Secret Access Key

4. Setup Environment Variables

Create .env.local file:

cp .env.example .env.local


Update with your actual values:

# AWS Credentials
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=us-west-2

# S3 Bucket
AWS_S3_BUCKET_NAME=your-bucket
AWS_S3_REGION=us-east-1

# App Config
NEXT_PUBLIC_APP_URL=http://localhost:3000


⚠️ Make sure the S3 bucket exists in the defined region.

5. Run the App
npm run dev


Open the app in browser:

👉 http://localhost:3000

📂 Folder Structure
├── app/
│   ├── api/            # Authentication, Interview, Verification APIs
│   ├── dashboard/      # User Dashboard UI
│   ├── interview/      # Interview Coach Pages
│   ├── login/          # Login / Registration
│   └── verification/   # Document Verification UI
├── components/         # CameraCapture, AWS Icons, UI components
├── lib/                # AWS clients & utilities
├── public/             # Static assets
└── aws/                # AWS policy references, setup guides

🔒 Security Notes

All biometric data (face images) are stored in your private S3 bucket.

No face data is shared externally.

Follow local laws regarding biometric authentication.