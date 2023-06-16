import streamlit as st
import openai
from streamlit_chat import message

# Initial system message
initial_message = "You are a helpful assistant that teaches Python to a Year 10 student preparing for GCSE in a conversational manner. Always provide step-by-step explanations. Include example Python code in your responses when it would help to illustrate the concept."

st.title('Python Learning Assistant')

# Add a warning at the top of the application
st.warning('**Disclaimer:** This app helps you learn Python and sometimes provides code examples. We encourage you to practice these examples in your own Python environment. However, do not run code that you do not understand, due to potential unforeseen results.')

def main():
    
    # Input for OpenAI API Key
    st.markdown("<div style='background-color: #ffa500; padding:10px; margin-bottom:10px;'>Input your OpenAI API Key:</div>", unsafe_allow_html=True)
    openai.api_key = st.text_input("", type="password")

    if 'num_questions' not in st.session_state:
        st.session_state['num_questions'] = 0

    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    user_input = st.text_input("Ask a Python question")

    if st.button('Send'):
        st.session_state['num_questions'] += 1

        # Generate a response to the user's question
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"{initial_message}\nStudent asks a Python question: {user_input}\nHow would you teach them?",
            max_tokens=500,
        )

        assistant_message = response.choices[0].text.strip()

        # Add the user's message and the assistant's response to the chat history
        st.session_state['chat_history'].insert(0, [user_input, assistant_message])

        # Display the chat history
        for chat in st.session_state['chat_history']:
            message(f'You: {chat[0]}', is_user=True)
            message(f'Assistant: {chat[1]}')

        st.write(f'You have asked {st.session_state["num_questions"]} questions.')

if __name__ == "__main__":
    main()
