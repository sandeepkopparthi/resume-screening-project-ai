def build_jd_parser_prompt(job_description: str) -> list[dict]:
    return [
        {
            "role": "system",
            "content": """
You are an expert HR recruiter.

Extract structured information from the following job description.

Return ONLY valid JSON.

Do not include markdown.

Do not include explanations.

If a scalar field is unavailable, return null.

If a list field is unavailable, return [].

JSON Structure:

{
    "job_title": "",
    "company_name": "",
    "location": "",
    "employment_type": "",
    "experience_required": "",
    "education_required": "",
    "required_technical_skills": [],
    "preferred_skills": [],
    "responsibilities": [],
    "required_certifications": [],
    "tools_and_frameworks": [],
    "soft_skills": [],
    "domain": "",
    "summary": ""
}
"""
        },
        {
            "role": "user",
            "content": job_description
        }
]