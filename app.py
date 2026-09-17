import streamlit as st

st.set_page_config(page_title="Fake News Detector", layout="centered")
st.title("📰 AI Fake News Detector")
st.markdown("An NLP based tool to detect misleading news")

news = st.text_area("Paste News Article / Headline here", height=180)

if st.button("Analyze News"):
    if news.strip() == "":
        st.warning("Please enter some news text")
    else:
        # Pro logic scoring
        fake_words = ["shocking", "miracle", "you won't believe", "free money", "100% guaranteed", "click here", "viral", "secret"]
        score = 0
        for w in fake_words:
            if w in news.lower():
                score += 20
        
        # length & caps check
        if news.isupper():
            score += 20
        if len(news.split()) < 8:
            score += 15

        st.subheader("Analysis Result:")
        if score >= 40:
            st.error(f"🚨 LIKELY FAKE NEWS (Risk Score: {score}%)")
            st.write("Reason: Contains sensational / clickbait language")
        elif score >= 20:
            st.warning(f"⚠️ SUSPICIOUS (Risk Score: {score}%)")
            st.write("Reason: Some misleading patterns found, needs verification")
        else:
            st.success(f"✅ LIKELY REAL (Risk Score: {score}%)")
            st.write("Reason: No sensational patterns detected")

        st.progress(score)

st.divider()
st.caption("Built with Python | Streamlit | NLP | Ishika Nainwal")
