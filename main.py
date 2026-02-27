# main.py
import asyncio
import sys
from src.infrastructure.jikan_api import JikanAPIClient

async def main():
    print("⛩️ Bem-vindo ao OtakuTracker Pro ⛩️\n")
    
    if len(sys.argv) < 2:
        print("Uso: python main.py <nome_do_anime>")
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    api_client = JikanAPIClient()

    print(f"🔍 Buscando metadados para: '{query}'...")
    
    try:
        anime = await api_client.search_anime(query)
        
        if anime:
            print("\n✅ Obra Encontrada!")
            print(f"Título: {anime.title}")
            print(f"ID MAL: {anime.mal_id}")
            print(f"Total de Episódios: {anime.total_episodes}")
            
            # Simulando uso do domínio
            print("\nSimulando: Assistindo 3 episódios...")
            anime.watch_episode(3)
            print(f"Progresso Atual: {anime.progress}/{anime.total_episodes}")
            print(f"Status Atual: {anime.status.name}")
        else:
            print("\n❌ Nenhuma obra encontrada com esse nome.")
            
    except Exception as e:
        print(f"\n⚠️ Erro ao comunicar com a API: {e}")

if __name__ == "__main__":
    # Garante a execução correta do event loop assíncrono
    asyncio.run(main())