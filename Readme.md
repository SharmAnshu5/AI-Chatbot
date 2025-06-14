# 🧠 AI Chatbot (Full Stack)

A modern, full-stack AI-powered chatbot using Flask (backend) and React (frontend), featuring JWT authentication, OpenAI integration, NLTK-based NLP, and a futuristic UI with neon-themed UX design.

---

## 🚀 Features

- JWT-based user authentication
- NLTK-powered text preprocessing
- OpenAI GPT-3 API integration
- JSON-based session chat history
- Modular Flask backend
- Futuristic React frontend (Tailwind CSS, neon UI)
- Wavy animated dark background
- Sidebar and role prompt templates

---

## 📦 Project Structure

```
chatbot/
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── .env
│   ├── requirements.txt
│   ├── routes/
│   │   ├── auth_routes.py
│   │   └── chat_routes.py
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── chat_service.py
│   │   └── logging_service.py
│   ├── database/
│   │   └── storage.py
│   └── chat_history.json
│
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── index.js
│   │   ├── index.css
│   │   ├── App.jsx
│   │   ├── components/
│   │   │   ├── Header.jsx
│   │   │   ├── Sidebar.jsx
│   │   │   ├── RightPanel.jsx
│   │   │   ├── Chatbox.jsx
│   │   │   ├── Footer.jsx
│   │   │   └── WavyLine.jsx
```

---

## ⚙️ Backend Setup

### 1. Navigate to the backend directory:
```bash
cd chatbot/backend
```

### 2. Create `.env` file:
```env
SECRET_KEY=your-secret-key
OPENAI_API_KEY=your-openai-api-key
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Run the Flask app:
```bash
python app.py
```

---

## 🧠 Frontend Setup

### 1. Navigate to the frontend:
```bash
cd chatbot/frontend
```

### 2. Install frontend dependencies:
```bash
npm install
```

### 3. Run React app:
```bash
npm start
```

The app will start at `http://localhost:3000`

Ensure your backend is running on `http://localhost:5000`

---

## 🔁 API Routes

### `POST /auth/login`
Returns a JWT token for the session.

### `POST /chat`
Body:
```json
{
  "session_id": "abc123",
  "message": "Hello"
}
```

### `GET /history/:session_id`
Returns previous chat logs.

---

## 🎨 Frontend Highlights

- **Wavy animated background** using Tailwind CSS and custom CSS
- **Gradient glowing buttons** for new chat and send
- **Prompt templates** in the right panel
- **Saved conversations** module
- **Dark futuristic techy vibe** with Inter font

---

## 📝 License
MIT — use freely with attribution.

---

## 👨‍💻 Author
Built and designed by **Anshu Sharma** ✨

For contributions, feedback, or support, reach out or fork the project!
