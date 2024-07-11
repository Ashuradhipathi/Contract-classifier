import streamlit as st
from utils import llm, extract_keypoints

'''import torch
from transformers import pipeline


chat = [
    {"role": "system", "content": "You are a sassy, wise-cracking robot as imagined by Hollywood circa 1986."},
    {"role": "user", "content": "Hey, can you tell me any fun things to do in New York?"}
]

pipe = pipeline("text-generation", "meta-llama/Meta-Llama-3-8B-Instruct", torch_dtype=torch.bfloat16, device_map="auto")
response = pipe(chat, max_new_tokens=512)
print(response[0]['generated_text'][-1]['content'])


chat = response[0]['generated_text']
chat.append(
    {"role": "user", "content": "Wait, what's so wild about soup cans?"}
)
response = pipe(chat, max_new_tokens=512)
print(response[0]['generated_text'][-1]['content'])
'''
def main():
    st.title("Contract comparator App")

    prompt = st.chat_input("If you have any doubts about clauses, let us know!")
    if prompt:
        st.write(f"User has sent the following prompt: {prompt}")
        response = llm.complete(prompt)
        st.write(response.text)
    


    if st.session_state['contract_text'] != '':
        with st.spinner('Extracting Contract...'):
            clauses = extract_keypoints(st.session_state['contract_text'])
        st.success("Done!")
        st.toast('Key Points extracted!')


        st.markdown(clauses.text)
    else:
        st.markdown("# Go back and upload the contract!!")
    


if __name__ == "__main__":
    main()