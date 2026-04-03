import streamlit as st
from mistralai import Mistral

model = "mistral-large-latest"

# ✅ Fetch from secrets
api_key = st.secrets.get("MISTRAL_API_KEY")

# ✅ Handle missing key safely
if not api_key:
    st.error("❌ Mistral API key not found. Add it to secrets.toml")
    st.stop()

# Initialize client
client = Mistral(api_key=api_key)

# UI
st.title("Askme anything 🚀")

with st.form('my_form'):
    text = st.text_input('Enter text:')
    submit = st.form_submit_button('Ask me')

if submit:
    if text.strip():
        with st.spinner("Thinking..."):
            try:
                response = client.chat.complete(
                    model=model,
                    messages=[
                        {"role": "user", "content": text}
                    ]
                )

                st.write(response.choices[0].message.content)

            except Exception as e:
                st.error(f"Error: {str(e)}")

    else:
        st.warning("Please enter a question!")
