# 🚀 Project Delta - AI-powered Change & Release Automation (MVP)

Project Delta is a solo-founder SaaS prototype that automates change request creation, validation, CAB approval, and calendar tracking using GPT-based AI agents.

## 🧱 MVP Scope (Week 1)
✅ Submit mock deployment request  
✅ Use LLM to generate a draft change request  
✅ Store CRs in SQLite  
✅ Display CRs in a basic calendar

## 📦 Tech Stack
- Streamlit (Frontend)
- FastAPI (Backend API)
- LangChain + OpenAI GPT-4o (LLM Agent)
- Freshdesk & ServiceNow API (mocked for now)
- SQLite → PostgreSQL (next phase)

## 🔧 Setup

```bash
git clone https://github.com/your-username/project-delta.git
cd project-delta
pip install -r requirements.txt
streamlit run app/ui.py
```

## 📁 Folder Structure
- `app/`: UI + LLM + CR generator
- `integrations/`: Freshdesk, SNOW, Slack APIs
- `calendar/`: Change calendar view
- `database/`: SQLite schema

## 🚧 Next Phases
- Live webhook integration
- PROD CAB agent (Slack approval flow)
- Full SNOW automation
- Dashboard reports

---

Project Delta is built by [Your Name], Release Manager turned AI-SaaS Founder 💼🚀
