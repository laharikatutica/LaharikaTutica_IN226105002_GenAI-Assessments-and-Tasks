from langchain_groq import ChatGroq
from prompts.extract_prompt import extract_prompt
from langchain_core.output_parsers import StrOutputParser

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

extraction_chain = extract_prompt | llm | StrOutputParser()