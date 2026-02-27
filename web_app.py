# web_app.py
from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from src.infrastructure.jikan_api import JikanAPIClient
from src.infrastructure.database import SessionLocal, AnimeDB
import uvicorn

app = FastAPI(title="OtakuTracker Web API")
templates = Jinja2Templates(directory="templates")
api_client = JikanAPIClient()

# Dependência para abrir e fechar a conexão com o banco a cada requisição
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/search")
async def search_anime_api(q: str):
    anime = await api_client.search_anime(q)
    if not anime:
        raise HTTPException(status_code=404, detail="Anime não encontrado.")
    
    return {
        "mal_id": anime.mal_id,
        "title": anime.title,
        "total_episodes": anime.total_episodes,
        "image_url": anime.image_url,
        "synopsis": anime.synopsis
    }

# Nova rota para adicionar o anime na biblioteca (salvar no banco)
@app.post("/api/add")
async def add_to_library(data: dict, db: Session = Depends(get_db)):
    db_anime = db.query(AnimeDB).filter(AnimeDB.mal_id == data["mal_id"]).first()
    if db_anime:
        return {"message": "Anime já está na biblioteca."}
    
    novo_anime = AnimeDB(
        mal_id=data["mal_id"],
        title=data["title"],
        total_episodes=data["total_episodes"],
        image_url=data["image_url"],
        synopsis=data["synopsis"],
        progress=0,
        status="PLAN_TO_WATCH"
    )
    db.add(novo_anime)
    db.commit()
    return {"message": "Adicionado com sucesso!"}

# Rota para pegar todos os animes do banco
@app.get("/api/library")
async def get_library(db: Session = Depends(get_db)):
    animes = db.query(AnimeDB).all()
    return animes

@app.post("/api/watch/{mal_id}")
async def watch_episode_api(mal_id: int, db: Session = Depends(get_db)):
    db_anime = db.query(AnimeDB).filter(AnimeDB.mal_id == mal_id).first()
    if not db_anime:
        raise HTTPException(status_code=404, detail="Anime não está na biblioteca.")
    
    if db_anime.total_episodes > 0 and db_anime.progress >= db_anime.total_episodes:
        raise HTTPException(status_code=400, detail="Você já terminou este anime!")
        
    db_anime.progress += 1
    
    if db_anime.total_episodes > 0 and db_anime.progress == db_anime.total_episodes:
        db_anime.status = "COMPLETED"
    elif db_anime.progress > 0:
        db_anime.status = "WATCHING"
        
    db.commit()
    db.refresh(db_anime)
    
    return {"progress": db_anime.progress, "status": db_anime.status}

if __name__ == "__main__":
    uvicorn.run("web_app:app", host="127.0.0.1", port=8000, reload=True)