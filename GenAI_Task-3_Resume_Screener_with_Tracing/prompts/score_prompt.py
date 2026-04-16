from langchain_core.prompts import PromptTemplate

score_prompt = PromptTemplate(
    input_variables=["matched_data", "job_description"],
    template="""
You are an objective scoring engine. Based on the match analysis, assign a fit score.

Match Analysis:
{matched_data}

Job Description:
{job_description}

Rules:
- Score must be between 0 and 100
- Be strict and objective
- Do NOT inflate scores

Return ONLY this:
Score: <number between 0-100>
"""
)