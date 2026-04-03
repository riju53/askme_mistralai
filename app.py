
import streamlit as st
from mistralai.client import Mistral

api_key = "ySNpbNwUdXVjoG2Hw1G6FaiPt3J6bZrZ"
model = "mistral-large-latest"

# UI
st.title("Askme anything 🚀")

with st.form('my_form'):
    text = st.text_input('Enter text:')
    submit = st.form_submit_button('Ask me')

if submit:
    if not api_key:
        st.error("Mistral API key not found. Please add your API key to Colab secrets as 'MISTRAL_API_KEY'.")
    elif text.strip():
        with st.spinner("Thinking..."):
            st.write("Model loaded ✅")

            response = client.chat.complete(
                model=model,
                messages=[
                    {"role": "user", "content": text}
                ]
            )

            st.write(response.choices[0].message.content)

    else:
        st.warning("Please enter a question!")
