import streamlit as st
import ollama

# Page Config
st.set_page_config(page_title="AI Code Explainer", page_icon="🤖", layout="wide")

# Title
st.title("🤖 AI Code Explainer (Offline)")
st.write("Paste your code and get explanation instantly 🚀")

# Sidebar
st.sidebar.header("⚙️ Settings")
model_choice = st.sidebar.selectbox(
    "Choose Model",
    ["mistral", "phi", "llama3"]
)

language = st.sidebar.selectbox(
    "Programming Language",
    ["Python", "Java", "C++", "JavaScript"]
)

# Input Area
st.subheader("📥 Input Code")
code = st.text_area("Paste your code here:", height=250)

# Show code preview
if code:
    st.subheader("📄 Code Preview")
    st.code(code, language=language.lower())

# Button
if st.button("🚀 Explain Code"):
    if code.strip() == "":
        st.warning("Please enter some code!")
    else:
        with st.spinner("🤖 AI is analyzing your code..."):

            prompt = f"""
            You are an expert programming tutor.

            Analyze the following {language} code and provide:

            1. Simple Explanation (in easy words)
            2. Time Complexity
            3. Space Complexity
            4. Suggestions for Improvement

            Code:
            {code}
            """

            try:
                response = ollama.chat(
                    model=model_choice,
                    messages=[{'role': 'user', 'content': prompt}]
                )

                result = response['message']['content']

                # Output Sections
                st.subheader("📖 Explanation")
                st.markdown(result)

                # Download Button
                st.download_button(
                    label="📥 Download Result",
                    data=result,
                    file_name="code_explanation.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"Error: {e}")

# Footer
st.markdown("---")
st.markdown("💡 Built using Streamlit + Ollama (No API Key Required)")