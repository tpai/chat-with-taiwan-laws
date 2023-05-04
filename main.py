import streamlit as st

from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

# Load embeddings and database
embeddings = OpenAIEmbeddings()
db = FAISS.load_local("faiss_index", embeddings)

# Create a retrieval chain with the ChatOpenAI model
chain = RetrievalQAWithSourcesChain.from_chain_type(llm=ChatOpenAI(model_name="gpt-4", temperature=0), chain_type="stuff", retriever=db.as_retriever(), max_tokens_limit=2500, reduce_k_below_max_tokens=True)

# Streamlit input field and text area
st.title("台灣法規問答 AI")
st.markdown("""
[![](https://img.shields.io/badge/tpai/chat_with_taiwan_laws-grey?style=flat-square&logo=github)](https://github.com/tpai/chat-with-taiwan-laws)
""")
# Description block
st.markdown("""
本工具引用自全國法規資料庫之[民法](https://law.moj.gov.tw/Hot/AddHotLaw.ashx?pcode=B0000001)、[中華民國刑法](https://law.moj.gov.tw/Hot/AddHotLaw.ashx?pcode=C0000001)、[刑事訴訟法](https://law.moj.gov.tw/Hot/AddHotLaw.ashx?pcode=C0010001)、[勞動基準法](https://law.moj.gov.tw/Hot/AddHotLaw.ashx?pcode=N0030001)、[勞工退休金條例](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=N0030020)以及[職業安全衛生設施條例](https://law.moj.gov.tw/Hot/AddHotLaw.ashx?pcode=N0060009)之 PDF 檔案，本工具僅供研究和學習使用，如有法律需求請諮詢專業律師。
""")
question = st.text_input("請輸入您的問題：")
if question:
    with st.spinner("🤖 思考中，請稍候..."):
        output = chain({"question": f"{question} 請用台灣繁體中文回答"}, return_only_outputs=True)
    st.text_area("🤖：", value=output["answer"], height=200)
