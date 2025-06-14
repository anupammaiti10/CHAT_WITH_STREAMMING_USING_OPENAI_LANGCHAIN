import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
# from langchain.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY") or "" #os.getenv("OPENAI_API_KEY") can return A str (if the environment variable exists

# Streamlit Ui
st.title("LangChain + OpenAI + Streamlit")
st.write("This is a demo of LangChain with OpenAI and Streamlit.")
# Here we are using ChatOpenAI because it comes from the chat_models module not from the llm module. chat_models directly use prompts for process but we have to given prompt with the llm using of others chains
llm=ChatOpenAI(model="openai/gpt-4.1",base_url="https://models.github.ai/inference",streaming=True,temperature=0.9) # If the ChatOpenAI is not import from the langchain_community then it would be error line .


prompts:list=[SystemMessage(content="You are a helpful assistant and it find that it is the error you have to given proper ans ")]

def get_chatmodel_response(question:str):
    global prompts
    prompts.append(HumanMessage(content=question))
    # Stream the response
    response = st.write_stream(
        llm.stream(prompts)  # Stream chunks
    )
    # answer.stream(lambda message: st.write(answer.content))
    prompts.append(AIMessage(content=response))
    return response


input=st.text_input("Ask a question:")
 
submit=st.button("Send")


if submit:
    
    st.spinner("The Response is:")
    response=get_chatmodel_response(input)
    # st.write(response)