from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Evaluation:
    id: int
    nom: str
    cours_id: int
    type: str
    coefficient: float
    date_creation: Optional[str] = None
    
    def __post_init__(self):
        if self.date_creation is None:
            self.date_creation = datetime.now().isoformat()
    
    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "cours_id": self.cours_id,
            "type": self.type,
            "coefficient": self.coefficient,
            "date_creation": self.date_creation
        }