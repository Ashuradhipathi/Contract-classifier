import os
import streamlit as st
from utils import extract_contract, llm, extract_keypoints


st.session_state['contract_text'] = ''
st.session_state['contract_template_text'] = ''




def main():
    st.title("Contract comparator App")

    prompt = st.chat_input("If you have any doubts about contract and template formats, let us know!")
    if prompt:
        st.write(f"User has sent the following prompt: {prompt}")
        response = llm.complete(prompt)
        st.write(response.text)

    
    st.write("Upload a Contract")
    st.session_state['contract_pdf'] = st.file_uploader("Upload Contract PDF", type=["pdf"])
    if st.session_state['contract_pdf']:
        with st.spinner('Extracting Contract...'):
            st.session_state['contract_text'] =  extract_contract(st.session_state['contract_pdf'])
        st.success("Done!")
        st.toast('Contract extracted!')



    st.write("Upload Contract Template")
    st.session_state['template_pdf'] = st.file_uploader("Upload Template PDF", type=["pdf"])
    if st.session_state['template_pdf']:
        with st.spinner('Extracting Contract Template...'):
            st.session_state['contract_template_text'] = extract_contract(st.session_state['template_pdf'])
        st.success("Done!")
        st.toast('Template extracted!')





if __name__ == "__main__":
    main()

