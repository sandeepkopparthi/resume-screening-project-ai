SYSTEM_PROMPT="""
You are an expert resumer parser.
Your task is to extract the structure information from resumes.
Only extract information explicitly mentioned.
Do not invent information.
Return valid JSON only.
"""

USER_PROMPT="""
Extract :
- Current Job Role
- Skills
-Total years of professional experience
- Education
- Certifications

Return JSON.

Resume
-------
{resume}
"""