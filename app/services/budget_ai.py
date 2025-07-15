from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import Runnable
from langchain_openai import ChatOpenAI
from utils.file_handler import read_file_as_string
from dotenv import load_dotenv

load_dotenv()  

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.3, )

def get_budget_suggestion(data_dir: str) -> str:
    csv_text = read_file_as_string(data_dir)

    prompt = PromptTemplate(
        input_variables=["csv_data"],
        template="""
You are a financial planning assistant. Based on the following expense data, provide a detailed monthly budget recommendation. 
Focus on essential vs. non-essential expenses, and suggest savings opportunities.

Data:
{csv_data}
""",
    )

    chain: Runnable = prompt | llm
    response = chain.invoke({"csv_data": csv_text})

    return response.content
