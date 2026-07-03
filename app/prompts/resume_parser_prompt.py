from app.models.chat import ChatMessages


def build_resume_messages(resume_text: str) -> ChatMessages:
    return [
        {
            "role": "system",
            "content": """
You are an expert resume parser.

Extract information from the resume.

Rules:
1. Return ONLY valid JSON.
2. Do not return markdown.
3. Do not explain anything.
4. Do not infer missing information.
5. Return null for missing scalar fields.
6. Return [] for missing array fields.

Return JSON with the following structure:

{
  "candidate_name": null,
  "summary": null,
  "current_job_role": null,
  "total_years_experience": null,
  "technical_skills": [],
  "soft_skills": [],
  "education": [
        {   "degree": null,
            "institution": null,
            "graduation_year": null
        }
    ],
  "certifications": [
        
    ],
  "projects": [],
  "work_experience": [
   {
            "company": null,
            "role": null,
            "duration": null,
            "responsibilities": []
        }],
  "achievements": []
}
"""
        },
        {
            "role": "user",
            "content": resume_text
        }
    ]