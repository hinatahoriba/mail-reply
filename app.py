import streamlit as st
from gemini import execute

st.set_page_config(
    page_title="AIメール自動作成",
    page_icon="✨",
    layout="wide"
)

with st.form("make_replay"):
    my_position = st.text_input("あなたの立場や役職")
    sender_name = st.text_input("送信者")
    received_email_content = st.text_area("届いたメールの内容をコピペしてください")
    main_points = st.text_input("返信で伝える内容")
    tone = st.selectbox(
        '返信のトーンを選んでください:',
        ('フォーマル', 'カジュアル', '丁寧', '簡潔')
    )
    submitted = st.form_submit_button("作成")

    if submitted:
        prompt = f"""{my_position}として、{sender_name}からの以下のメールへ返信を作成してください。
        届いたメール:{received_email_content}
        返信で伝える要点: {main_points}
        返信のトーン: {tone}
        """
                
        st.write(execute(prompt))
        st.success("フォームが送信されました！")

# --- アプリケーションのフッター ---
st.write('---')
st.write('©HinataHoriba')
