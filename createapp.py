import streamlit as st
from transformers import pipeline

model = pipeline("text-generation", model="openai-gpt")

def main():

    st.title('Chatbot')
    st.sidebar.header('About')
    st.sidebar.text('This is a chatbot powered by GPT model.')
    st.sidebar.header('Instructions')
    st.sidebar.text('Enter your question in the text box and click on Generate button.')

    st.header('Ask me something!')
    text = st.text_area("How can I help you today?", height=200)

    if st.button("Generate"):

        if text:
            with st.spinner('Generating...'):
                content = model(text, max_length=200, num_return_sequences=1)[0]['generated_text']
            st.success("Answer:")
            st.write(content)
        else:
            st.warning("Please enter something.")
            
if __name__ == "__main__":  
    main()
