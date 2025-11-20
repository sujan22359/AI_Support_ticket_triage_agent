import streamlit as st
import requests

API_URL = "http://localhost:8000/triage"

st.set_page_config(page_title="AI Ticket Triage", layout="centered")

st.title("Support Ticket Triage Agent")
st.write("Enter a support ticket description and let the AI classify & suggest next actions.")

description = st.text_area("Ticket Description", height=200)

if st.button("Triaged Ticket"):
    if not description.strip():
        st.error("Please enter a ticket description.")
    else:
        with st.spinner("Analyzing with AI..."):
            try:
                response = requests.post(API_URL, json={"description": description})
                result = response.json()

                # Display results
                st.subheader(" Summary")
                st.write(result.get("summary", ""))

                st.subheader("Category & Severity")
                st.write(f"**Category:** {result.get('category','')}")
                st.write(f"**Severity:** {result.get('severity','')}")

                st.subheader("Issue Type")
                st.write(f"**{result.get('issue_type','').upper()}**")

                st.subheader("Suggested Action")
                st.info(result.get("suggested_action",""))

                st.subheader(" KB Matches")
                kb_matches = result.get("kb_matches", [])
                for match in kb_matches:
                    st.write(f"- **{match['id']}** – {match['title']} (score: {match['score']:.2f})")
                    st.caption(f"Action: {match['recommended_action']}")

                st.subheader("Clarifying Questions")
                clarifying = result.get("clarifying_questions", [])
                if clarifying:
                    for q in clarifying:
                        st.write(f"- {q}")
                else:
                    st.write("No clarifying questions needed.")

            except Exception as e:
                st.error(f"Error calling API: {e}")
