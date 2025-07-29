from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Professeur:
    id: int
    nom: str
    email: str
    specialite: str
    date_creation: Optional[str] = None
    
    def __post_init__(self):
        if self.date_creation is None:
            self.date_creation = datetime.now().isoformat()
    
    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "email": self.email,
            "specialite": self.specialite,
            "date_creation": self.date_creation
        }