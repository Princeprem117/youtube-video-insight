import langchain_helper as lch
import streamlit as st
 

st.title("Pet Name Generator")

user_animal_type = st.sidebar.selectbox("what is your pet?",('Cat','Dog','Horse','Cow'))

if user_animal_type == "Cat":
    pet_color = st.sidebar.text_area(label="what is your pet color",max_chars=15)

if user_animal_type == "Dog":
    pet_color = st.sidebar.text_area(label="what is your pet color",max_chars=15)
if user_animal_type == "Horse":
    pet_color = st.sidebar.text_area(label="what is your pet color",max_chars=15)
if user_animal_type == "Cow":
    pet_color = st.sidebar.text_area(label="what is your pet color",max_chars=15)


if pet_color:
    response = lch.generate_pet_name(user_animal_type, pet_color)
    st.markdown(response)