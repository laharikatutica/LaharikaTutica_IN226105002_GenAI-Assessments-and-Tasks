from langchain_core.prompts import PromptTemplate

explain_prompt = PromptTemplate(
    input_variables=["score", "matched_data"],
    template="""
You are an AI hiring assistant. Write a clear explanation of the candidate's score.

Score: {score}
Matched Data: {matched_data}

Write a 3-5 sentence explanation covering:
1. Why this score was assigned
2. Key strengths of the candidate
3. Critical gaps or weaknesses
4. Hiring recommendation (Strong Yes / Maybe / No)
"""
)