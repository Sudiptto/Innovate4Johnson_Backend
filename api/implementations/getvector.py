
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()

api_key = os.environ.get("GOOGLE_API_KEY")
if api_key is None:
    raise ValueError("GOOGLE_API_KEY environment variable not found.")

genai.configure(api_key=api_key)

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)


def get_vector(listing_info, resume_text, candidate_id):
    prompt = """
    You are an AI assistant that processes resumes and evaluates them against job requirements. You will be given three inputs:

1. The **job listing**, which includes a description of the role, required skills, qualifications, and experience.
2. The **raw text of a resume**.
3. A unique **candidate ID** for identification.

Your task is to:
- Evaluate the resume based on the job listing.
- Return a **vector of scores** with four values in the following structure: `[candidate_id, technical_skill, experience, education]`.

Each score should be on a scale of 1 to 10, and the evaluation should be based on the following criteria:

1. **Technical Skills**: Evaluate how well the candidate’s technical skills match the job requirements. Consider both direct skills (those explicitly listed in the job description) and related skills (skills that are similar, commonly used together, or enhance the required skills). 
   - 1 means an average match, while 10 means a perfect match.

2. **Experience**: Evaluate the candidate’s experience based on both the **number of years** and the **relevance and depth** of their experience. In assessing relevance, consider whether their job roles, tasks, and achievements align closely with the job’s responsibilities.
   - 1 means an average match, while 10 means a perfect match.

3. **Education**: Evaluate how well the candidate’s educational background matches the job’s education requirements (e.g., degree, certifications).
   - 1 means an average match, 10 means a perfect match.

Your output should be a vector in the following format:

[candidate_id, technical_skill, experience, education]
    """

    response = llm.invoke(prompt, resume_text, listing_info, candidate_id)

    # Extract the vector from the response
    vector = [candidate_id] + [int(score) for score in response.split(",")]

    return vector