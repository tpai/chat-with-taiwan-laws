import os
import streamlit as st

from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

# Environment variables
OPENAI_MODEL = os.environ.get("OPENAI_MODEL", "gpt-3.5-turbo")

# Load embeddings and database
embeddings = OpenAIEmbeddings()
db = FAISS.load_local("faiss_index", embeddings)

# Create a retrieval chain with the ChatOpenAI model
chain = RetrievalQAWithSourcesChain.from_chain_type(llm=ChatOpenAI(model_name=OPENAI_MODEL, temperature=0), chain_type="stuff", retriever=db.as_retriever(), max_tokens_limit=3500, reduce_k_below_max_tokens=True)

# Streamlit input field and text area
st.title("台灣法規問答 AI")
st.markdown("""
[![](https://img.shields.io/badge/tpai/chat_with_taiwan_laws-grey?style=flat-square&logo=github)](https://github.com/tpai/chat-with-taiwan-laws)
""")
# Description block
st.markdown("""
本工具引用自全國法規資料庫之[民法](https://law.moj.gov.tw/Hot/AddHotLaw.ashx?pcode=B0000001)、[民事訴訟法](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=B0010001)、[民事訴訟法施行法](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=B0010002)、[中華民國刑法](https://law.moj.gov.tw/Hot/AddHotLaw.ashx?pcode=C0000001)、[中華民國刑法施行法](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=C0000002)、[刑事訴訟法](https://law.moj.gov.tw/Hot/AddHotLaw.ashx?pcode=C0010001)、[刑事訴訟法施行法](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=C0010002)、[社會秩序維護法](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0080067)、[違反社會秩序維護法案件處理辦法](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0080070)、[地方法院與警察機關處理違反社會秩序維護法案件聯繫辦法](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0080076)、[跟蹤騷擾防制法](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0080211)、[跟蹤騷擾防制法施行細則](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0080213)、[跟蹤騷擾案件保護令執行辦法](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=D0080214)、[勞動基準法](https://law.moj.gov.tw/Hot/AddHotLaw.ashx?pcode=N0030001)、[勞工退休金條例](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=N0030020)以及[職業安全衛生設施條例](https://law.moj.gov.tw/Hot/AddHotLaw.ashx?pcode=N0060009)之 PDF 檔案，本工具僅供研究和學習使用，如有法律需求請諮詢專業律師。
""")
question = st.text_input("請輸入您的問題：")
if question:
    with st.spinner("🤖 思考中，請稍候..."):
        output = chain({"question": f"{question} 請用台灣繁體中文回答"}, return_only_outputs=True)
    st.text_area("🤖：", value=output["answer"], height=200)
