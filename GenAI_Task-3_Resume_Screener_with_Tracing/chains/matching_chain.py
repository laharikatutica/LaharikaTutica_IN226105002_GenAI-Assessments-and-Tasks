from langchain_groq import ChatGroq
from prompts.match_prompt import match_prompt
from langchain_core.output_parsers import StrOutputParser

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

matching_chain = match_prompt | llm | StrOutputParser()