from fastapi import FastAPI
from .routes import router as routes_router
from .stats import router as stats_router

app = FastAPI(
    title="Educational System API", 
    version="1.0.0",
    description="API pour gérer le système éducatif avec professeurs, étudiants, cours et notes"
)

# Inclure les routes
app.include_router(routes_router, tags=["CRUD Operations"])
app.include_router(stats_router, tags=["Statistics"])

@app.get("/")
def root():
    """Page d'accueil de l'API"""
    return {
        "message": "API Éducative - Système de gestion éducationnel",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)