'''template = ''
    contract = ''
    # File upload
    uploaded_template_file = st.file_uploader("Upload a template file", type="pdf")
    
    if uploaded_template_file is not None:
        template = parser.load_data(file=uploaded_template_file)

    uploaded_Contract_file = st.file_uploader("Upload the Contract file", type="pdf")
    
    if uploaded_Contract_file is not None:
        contract = parser.load_data(file=uploaded_Contract_file)

    if contract and template:'''