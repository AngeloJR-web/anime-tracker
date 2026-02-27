# tests/test_media.py
import pytest
from src.domain.media import AnimeItem, ContentStatus

def test_watch_episode_updates_progress_and_status():
    """Garante que assistir a um episódio atualiza o progresso e muda o status para WATCHING."""
    # Arrange (Preparação)
    anime = AnimeItem(mal_id=1, title="Anime de Teste", total_episodes=12)
    
    # Act (Ação)
    anime.watch_episode(1)
    
    # Assert (Verificação)
    assert anime.progress == 1
    assert anime.status == ContentStatus.WATCHING

def test_watch_episode_completes_anime():
    """Garante que ao atingir o limite de episódios, o status muda para COMPLETED."""
    anime = AnimeItem(mal_id=2, title="Anime Curto", total_episodes=3)
    
    anime.watch_episode(3)
    
    assert anime.progress == 3
    assert anime.status == ContentStatus.COMPLETED

def test_cannot_watch_more_episodes_than_total():
    """Garante que o sistema bloqueia o usuário de assistir além do limite."""
    anime = AnimeItem(mal_id=3, title="Anime Fechado", total_episodes=12)
    anime.watch_episode(12) # Assiste tudo
    
    # Verifica se o Python levanta um ValueError ao tentar o episódio 13
    with pytest.raises(ValueError, match="Progresso excede o total de episódios."):
        anime.watch_episode(1)