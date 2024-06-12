import os
import streamlit as st
#from llama_index.readers.file import PDFReader
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding
import streamlit.components.v1 as components
from pypdf import PdfReader



# Download PDFReader
contract_template = PdfReader("/workspaces/Contract-classifier/Contract-Comparison/streamlit_app/juro-affiliate-marketing-agreement-template.pdf")
contract_template_text = contract_template.pages[0].extract_text()

contract =  PdfReader("/workspaces/Contract-classifier/Contract-Comparison/streamlit_app/affiliatetermsofuse11911.pdf")
contract_text = contract.pages[0].extract_text()



# Set Google API key
GOOGLE_API_KEY = os.getenv("api")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


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



llm = Gemini(model="models/gemini-1.5-flash-latest", temperature=0, embedding=GeminiEmbedding,)

def main():
    st.title("Contract comparator App")
    
    if st.button("Key Points"):
        key_points = extract_keypoints(contract_template_text)
        st.markdown(key_points.text)

    if st.button("Clauses"):
        clauses = extract_clauses(contract_template_text)
        st.markdown(clauses.text)

    if st.button("Deviations"):
        deviations = find_deviations(contract_text, contract_template_text)
        #for deviation in deviations:
        #print(deviations)
        st.markdown(deviations)


if __name__ == "__main__":
    main()

