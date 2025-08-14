import streamlit as st
import google.generativeai as genai

# --- APIキーの設定 ---
# st.secretsを使って安全にAPIキーを取得
api_key = st.secrets["API_KEY"]
genai.configure(api_key=api_key)

# --- プロンプトをモデルに送信する関数 ---
def execute(prompt, gemini_model='gemini-1.5-flash'):
    # モデルを指定
    model = genai.GenerativeModel(gemini_model)
    
    # プロンプトを渡してコンテンツを生成
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"エラーが発生しました: {e}")
        return None

# 確認用
#print(execute(input("gemini aiへの命令を書き込んでください")))