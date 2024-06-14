import os
import streamlit as st
#from llama_index.readers.file import PDFReader
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding
import streamlit.components.v1 as components
from pypdf import PdfReader

global contract_text
global contract_template_text 

def extract_contract(contract_pdf):
    pdf_text = ""
    pdf_reader = PdfReader(contract_pdf)
    number_of_pages = len(pdf_reader.pages)
    for index in range(number_of_pages):
        pdf_text = pdf_text + pdf_reader.pages[index].extract_text()
    return pdf_text




# Set Google API key
GOOGLE_API_KEY = os.getenv("api")


def extract_keypoints(contract_text):
    key_points = llm.complete(f"You are a contract evaluator, You will be provided a contract, {contract_text}. return the key points that should be known to both the parties")
    return key_points

def extract_clauses(contract_text):
    clauses = llm.complete(f"You are a contract evaluator, You will be provided a contract, {contract_text}.Mention the key clauses and sub clauses of the contract and categorise the contents of contract under the clauses")
    return clauses

def find_deviations(contract_text, contract_template_text):    
    prompt = f"""
    You are a contract analysis expert.  
    You are given a contract and a template:

    Contract:
    ```
    {contract_text}
    ```

    Template:
    ```
    {contract_template_text}
    ```

    Analyze the contract and the template and identify any deviations.  
    Respond in the following format in markdown:

    - Deviation 1: [Explain the deviation]
    - Deviation 2: [Explain the deviation]
    ...

    Focus on structural differences, missing information, or inconsistencies.
    """

    response = llm.complete(prompt)
    
    return response.text



llm = Gemini(model="models/gemini-1.5-flash-latest", temperature=0, embedding=GeminiEmbedding,api_key=GOOGLE_API_KEY)

def main():
    st.title("Contract comparator App")

    
    st.write("Upload a Contract")
    contract_pdf = st.file_uploader("Upload Contract PDF", type=["pdf"])
    if contract_pdf:
        contract_text = extract_contract(contract_pdf)


    st.write("Upload Contract Template")
    contract_template_pdf = st.file_uploader("Upload Template PDF", type=["pdf"])
    if contract_template_pdf:
        contract_template_text = extract_contract(contract_template_pdf)

    
    if st.button("Key Points"):
        key_points = extract_keypoints(contract_text)
        st.markdown(key_points.text)

    if st.button("Clauses"):
        clauses = extract_clauses(contract_text)
        st.markdown(clauses.text)

    if st.button("Deviations"):
        deviations = find_deviations(contract_text, contract_template_text)
        #for deviation in deviations:
        #print(deviations)
        st.markdown(deviations)


if __name__ == "__main__":
    main()

