from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Review:
    id: int
    etudiant_id: int
    cours_id: int
    note: int
    commentaire: str
    date_creation: Optional[str] = None
    
    def __post_init__(self):
        if self.date_creation is None:
            self.date_creation = datetime.now().isoformat()
    
    def to_dict(self):
        return {
            "id": self.id,
            "etudiant_id": self.etudiant_id,
            "cours_id": self.cours_id,
            "note": self.note,
            "commentaire": self.commentaire,
            "date_creation": self.date_creation
        }