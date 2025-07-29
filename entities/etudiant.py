from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass 
class Etudiant:
    id: int
    nom: str
    email: str
    numero_etudiant: str
    date_naissance: str
    date_creation: Optional[str] = None
    
    def __post_init__(self):
        if self.date_creation is None:
            self.date_creation = datetime.now().isoformat()
    
    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "email": self.email,
            "numero_etudiant": self.numero_etudiant,
            "date_naissance": self.date_naissance,
            "date_creation": self.date_creation
        }