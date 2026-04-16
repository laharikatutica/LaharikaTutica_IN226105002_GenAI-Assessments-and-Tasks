from langchain_groq import ChatGroq
from prompts.explain_prompt import explain_prompt
from langchain_core.output_parsers import StrOutputParser

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

explanation_chain = explain_prompt | llm | StrOutputParser()