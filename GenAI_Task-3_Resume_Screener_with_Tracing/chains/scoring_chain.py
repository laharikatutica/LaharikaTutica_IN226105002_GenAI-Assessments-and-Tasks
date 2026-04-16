from langchain_groq import ChatGroq
from prompts.score_prompt import score_prompt
from langchain_core.output_parsers import StrOutputParser

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

scoring_chain = score_prompt | llm | StrOutputParser()

