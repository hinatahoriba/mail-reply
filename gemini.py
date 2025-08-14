import os
import streamlit as st
import google.generativeai as genai


# APIキーの設定
api_key = st.secrets["API_KEY"]

def execute(prompt, gemini_model='gemini-2.0-flash'):
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model= gemini_model,
        contents=prompt
    )
    return response.text

# 確認用
#print(execute(input("gemini aiへの命令を書き込んでください")))