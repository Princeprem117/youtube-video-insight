from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os
load_dotenv()

def generate_pet_name(animal_type, pet_color):
    llm = ChatOpenAI(
        model_name="openai/gpt-4o-mini",
        temperature=0.7,
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1",
        )
    prompt_template_name=PromptTemplate(
        input_variables = ['animal_type','pet_color'],
        template="I have a {animal_type} pet and it is {pet_color} in color.I want a cool name for it. Suggest me five names for my pet",
    )
    chain = prompt_template_name | llm
    response = chain.invoke({
        "animal_type": animal_type,
        "pet_color": pet_color
        })
    return response.content

if __name__ == "__main__":
    print(generate_pet_name("horse", "white"))