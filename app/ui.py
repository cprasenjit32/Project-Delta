import streamlit as st
import json

st.set_page_config(page_title="Project Delta - CR Generator", layout="centered")

st.title("🚀 Project Delta")
st.subheader("Auto-Generate Change Request from Ticket")

# Input ticket JSON
ticket_input = st.text_area("📩 Paste Ticket JSON (from Freshdesk/Jira)", height=250)

if st.button("Generate CR"):
    if not ticket_input:
        st.warning("Please paste a ticket first.")
    else:
        try:
            # Try parsing the JSON
            ticket = json.loads(ticket_input)

            # Mock CR generation (you'll replace this with real LLM agent later)
            cr_output = {
                "title": f"{ticket.get('subject', 'Change Request')}",
                "env": ticket.get("environment", "LLE/PROD"),
                "type": "Normal",
                "risk": ticket.get("priority", "Medium"),
                "requested_by": ticket.get("requested_by", "DevOps Team"),
                "status": "Pending Approval"
            }

            st.success("✅ Change Request Generated:")
            st.json(cr_output)

        except Exception as e:
            st.error(f"❌ Invalid JSON: {e}")

