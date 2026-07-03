from app.models.chat import ChatMessages
from app.models.resume import Resume
from app.models.job_description import JobDescription


def build_candidate_evaluation_messages(
    self,
    resume: Resume,
    job: JobDescription,
) -> ChatMessages:

    return [
        {
            "role": "system",
            "content": """
You are an experienced technical recruiter.

Evaluate how well the candidate matches the given job description.

Use only the provided information.

Do not assume missing experience or skills.

Evaluate:

1. Technical Skills
2. Experience
3. Education
4. Overall Fit

Recommendation must be exactly one of:

- Highly Recommended
- Recommended
- Consider
- Not Recommended

Return ONLY valid JSON.

Do not include markdown.

JSON Structure:

{
    "technical_match_score": 0,
    "experience_match_score": 0,
    "education_match_score": 0,
    "responsibility_match_score": 0,
    "soft_skill_match_score": 0,

    "confidence_score": 0,

    "required_matching_skills": [],

    "required_missing_skills": [],

    "preferred_matching_skills": [],

    "preferred_missing_skills": [],

    "additional_skills": [],

    "matched_skill_evidence": [
        {
            "skill": "",
            "evidence": ""
        }
    ],

    "strengths": [],

    "weaknesses": [],

    "hiring_risks": [],

    "interview_focus_areas": [],

    "reasoning": ""
}
"""
        },
        {
            "role": "user",
            "content": f"""
Resume:

{resume.model_dump_json(indent=2)}

Job Description:

{job.model_dump_json(indent=2)}
"""
        }
    ]