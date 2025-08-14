import os
from dotenv import load_dotenv #.envファイルの読み込み用
from google import genai #gemini AIのため

# .env　ファイルを読み込む
load_dotenv()

# APIキーの設定
api_key = os.getenv("API_KEY")

def execute(prompt, gemini_model='gemini-2.0-flash'):
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model= gemini_model,
        contents=prompt
    )
    return response.text

# 確認用
#print(execute(input("gemini aiへの命令を書き込んでください")))