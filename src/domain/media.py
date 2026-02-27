# src/domain/media.py
from dataclasses import dataclass, field
from enum import Enum, auto
from datetime import datetime
from typing import Optional

class ContentStatus(Enum):
    WATCHING = auto()
    COMPLETED = auto()
    PLAN_TO_WATCH = auto()

@dataclass
class AnimeItem:
    mal_id: int
    title: str
    total_episodes: int
    progress: int = 0
    status: ContentStatus = ContentStatus.PLAN_TO_WATCH
    score: Optional[float] = None
    image_url: Optional[str] = None
    synopsis: Optional[str] = None
    last_updated: datetime = field(default_factory=datetime.now)

    def watch_episode(self, count: int = 1):
        """Atualiza o progresso e o status automaticamente."""
        if self.progress + count > self.total_episodes and self.total_episodes != 0:
            raise ValueError("Progresso excede o total de episódios.")
        
        self.progress += count
        self.last_updated = datetime.now()
        
        if self.total_episodes > 0 and self.progress == self.total_episodes:
            self.status = ContentStatus.COMPLETED
        elif self.progress > 0 and self.status == ContentStatus.PLAN_TO_WATCH:
            self.status = ContentStatus.WATCHING