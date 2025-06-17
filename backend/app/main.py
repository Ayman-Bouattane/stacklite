from fastapi import FastAPI
from .pipeline import run_pipeline
from .model import train_model, predict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS so the React frontend (http://localhost:3000) can call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    global insights, _
    insights = run_pipeline()
    # Train the model (we only need the persisted model file here)
    _, _ = train_model()

@app.get("/insights")
async def get_insights():
    return insights

@app.get("/predict/{n_days}")
async def get_prediction(n_days: int):
    return predict(n_days)
