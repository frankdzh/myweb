import openai_secret_manager
import openai
import streamlit as st

# Get API key
secrets = openai_secret_manager.get_secret("openai")
openai.api_key = secrets["api_key"]

def generate_cover_letter(prompt, temperature, max_tokens):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    message = completions.choices[0].text
    return message.strip()

def main():
    st.title("Cover Letter Generator")

    personal_info = st.text_input("Enter your personal information (name, contact information, etc.)")
    job_description = st.text_input("Enter the job description")
    temperature = st.slider("Select the tone of the letter", 0.0, 1.0, 0.5)
    max_tokens = st.slider("Select the number of words for the summary", 100, 500, 300)

    if st.button("Generate Cover Letter"):
        prompt = (f"Please generate a cover letter for the following job description: {job_description}. "
                  f"The letter should include the personal information: {personal_info}.")
        cover_letter = generate_cover_letter(prompt, temperature, max_tokens)
        st.success("Cover letter generated!")
        st.text(cover_letter)

    if st.button("Download Cover Letter"):
        prompt = (f"Please generate a cover letter for the following job description: {job_description}. "
                  f"The letter should include the personal information: {personal_info}.")
        cover_letter = generate_cover_letter(prompt, temperature, max_tokens)
        st.text("Cover letter saved!")
        st.markdown(f'<a href="data:text/plain;base64,{cover_letter}" download="cover_letter.txt">Download</a>',unsafe_allow_html=True)

if __name__ == "__main__":
    main()
