import langchain_helper as lch
import streamlit as st
 

st.title("Pet Name Generator")

animal_type = st.sidebar.selectbox("what is your pet?",('Cat','Dog','Horse','Cow'))

if animal_type == "Cat":
    pet_color = st.sidebar.selectbox("what is your pet color",max_char=15)

if animal_type == "Dog":
    pet_color = st.sidebar.selectbox("what is your pet color",max_char=15)
if animal_type == "Horse":
    pet_color = st.sidebar.selectbox("what is your pet color",max_char=15)
if animal_type == "Cow":
    pet_color = st.sidebar.selectbox("what is your pet color",max_char=15)