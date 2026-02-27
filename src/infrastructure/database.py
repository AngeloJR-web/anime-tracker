# src/infrastructure/database.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Cria um arquivo chamado 'otakutracker.db' na raiz do projeto
SQLALCHEMY_DATABASE_URL = "sqlite:///./otakutracker.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Esta é a nossa Tabela no Banco de Dados
class AnimeDB(Base):
    __tablename__ = "animes"

    mal_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    total_episodes = Column(Integer)
    progress = Column(Integer, default=0)
    status = Column(String, default="PLAN_TO_WATCH")
    image_url = Column(String)
    synopsis = Column(String)

# Cria as tabelas no banco de dados se não existirem
Base.metadata.create_all(bind=engine)