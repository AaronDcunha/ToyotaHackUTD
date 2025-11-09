## 🚗 ToyotaHackUTD — AI-Powered Toyota Car Finder
---

## 🌟 Inspiration
---

Artificial Intelligence is revolutionizing how we interact with information. This is much like how Google transformed the way we access information. We wanted to bring that same innovation to the car-buying experience. Purchasing a car is a major decision, and our goal was to make it practical, smarter, and more personalized utilizing AI technology.

## 💡 What It Does
---


ToyotaHackUTD offers users a way to explore Toyota’s car lineup in two intuitive ways:

🔍 Filter Search: Manually filter cars by particular qualities such as price, model, fuel type, and more.

💬 AI-Powered Search: Describe your dream car in a short sentence. AI will recommend matching Toyota models that are most suitable for your preferences.

##  🛠️ How We Built It
---

We combined the power of Google’s Gemini API with a well formatted Toyota CSV dataset including a detailed specification for a large range of Toyota vehicles.

Our stack included:

Frontend: Built using modern web technologies to make sure it is clean and responsive UI.

Backend: Integrated Gemini AI with the Toyota dataset for the purpose: intelligent query processing.

Data Handling: CSV parsing and data matching algorithms to productively filter and rank car options.

## ⚙️ Challenges We Faced
---

🎨 Designing an organized and visually enticing color scheme for the front end.

🧩 Integrating the AI logic with the front end. This allows for seamless communication between the Gemini API and the UI components.


## 🏆 Accomplishments We’re Proud Of
---

Built a fully functional AI-powered web app from scratch in a restricted time frame.

Designed a user-friendly interface that feels intuitive and modern.

Developed a project that can genuinely improve the car-buying process and support people in making enhanced decisions.


## 📚 What We Learned
---

How to efficiently integrate Gemini API with structured data sources like CSV files.

The essence of team collaboration, version control, and UI/UX design in building a complete application.

Balancing AI complexity with usability to create a seamless user experience.

## 🚀 What’s Next for Toyota AI Search

⚡Performance Optimization: Enhace the search algorithm to handle hugedatasets effectively.

🧠 Smarter AI Queries: Improve natural language understanding for more nuanced and personalized car recommendations.

📱 Mobile Optimization: Build a mobile-friendly or app version for on-the-go users.

🌐 Expanded Dataset: Incoperate more Toyota models and integrate real-time data such as availability or pricing.

## 🤝 Acknowledgments
---

Special thanks to Toyota for sponsoring the hackathon and to HackUTD for hosting an aspiring event that motivates innovation and collaboration.



## Frontend Setup (React + Vite)
---

Go to the frontend folder
```
cd frontend
```

Install dependencies
```
npm install
```

Run the development server
```
npm run dev
```

Open the app at
http://localhost:5173



## Backend Setup (FastAPI)
---

Go to the backend folder
cd backend

Create and activate a virtual environment
```
python -m venv venv
venv\Scripts\activate # Windows
source venv/bin/activate # macOS/Linux
```

Install dependencies
```
pip install -r requirements.txt
```

Add your Gemini API key to the ai_query.py file

Run the backend server
```
uvicorn main:app --reload --port 8000
```

Backend will be live at
http://127.0.0.1:8000



## Connecting Frontend & Backend
---

Make sure both servers are running:

Frontend → http://localhost:5173

Backend → http://127.0.0.1:8000

Frontend fetches data from:
/result/ai
/result/manual

