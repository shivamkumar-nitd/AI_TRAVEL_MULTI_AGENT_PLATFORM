# ✈️ AI Travel Planner

An AI-powered multi-agent travel planning application built using **LangGraph**, **Groq LLM**, **Streamlit**, and **PostgreSQL**. The application generates personalized travel itineraries by combining flight information, hotel recommendations, and AI-generated travel plans through a collaborative agent workflow.

---

## 🚀 Features

- 🤖 Multi-Agent workflow using LangGraph
- ✈️ Flight search integration
- 🏨 Hotel recommendations using Tavily Search
- 🗺️ AI-generated personalized travel itineraries
- 💬 Streaming responses in Streamlit
- 🧠 Persistent conversation memory using PostgreSQL Checkpointer
- 👤 User-specific conversation history
- ⚡ Powered by Groq Llama 3.3 70B
- 📊 Live agent execution visualization

---

# 🏗️ Architecture

```
                    User
                      │
                      ▼
              Streamlit Frontend
                      │
                      ▼
                LangGraph Workflow
                      │
      ┌───────────────┼───────────────┐
      ▼               ▼               ▼
 Flight Agent    Hotel Agent    Itinerary Agent
      │               │               │
      └───────────────┼───────────────┘
                      ▼
               Final Response Agent
                      │
                      ▼
                  Streamlit UI
```

---

# 🤖 Agent Workflow

### Flight Agent

- Searches available flights
- Fetches airline information
- Returns structured flight results

---

### Hotel Agent

- Uses Tavily Search
- Finds hotels based on user destination
- Returns hotel recommendations

---

### Itinerary Agent

Combines

- User preferences
- Flight information
- Hotel recommendations

to generate a complete travel itinerary.

---

### Final Agent

Creates a polished response including

- Flight summary
- Hotel suggestions
- Day-wise itinerary
- Travel tips

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Streamlit | Frontend |
| LangGraph | Multi-Agent Workflow |
| Groq Llama 3.3 70B | LLM |
| PostgreSQL | Memory & Checkpointing |
| Tavily API | Hotel Search |
| AviationStack API | Flight Search |
| Psycopg | PostgreSQL Driver |
| LangChain | LLM Framework |

---

# 📂 Project Structure

```
air_travel/

│── frontend.py
│── main.py
│── users.py
│── .env
│── requirements.txt

│
├── tools
│   ├── flight_tool.py
│   └── tavily_tool.py

│
├── assets

│
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone {repo link}

cd repo name
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
GROQ_API_KEY=your_groq_key

TAVILY_API_KEY=your_tavily_key

AVIATIONSTACK_API_KEY=your_aviationstack_key

DATABASE_URL=postgresql://username:password@localhost:5432/travel_db
```

---

# 🗄️ PostgreSQL Setup

Create the database.

Then create the user table.

```sql
CREATE TABLE IF NOT EXISTS users(
    user_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

LangGraph automatically creates

- checkpoints
- checkpoint_blobs
- checkpoint_writes

during initialization.

---

# ▶️ Run the Application

```bash
streamlit run frontend.py
```

---

# 🧠 Conversation Memory

Each user receives a unique **User ID**.

The application stores conversation checkpoints in PostgreSQL using LangGraph's `PostgresSaver`.

This enables persistent memory across sessions for individual users.

---

# 📸 Screenshots

Add screenshots here.

Example:

```
assets/home.png

assets/result.png

assets/agents.png
```

---

# Future Improvements

- 🔐 User Authentication
- 🌍 Google Maps Integration
- 💳 Flight & Hotel Booking
- 📅 Calendar Export
- 🧳 Budget Optimizer
- 🌦️ Weather Forecast
- 🚖 Local Transport Suggestions
- 🗣️ Voice Assistant
- 🌐 Multi-language Support

---

# Learning Outcomes

This project demonstrates practical implementation of

- Multi-Agent AI Systems
- LangGraph State Management
- LLM Orchestration
- Persistent AI Memory
- PostgreSQL Checkpointing
- Streamlit Frontend Development
- API Integration
- Prompt Engineering

---

# Author

**Shivam Kumar**

B.Tech, Metallurgical and Materials Engineering

National Institute of Technology Durgapur

GitHub: https://github.com/shivamkumar-nitd

LinkedIn: https://www.linkedin.com/in/shivamkumarnit/

---

