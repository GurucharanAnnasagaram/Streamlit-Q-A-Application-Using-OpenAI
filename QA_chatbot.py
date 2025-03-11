import os
import streamlit as st
from langchain.llms import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Function to load OpenAI model and get response
def get_openai_response(question):
    # Initialize the OpenAI model with the correct API key and model name
    llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), model_name="text-moderation-latest", temperature=0.5)
    response = llm(question)
    return response


# Initialize Streamlit
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")

# Input field for the user's question
user_input = st.text_input("Input:", key="input")

# Button to submit the question
if st.button("Ask the question"):
    if user_input:
        # Get response from OpenAI
        response = get_openai_response(user_input)
        # Display the response
        st.subheader("The response is:")
        st.write(response)
    else:
        st.write("Please enter a question.")
