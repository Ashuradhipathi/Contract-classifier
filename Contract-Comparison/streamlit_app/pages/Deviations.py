import streamlit as st
from utils import find_deviations
from utils import llm



def main():
    st.title("Contract comparator App")

    prompt = st.chat_input("If you have any doubts about contract and template formats, let us know!")
    if prompt:
        st.write(f"User has sent the following prompt: {prompt}")
        response = llm.complete(prompt)
        st.write(response.text)


    if st.session_state['contract_text'] != '' and st.session_state['contract_template_text'] != '':
        with st.spinner('Wait for it...'):
            clauses = find_deviations(st.session_state['contract_text'],st.session_state['contract_template_text'])
            st.toast('Clauses extracted!')
            st.success("Done!")
        st.markdown(clauses)
    else:
        st.markdown("# Go back and upload the contract!!")




if __name__ == "__main__":
    main()