from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Cours:
    id: int
    nom: str
    code: str
    description: str
    credits: int
    date_creation: Optional[str] = None
    
    def __post_init__(self):
        if self.date_creation is None:
            self.date_creation = datetime.now().isoformat()
    
    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "code": self.code,
            "description": self.description,
            "credits": self.credits,
            "date_creation": self.date_creation
        }