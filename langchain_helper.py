from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.agents import create_agent
from langchain_core.tools import tool

from dotenv import load_dotenv
import os

load_dotenv()


def get_llm():
    llm = ChatOpenAI(
        model="openai/gpt-4o-mini",
        temperature=0.7,
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1",
    )

    return llm


def generate_pet_name(animal_type, pet_color):
    llm = get_llm()

    prompt_template_name = PromptTemplate(
        input_variables=["animal_type", "pet_color"],
        template=(
            "I have a {animal_type} pet and it is {pet_color} in color. "
            "I want a cool name for it. Suggest me five names for my pet."
        ),
    )

    chain = prompt_template_name | llm

    response = chain.invoke({
        "animal_type": animal_type,
        "pet_color": pet_color,
    })

    return response.content


@tool
def calculator(expression: str) -> str:
    """Calculate a mathematical expression."""
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"Error calculating expression: {e}"


def langchain_agent():
    llm = get_llm()

    agent = create_agent(
        model=llm,
        tools=[calculator],
    )

    result = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": (
                    "A horse has an average age of 20 years. "
                    "Use the calculator tool to multiply 20 by 3."
                ),
            }
        ]
    })

    print(result["messages"][-1].content)


if __name__ == "__main__":
    langchain_agent()
    # print(generate_pet_name("horse", "white"))
