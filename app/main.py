# with lang graph implementation

from app.models.screening_state import ScreeningState

from app.services.llm_service import LLMService

from app.nodes.resume_parser import ResumeParserNode
from app.nodes.jd_parser import JDParserNode
from app.nodes.candidate_evaluator import CandidateEvaluatorNode
from app.nodes.interview_generator import InterviewGeneratorNode

from app.graph.workflow import ScreeningWorkflow


def main():

    # -----------------------------
    # Infrastructure
    # -----------------------------

    llm_service = LLMService()

    # -----------------------------
    # Nodes
    # -----------------------------

    resume_parser = ResumeParserNode(llm_service)
    jd_parser = JDParserNode(llm_service)
    candidate_evaluator = CandidateEvaluatorNode(llm_service)
    interview_generator = InterviewGeneratorNode(llm_service)

    # -----------------------------
    # Workflow
    # -----------------------------

    workflow = ScreeningWorkflow(
        resume_parser=resume_parser,
        jd_parser=jd_parser,
        candidate_evaluator=candidate_evaluator,
        interview_generator=interview_generator,
    )

    # -----------------------------
    # Initial State
    # -----------------------------

    state = ScreeningState(
        resume_file_path="resumes/srimukhi_Tr_AME_CV.pdf",
        jd_file_path="job_descriptions/ame_jd.pdf",
    )

    # -----------------------------
    # Execute Workflow
    # -----------------------------

    result = workflow.invoke(state)

    # -----------------------------
    # Output
    # -----------------------------

    # print("Result:", result)

    print("result",result.model_dump_json(indent=4))


if __name__ == "__main__":
    main()

# without lang graph implementation
# import os
# from dotenv import load_dotenv
# from groq import Groq
# from app.nodes.candidate_evaluator import CandidateEvaluatorNode
# from app.nodes.interview_generator import InterviewGeneratorNode
# from app.nodes.jd_parser import JDParserNode
# from app.parsers.pdf_parser import extract_text_from_pdf

# #load environment variables from .env file
# load_dotenv()

# #read api key from environment variable
# # api_key = os.getenv("GROQ_API_KEY")

# # #create a Groq client instance with the api key
# # client = Groq(api_key=api_key)

# # #send request to LLM
# # response = client.chat.completions.create(
# #     model="llama-3.3-70b-versatile",
# #     messages=[
# #         {
# #             "role":"system",
# #             "content":"You are a resume parser agent."
# #         },
# #         {
# #             "role":"user",
# #             "content":"Parse the given resume and extract the current job role, Skills & Years of working Experience. Return the extracted details in json format. Don"
# #             "t invent experience. If any details are missing don't assume and just return as 'Not Mentioned'."
# #         }
# #     ]
# # )

# # #print response
# # print(response.choices[0].message.content)

# from app.nodes.resume_parser import ResumeParser
# from app.services.llm_service import LLMService
# from app.prompts.resume_parser_prompt import build_resume_parser_messages

# # text = extract_text_from_pdf("resumes/Sandeep_Kopparthi_Senior_Frontend_Engineer_CV_2025.pdf")


# # resume_parser = ResumeParser(llm_service)
# # print("resume parse method response:", resume_parser.parse(text))



# # jd_text = extract_text_from_pdf("job_descriptions/Sample_JD.pdf")

# # jd_parser = JDParserNode(llm_service)

# # job = jd_parser.parse(jd_text)

# # print(job)

# # print(text[:1000])

# # from app.models.education import Education
# # from app.models.projects import Project
# # from app.models.resume import Resume
# # from app.models.work_experience import WorkExperience

# # resume = Resume(
# #     candidate_name="Sandeep K",

# #     summary="Senior Software Engineer with experience in Angular, Node.js and AI.",

# #     current_job_role="Senior Software Engineer",

# #     total_years_experience="6 Years",

# #     technical_skills=[
# #         "Angular",
# #         "Node.js",
# #         "Python"
# #     ],

# #     education=[
# #         Education(
# #             degree="B.Tech",
# #             institution="JNTU",
# #             graduation_year="2020"
# #         )
# #     ],

# #     projects=[
# #         Project(
# #             project_name="Resume Screening Agent",
# #             candidate_role="Full Stack Developer",
# #             technologies_used=[
# #                 "Python",
# #                 "Groq"
# #             ]
# #         )
# #     ],

# #     work_experience=[
# #         WorkExperience(
# #             company="Plural Technology",
# #             role="Senior Software Engineer"
# #         )
# #     ]
# # )

# # print(resume.model_dump())

# llm_service = LLMService()

# resume_parser = ResumeParser(llm_service)

# jd_parser = JDParserNode(llm_service)

# evaluator = CandidateEvaluatorNode(llm_service)

# interviewer = InterviewGeneratorNode(llm_service)

# resume_text = extract_text_from_pdf("resumes/Sandeep_Kopparthi_Senior_Frontend_Engineer_CV_2025.pdf")

# resume = resume_parser.parse(resume_text)


# jd_text = extract_text_from_pdf("job_descriptions/Sample_JD.pdf")

# job = jd_parser.parse(jd_text)

# evaluation = evaluator.evaluate(
#     resume,
#     job
# )

# plan = interviewer.generate(
#     resume,
#     job,
#     evaluation,
# )

# print("=" * 80)
# print("OVERALL STRATEGY")
# print("=" * 80)
# print(plan.overall_strategy)

# print()

# print("=" * 80)
# print("INTERVIEWER NOTES")
# print("=" * 80)
# print(plan.interviewer_notes)

# from collections import defaultdict

# sections = defaultdict(list)

# for q in plan.questions:
#     sections[q.category].append(q)

# for category, questions in sections.items():

#     print()

#     print("=" * 80)

#     print(category)

#     print("=" * 80)

#     for q in questions:
#         print(f"- {q.question}")