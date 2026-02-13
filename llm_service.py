import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_resume(resume_text, job_description):
    try:
        prompt = f"""
        You are an expert ATS system and career coach.

        Analyze the resume against the job description.

        Return:
        1. Resume Score (0-100)
        2. Missing Keywords
        3. Skill Gaps
        4. Suggested Improvements
        5. 5 Interview Questions

        Resume:
        {resume_text}

        Job Description:
        {job_description}
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error calling Gemini API: {str(e)}"
