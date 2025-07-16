from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
import streamlit as st

load_dotenv()

st.title('LLM機能を搭載したWebアプリ')

st.write("##### 動作モード1: 健康に関する専門家")
st.write("健康に関する質問にお答えします。")
st.write("##### 動作モード2: 教育に関する専門家")
st.write("教育に関する質問にお答えします。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["健康に関する専門家", "教育に関する専門家"]
)

st.divider()

if selected_item == "健康に関する専門家":
    st.write("健康に関する質問を入力してください。")
else:
    st.write("教育に関する質問を入力してください。")
user_input = st.text_input("質問:")

if st.button("送信"):
    st.divider()
    st.write(f"送信された質問: {user_input}")
    # ここで健康に関する処理を行う
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    messages = [
        SystemMessage(content=f"あなたは{selected_item}です。"),
        HumanMessage(content=user_input),
    ]

    result = llm(messages)
    st.write(f"回答：{result.content}")

