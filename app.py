import streamlit as st
from openai import OpenAI

# --- Initialize OpenAI Client ---
client = OpenAI(api_key=st.secrets["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"])

# --- Email Writing Function ---
def write_email(user_prompt, tone="Formal"):
    system_prompt = f"You are a professional email writer. Write a complete {tone.lower()} email based on the user's instruction. Always use correct grammar and a clear structure."

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7,
        max_tokens=600
    )
    email_text = response.choices[0].message.content
    return email_text

# --- Streamlit Web App ---
st.title("Autonomous Email Writing Agent")

st.write("Enter a simple instruction and get a complete email drafted!")

user_prompt = st.text_area("Instruction", placeholder="E.g., Write a follow-up email after a meeting.")
tone = st.selectbox("Select Tone", ["Formal", "Friendly", "Concise", "Apologetic", "Persuasive"])

if st.button("Generate Email"):
    if user_prompt.strip() == "":
        st.warning("Please enter an instruction.")
    else:
        with st.spinner("Writing email..."):
            email = write_email(user_prompt, tone)
            st.subheader("Generated Email")
            st.text_area("Email Output", value=email, height=300)

st.caption("© 2025 Your Email AI Agent")
