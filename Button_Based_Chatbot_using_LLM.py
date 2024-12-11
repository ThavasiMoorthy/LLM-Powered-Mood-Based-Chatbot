import streamlit as st
from langchain_community.llms import Ollama  # Ensure this import works and Ollama is installed

# Initialize the language model with a higher temperature for more creative responses
llm = Ollama(model="llama3.1:latest", temperature=0.9)  # Adjust temperature for more response variety

# Define a function to generate a unique response based on mood
def generate_response(mood):
    # Define a prompt for the LLM to generate a unique response
    prompt = f"Generate a supportive and unique response for someone feeling {mood}."
    response = llm(prompt).strip()  # Get the response from the LLM
    return response

# Streamlit app layout
st.title("Mood Detection Chatbot")
st.write("How are you feeling right now? Please select one of the options below:")

# Mood button options
moods = ["Happy", "Sad", "Crying", "Stressed", "Scared"]

# Create a button for each mood
for mood in moods:
    if st.button(mood):
        response = generate_response(mood)  # Generate a response based on the selected mood
        st.success(response)  # Display the generated response
#FULL CODE WITH BUTTON