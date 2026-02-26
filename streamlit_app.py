import streamlit as st
exec(open("tb_agent_complete.py").read())  # Your LangGraph agent!

st.title("🇮🇳 TB Cough Agent - LangGraph Powered")
audio = st.file_uploader("Upload cough", type=['wav'])

if st.button("🔍 Screen for TB") and audio:
    with st.spinner("LangGraph analyzing..."):
        result = tb_agent.invoke({"cough_audio": audio})
    
    st.success(f"**TB Risk:** {result['tb_risk']:.1%}")
    st.warning(f"**Status:** {result['risk_level']}")
    st.info(f"**हिंदी:** {result['hindi_alert']}")
