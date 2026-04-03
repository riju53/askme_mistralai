import streamlit as st
from mistralai import Mistral

model = "mistral-large-latest"

# ✅ Initialize client (THIS WAS MISSING)

api_key = st.secrets["MISTRAL_API_KEY"]
client = Mistral(api_key=api_key)

# UI
st.title("Askme anything 🚀")

with st.form('my_form'):
    text = st.text_input('Enter text:')
    submit = st.form_submit_button('Ask me')

if submit:
    if not api_key:
        st.error("Mistral API key not found.")
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
