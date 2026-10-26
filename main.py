import streamlit as st
from langchain.chat_models import init_chat_model
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import HumanMessage,AIMessage # AIMessage : message by llm 
import os

## Page config
st.set_page_config(page_title="Simple Langchain Chatbot with Groq 🚀",page_icon="🚀")

#Title 
st.title("🚀 Simple Langchain Chat with Groq")
st.markdown("Learn Langchain basics with Groq's ultra-fast inference")

with st.sidebar:
    st.header("Settings")

    # 2. Determine default key from Secrets or Environment Variables
    default_key = ""
    if "GROQ_API_KEY" in st.secrets:
       default_key = st.secrets["GROQ_API_KEY"]
    else:
       default_key = os.getenv("GROQ_API_KEY", "")

# 3. Create the password input field (pre-filled with the secret if available)
    api_key = st.text_input(
    "GROQ API KEY",
    value=default_key,
    type="password",
    help="Get a free API key at console.groq.com",)

# 4. Check if the key is provided before running the app
    if not api_key:
      st.warning("⚠️ Please enter your Groq API key to proceed.")
      st.stop()
    #Model selection
    model_name=st.selectbox(
        "Model",["openai/gpt-oss-120b","meta-llama/llama-prompt-guard-2-22m"]
        ,index=0
        )
    #clear button
    if st.button("Clear Chat"):
        st.session_state.messages=[]
        st.rerun()

#INitializae chat history 
if "messages" not in st.session_state:
    st.session_state.messages=[] # if first time

##Initialize llm
@st.cache_resource
# It tells Streamlit to cache the function's returned resource so it can 
# reuse it when the same arguments are supplied, instead of recreating the resource on every rerun.


# The cache is separate from chat history. st.cache_resource caches the chain, 
# whereas st.session_state.messages stores the conversation.
def get_chain(api_key,model_name):
    if not api_key:
        return None
    #initialize model
    llm=ChatGroq(groq_api_key=api_key,
             model_name=model_name,
             temperature=0.7,
             streaming=True)
    
    #Chat prompt template
    # prompt=ChatPromptTemplate.from_messages([
    #     ("system","You are a helpful assistant powered by Groq. Answer questions clearly and concisely"),
    #     ("user","{question}")
    # ])
    prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Answer clearly."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}")])

    ##create chain
    chain=prompt |llm |StrOutputParser()
    return chain

##get chain 
chain=get_chain(api_key,model_name)
if not chain:
    st.warning("Please enter your Groq API key in the sidebar to start chatting !")
    st.markdown("[Get your free API key here](https://console.groq.com)")
else:
    #display the chat message
    for mssg in st.session_state.messages:
        with st.chat_message(mssg["role"]):
            st.write(mssg["content"])


# The := operator
# This is called the walrus operator, or assignment expression.

# It assigns the returned value to question and checks that value in the same expression.

    #chat input
    if question:=st.chat_input("Ask me anything...."):
        #add user message to session state
        st.session_state.messages.append({"role":"user","content":question})
        #display
        with st.chat_message("user"):
            st.write(question)


        #Generate output/response
        with st.chat_message("assistant"):
            mssg_placeholder=st.empty()
            full_response=""

            try:
                #stream response from groq

                # this is same as following this is list comprehension 
            #    history = [                         
            #    HumanMessage(content=m["content"])
            #    if m["role"] == "user"
            #    else AIMessage(content=m["content"])
            #    for m in st.session_state.messages[:-1]
            #    ]
                history = []

                for m in st.session_state.messages[:-1]:
                   if m["role"] == "user":
                     history.append( HumanMessage(content=m["content"]))
                   else:
                     history.append(AIMessage(content=m["content"]))

                for chunk in chain.stream({
                 "history": history,
                  "question": question}):
                   full_response += chunk
                   mssg_placeholder.markdown(full_response)
                # for chunk in chain.stream({"question":question}):
                #     full_response+=chunk
                #     mssg_placeholder.markdown(full_response + "")
                # mssg_placeholder.markdown(full_response)

                #ADD to history
                st.session_state.messages.append({"role":"assistant","content":full_response})
            except Exception as e:
                st.error(f"Error:{str(e)}")


#Examples
st.markdown("-------")
st.markdown("### Try these examples")
col1,col2=st.columns(2)
with col1:
    st.markdown("-What is Langchain?")
    st.markdown("-Explain Groq's LPU technique")
with col2:
    st.markdown("-How do I learn programming?")
    st.markdown("-Write a haiku about AI")
#Footer s
st.markdown("---")
st.markdown("Built with Langchain & Groq | Experience the speed! ⚡")    