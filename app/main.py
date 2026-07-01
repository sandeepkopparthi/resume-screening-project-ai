import os
from dotenv import load_dotenv
from groq import Groq
from app.parsers.pdf_parser import extract_text_from_pdf

#load environment variables from .env file
load_dotenv()

#read api key from environment variable
# api_key = os.getenv("GROQ_API_KEY")

# #create a Groq client instance with the api key
# client = Groq(api_key=api_key)

# #send request to LLM
# response = client.chat.completions.create(
#     model="llama-3.3-70b-versatile",
#     messages=[
#         {
#             "role":"system",
#             "content":"You are a resume parser agent."
#         },
#         {
#             "role":"user",
#             "content":"Parse the given resume and extract the current job role, Skills & Years of working Experience. Return the extracted details in json format. Don"
#             "t invent experience. If any details are missing don't assume and just return as 'Not Mentioned'."
#         }
#     ]
# )

# #print response
# print(response.choices[0].message.content)

# text = extract_text_from_pdf("resumes/Sandeep_Kopparthi_Senior_Frontend_Engineer_CV_2025.pdf")

# print(text[:1000])

from app.models.projects import Project

project = Project(
    project_name="Resume Screening"
)


print(project.model_dump())


