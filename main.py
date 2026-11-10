   
import streamlit as st
from langchain.chat_models import init_chat_model
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import HumanMessage,AIMessage # AIMessage : message by llm 
import os

load_dotenv()
## Page config
st.set_page_config(page_title="Simple Langchain Chatbot with Groq 🚀",page_icon="🚀")

#Title 
st.title("🚀 Simple Langchain Chat with Groq")
st.markdown("Learn Langchain basics with Groq's ultra-fast inference")

with st.sidebar:
    st.title("⚙️ Settings")
    st.caption("Configure your model and chat options")
    st.divider()
   
    #API key
    api_key=os.getenv("GROQ_API_KEY")
    if not api_key:
        print("api key not found..........")
    #Model selection
    model_name=st.selectbox(
        "Model", 
        ["openai/gpt-oss-120b","qwen/qwen3.8-27b"], 
        index=0
    )
    st.divider()

    if st.button("New Chat"):
            st.session_state.messages=[]
            st.rerun()
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
    st.warning("Please select your model from left sidebar!")
    # st.markdown("[Get your free API key here](https://console.groq.com)")
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
        with  st.chat_message("user"):
            st.write(question)


        #Generate output/response
        with st.chat_message("assistant"):
            mssg_placeholder=st.empty()
            full_response=""

            try:
                
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
                
                #ADD to history
                st.session_state.messages.append({"role":"assistant","content":full_response})
            except Exception as e:
                st.error(f"Error:{str(e)}")


#Examples
if len(st.session_state.messages)==0:
    _, center_col, _ = st.columns([1, 4, 1])
    with center_col:
      st.markdown("<h2 style='text-align: center;'>How can I help you today?</h2>", unsafe_allow_html=True)
      st.markdown("<p style='text-align: center; color: gray;'>Powered by Langchain & Groq ultra-fast inference</p>", unsafe_allow_html=True)
    
    st.write("") # Generates intentional layout spacing
    st.write("") 

# 2. Modern 2x2 Grid Prompt Layout using native columns
    col1, col2 = st.columns(2)

    with col1:
     if st.button("💡 Explain a concept\n\nWhat is Langchain and how does it work?", use_container_width=True):
        st.session_state.chat_input_value = "What is Langchain and how does it work?"
        st.rerun()
        
     if st.button("🚀 Analyze architecture\n\nExplain Groq's LPU hardware technique", use_container_width=True):
        st.session_state.chat_input_value = "Explain Groq's LPU hardware technique"

    with col2:
     if st.button("💻 Write & debug code\n\nHelp me learn backend programming step-by-step", use_container_width=True):
        st.session_state.chat_input_value = "Help me learn backend programming step-by-step"
        
     if st.button("📝 Brainstorm ideas\n\nWrite a creative haiku about artificial intelligence", use_container_width=True):
        st.session_state.chat_input_value = "Write a creative haiku about artificial intelligence"
