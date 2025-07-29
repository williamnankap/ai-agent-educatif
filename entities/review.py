from datetime import datetime


class Review:
    """Classe représentant l'évaluation d'un cours par un étudiant"""
    
    def __init__(self, etudiant_id: int, cours_id: int, note: int, 
                 commentaire: str = "", id: int = None, date_creation: str = None):
        self.id = id
        self.etudiant_id = etudiant_id
        self.cours_id = cours_id
        self._note = note  # Attribut privé avec validation
        self._commentaire = commentaire  # Attribut privé avec validation
        self.date_creation = date_creation or datetime.now().isoformat()
    
    @property
    def note(self) -> int:
        """Note donnée au cours (1-5 étoiles) avec validation"""
        return self._note
    
    @note.setter
    def note(self, value: int):
        if not isinstance(value, int):
            raise ValueError("La note doit être un entier")
        if value < 1:
            raise ValueError("La note ne peut pas être inférieure à 1")
        if value > 5:
            raise ValueError("La note ne peut pas dépasser 5")
        self._note = value
    
    @property
    def commentaire(self) -> str:
        """Commentaire de l'étudiant avec validation"""
        return self._commentaire
    
    @commentaire.setter
    def commentaire(self, value: str):
        if len(value) > 1000:
            raise ValueError("Le commentaire ne peut pas dépasser 1000 caractères")
        self._commentaire = value.strip()
    
    @property
    def appreciation(self) -> str:
        """Retourne une appréciation basée sur la note"""
        appreciations = {
            1: "Très insatisfait",
            2: "Insatisfait", 
            3: "Neutre",
            4: "Satisfait",
            5: "Très satisfait"
        }
        return appreciations.get(self._note, "Non évalué")
    
    @property
    def etoiles(self) -> str:
        """Représentation visuelle en étoiles"""
        return "⭐" * self._note + "☆" * (5 - self._note)
    
    def est_positive(self) -> bool:
        """Vérifie si la review est positive (>= 4 étoiles)"""
        return self._note >= 4
    
    def to_dict(self) -> dict:
        """Convertit l'objet en dictionnaire pour la sérialisation JSON"""
        return {
            "id": self.id,
            "etudiant_id": self.etudiant_id,
            "cours_id": self.cours_id,
            "note": self._note,
            "commentaire": self._commentaire,
            "date_creation": self.date_creation
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """Crée un objet Review à partir d'un dictionnaire"""
        return cls(
            etudiant_id=data.get("etudiant_id", 1),
            cours_id=data.get("cours_id", 1),
            note=data.get("note", 3),
            commentaire=data.get("commentaire", ""),
            id=data.get("id"),
            date_creation=data.get("date_creation")
        )
    
    def __str__(self) -> str:
        return f"Review {self.etoiles} - {self.appreciation}"
    
    def __repr__(self) -> str:
        return f"Review(id={self.id}, note={self._note}, cours_id={self.cours_id})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Review):
            return False
        return self.id == other.id and self.id is not None
    
    def __lt__(self, other) -> bool:
        """Permet la comparaison des reviews"""
        if not isinstance(other, Review):
            return NotImplemented
        return self._note < other._note