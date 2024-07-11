import streamlit as st
from utils import extract_clauses
from utils import llm


def main():
    st.title("Contract comparator App")

    prompt = st.chat_input("If you have any doubts about clauses, let us know!")
    if prompt:
        st.write(f"User has sent the following prompt: {prompt}")
        response = llm.complete(prompt)
        st.write(response.text)
    


    if st.session_state['contract_text'] != '':
        with st.spinner('Extracting Contract...'):
            clauses = extract_clauses(st.session_state['contract_text'])
        st.success("Done!")
        st.toast('Contract extracted!')


        st.markdown(clauses.text)
    else:
        st.markdown("# Go back and upload the contract!!")




if __name__ == "__main__":
    main()