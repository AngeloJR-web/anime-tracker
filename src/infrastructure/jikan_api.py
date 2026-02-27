# src/infrastructure/jikan_api.py
import aiohttp
from src.domain.media import AnimeItem

class JikanAPIClient:
    """Cliente assíncrono para a API oficial do MyAnimeList (Jikan)."""
    BASE_URL = "https://api.jikan.moe/v4"

    async def search_anime(self, title: str) -> AnimeItem | None:
        async with aiohttp.ClientSession() as session:
            url = f"{self.BASE_URL}/anime"
            params = {"q": title, "limit": 1}
            
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    if not data.get("data"):
                        return None
                    
                    anime_data = data["data"][0]
                    img_url = anime_data.get("images", {}).get("jpg", {}).get("large_image_url")
                    sinopse = anime_data.get("synopsis", "Sinopse não disponível.")
                    return AnimeItem(
                        mal_id=anime_data["mal_id"],
                        title=anime_data["title"],
                        total_episodes=anime_data.get("episodes") or 0, 
                        image_url=img_url,
                        synopsis=sinopse
                    )
                response.raise_for_status()