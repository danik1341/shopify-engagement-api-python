
## 🧠 Shopify Engagement Tracker API – FastAPI

This is the **Python FastAPI** backend for the Shopify Engagement Tracker. It receives tracking data from the frontend and generates short, personalized engagement messages using the OpenAI API.

> ✅ Built with [FastAPI](https://fastapi.tiangolo.com/), Python, and OpenAI

---

## 📦 Features

* Receives session data from `tracker.js`
* Uses OpenAI to generate tailored popup messages
* Logic handles:

  * First-time visitors
  * Returning users with cart items
  * Cart interactions and page views
* Lightweight and production-ready

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/shopify-engagement-api-python.git
cd shopify-engagement-api-python
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # On macOS/Linux
venv\Scripts\activate           # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env`

```env
OPENAI_API_KEY=sk-...
PORT=3030
HOST=0.0.0.0
```

> `.env` is automatically loaded using `python-dotenv`.

### 5. Run the server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 3030
```

---

## 📂 Project Structure

```
.
├── main.py                      # FastAPI app entrypoint
├── routers/
│   └── tracker.py              # Handles /track-session route
├── services/
│   └── tracker.py              # Core logic for session handling and prompt building
├── llm/
│   └── openai_client.py        # OpenAI Chat API wrapper
├── models/
│   ├── session.py              # Pydantic session models
│   └── events.py               # Event model
├── .env
├── requirements.txt
```

---

## 🔌 API Endpoint

### `POST /track-session`

#### Request body

```json
{
  "time_on_site": 130,
  "current_page": "/products/snowboard-1",
  "cart_items": [
    { "title": "Speedy Board", "quantity": 1 }
  ],
  "current_cart_count": 1,
  "events": [
    { "type": "page_view", "at": 1696589273000 }
  ],
  "user_id": "optional-123"
}
```

#### Response

```json
{
  "show": true,
  "message": "Looks like you're checking out Speedy Board! Want help choosing accessories?"
}
```

---

## 🧠 OpenAI Integration

Messages are generated using `gpt-3.5-turbo`. The prompt is dynamically constructed based on:

* Cart contents (titles + quantities)
* Page location
* Time on site
* Interaction events (add\_to\_cart, etc.)

Make sure `OPENAI_API_KEY` is provided in your `.env` file.

---

## ⚙️ Configuration

Environment values are read from `.env`:

| Key              | Description                    |
| ---------------- | ------------------------------ |
| `OPENAI_API_KEY` | OpenAI API key for LLM access  |
| `PORT`           | Port to run the FastAPI server |
| `HOST`           | Host to bind the server to     |

---

## 🔐 CORS

CORS is enabled globally to allow the frontend to communicate with this API.

Configured in `main.py`:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update to restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## ✅ .gitignore

Ensure your `.gitignore` includes:

```gitignore
.env
venv/
__pycache__/
```

---

## 🛠 Dev Tips

* This API can be run on any port/host thanks to `.env` support.
* You can use `curl`, Postman, or your `tracker.js` to test locally.
* The LLM call is synchronous for simplicity; feel free to convert to `async` if needed.

---
