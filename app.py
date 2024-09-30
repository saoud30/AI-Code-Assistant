import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set page config first
st.set_page_config(page_title="Versatile Code Assistant", layout="wide")

# Custom CSS for improved chat input without overriding Streamlit's default background
st.markdown(
"""
<style>
.stTextInput > div > div > input {
color: white;
}
.stTextArea > div > div > textarea {
color: white;
}
/* Improve chat input styling */
.stChatInputContainer {
background-color: transparent !important;
}
.stChatInputContainer > div {
background-color: rgba(255, 255, 255, 0) !important; /* Changed to 0 */
border: 1px solid rgba(255, 255, 255, 0.2);
border-radius: 5px;
}
.stChatInputContainer input {
color: white !important;
}
/* Remove default Streamlit footer */
footer {
visibility: hidden;
}
</style>
""",
unsafe_allow_html=True
)

# Set up Groq client using API key from .env
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("API Key not found! Please set it in the .env file.")
else:
    os.environ["GROQ_API_KEY"] = api_key
    client = Groq()

def generate_response(prompt, mode, language=None, version=None):
    if mode == "Code Generation":
        system_content = f"You are a helpful assistant that generates {language} {version} code based on user prompts."
        user_content = f"Generate {language} {version} code for the following task: {prompt}"
    else:  # Conversation mode
        system_content = "You are a knowledgeable programming assistant capable of answering questions about various programming languages and concepts."
        user_content = prompt

    messages = [
        {"role": "system", "content": system_content},
        {"role": "user", "content": user_content}
    ]

    completion = client.chat.completions.create(
        model="llama3-groq-70b-8192-tool-use-preview",
        messages=messages,
        temperature=0.5,
        max_tokens=1024,
        top_p=0.65,
        stream=True,
        stop=None,
    )

    response = ""
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            response += chunk.choices[0].delta.content

    return response

st.title("🖥️ Versatile Code Assistant")

# Mode selection
mode = st.radio("Select mode:", ["Code Generation", "Conversation"])

if mode == "Code Generation":
    col1, col2, col3 = st.columns([3, 1, 1])

    with col1:
        prompt = st.text_area("Enter your code generation prompt:", height=100)

    with col2:
        languages = ["Python", "C", "C++"]
        selected_language = st.selectbox("Select language:", languages)

    with col3:
        if selected_language == "Python":
            versions = ["2.7.18", "3.5.10", "3.6.15", "3.7.12", "3.8.12", "3.9.13", "3.10.8", "3.11.3", "3.12.0"]
        elif selected_language == "C" or selected_language == "C++":
            versions = ["GCC 9.2.0"]
        selected_version = st.selectbox(f"Select {selected_language} version:", versions, index=len(versions)-1)

else:  # Conversation mode
    prompt = st.text_input("Ask a question about programming:")

if st.button("Generate Response"):
    if prompt:
        with st.spinner("Generating response..."):
            if mode == "Code Generation":
                response = generate_response(prompt, mode, selected_language, selected_version)
                st.code(response, language=selected_language.lower())
            else:
                response = generate_response(prompt, mode)
                st.markdown(response)
    else:
        st.warning("Please enter a prompt or question.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Chat with the assistant", key="chat_input"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = generate_response(prompt, "Conversation")
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

st.sidebar.header("About")
st.sidebar.info(
    "This Versatile Code Assistant uses the Groq API to generate code and answer programming questions. "
    "You can switch between Code Generation and Conversation modes to suit your needs."
)

st.sidebar.header("Instructions")
st.sidebar.markdown(
    """
    Code Generation Mode:
    1. Enter a clear and specific prompt describing the code you need.
    2. Select the desired language and version.
    3. Click the 'Generate Response' button.

    Conversation Mode:
    1. Enter a programming-related question or topic.
    2. Click the 'Generate Response' button or use the chat input at the bottom.
    3. Engage in a conversation about programming concepts.
    """
)
