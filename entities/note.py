from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Note:
    id: int
    etudiant_id: int
    evaluation_id: int
    valeur: float
    commentaire: str
    date_creation: Optional[str] = None
    
    def __post_init__(self):
        if self.date_creation is None:
            self.date_creation = datetime.now().isoformat()
    
    def to_dict(self):
        return {
            "id": self.id,
            "etudiant_id": self.etudiant_id,
            "evaluation_id": self.evaluation_id,
            "valeur": self.valeur,
            "commentaire": self.commentaire,
            "date_creation": self.date_creation
        }