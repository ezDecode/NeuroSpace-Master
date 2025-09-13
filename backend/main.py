import os
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from auth import verify_clerk_jwt


APP_ENV = os.getenv("APP_ENV", "development")
FRONTEND_ORIGIN = os.getenv("FRONTEND_ORIGIN", "http://localhost:3000")

app = FastAPI(title="NeuroSpace API", version="2.0.0")

allowed_origins = [FRONTEND_ORIGIN] if FRONTEND_ORIGIN else ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "env": APP_ENV}


@app.get("/me")
async def me(claims: dict = Depends(verify_clerk_jwt)) -> dict:
    return {"claims": claims}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", "8000")),
        reload=APP_ENV != "production",
    )

