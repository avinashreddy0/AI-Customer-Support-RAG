import streamlit as st
from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
from config import LLM_MODEL

@st.cache_resource
def llm_model():
    pipe = pipeline('text-generation',model=LLM_MODEL,max_new_tokens = 100,do_sample = False,temperature = 0.,7return_full_text = False)

    llm = HuggingFacePipeline(pipeline=pipe)

 
    return llm
@st.cache_resource
def generation_answer(final_prompt):
    llm = llm_model()

    answer = llm.invoke(final_prompt)
    return answer
