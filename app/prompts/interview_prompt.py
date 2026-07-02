from app.models.resume import Resume
from app.models.job_description import JobDescription
from app.models.candidate_assessment import CandidateAssessment


class InterviewPromptBuilder:

    @staticmethod
    def build(
        resume: Resume,
        job: JobDescription,
        assessment: CandidateAssessment,
    ) -> str:
        
        role = """
        You are a Senior Technical Interview Panel with expertise in software engineering hiring.

        Your task is to prepare a structured interview plan for a hiring manager.
        """
        objective = """
        Generate role-specific interview questions using:

        - Resume
        - Job Description
        - Candidate Assessment

        The interview plan must help validate whether the candidate possesses
        the technical and behavioral competencies required for the role.
        """

        technical_rules = """
        Generate technical questions that:

        - Focus primarily on required technical skills.
        - Cover technologies mentioned in the Job Description.
        - Validate claims made in the resume.
        - Investigate missing or weak skills identified in the assessment.
        - Include framework-specific questions.
        - Include debugging questions.
        - Include architecture and design questions.
        - Include real-world implementation scenarios.
        - Avoid theoretical trivia.
        - Prefer practical engineering discussions.
        """

        behavioral_rules = """
        Generate behavioral questions that evaluate:

        - Ownership
        - Collaboration
        - Communication
        - Conflict resolution
        - Decision making
        - Learning ability
        - Leadership (if applicable)
        """

        distribution = """
        Generate approximately:

        Technical Core: 4

        Technical Missing Skills: 3

        Technical Experience: 3

        Technical Architecture: 2

        Technical Scenario: 2

        Behavioral: 3
        """

        resume_section = f"""
        Resume

        {resume.model_dump_json(indent=2)}
        """

        jd_section = f"""
        Job Description

        {job.model_dump_json(indent=2)}
        """

        assessment_section = f"""
        Candidate Assessment

        {assessment.model_dump_json(indent=2)}
        """

        output_schema = """
        Return ONLY valid JSON.

        {
            "overall_strategy": "...",
            "interviewer_notes": "...",
            "questions": [
                {
                    "category": "...",
                    "difficulty": "...",
                    "skill": "...",
                    "question": "...",
                    "purpose": "...",
                    "expected_signals": [],
                    "follow_up_questions": []
                }
            ]
        }
        """

        quality_rules = """
        Additional Requirements:

        - Do not generate generic textbook questions.
        - Every technical question must reference a skill or responsibility from the Job Description.
        - Prefer practical implementation questions over definition-based questions.
        - Assume the interview is for an experienced software engineer unless the Job Description specifies otherwise.
        - Questions should progressively increase in difficulty.
        - Do not repeat the same concept in multiple questions.
        - Generate concise, interview-ready questions.
        """

        return "\n\n".join(
            [
                role,
                objective,
                technical_rules,
                behavioral_rules,
                distribution,
                resume_section,
                jd_section,
                assessment_section,
                output_schema,
                quality_rules
            ]
        )