from datetime import datetime


class Note:
    """Classe représentant une note attribuée à un étudiant pour une évaluation"""
    
    def __init__(self, etudiant_id: int, evaluation_id: int, valeur: float, 
                 commentaire: str = "", id: int = None, date_creation: str = None):
        self.id = id
        self.etudiant_id = etudiant_id
        self.evaluation_id = evaluation_id
        self._valeur = valeur  # Attribut privé avec validation
        self.commentaire = commentaire
        self.date_creation = date_creation or datetime.now().isoformat()
    
    @property
    def valeur(self) -> float:
        """Valeur de la note avec validation (0-20)"""
        return self._valeur
    
    @valeur.setter
    def valeur(self, value: float):
        if value < 0:
            raise ValueError("La note ne peut pas être négative")
        if value > 20:
            raise ValueError("La note ne peut pas dépasser 20")
        self._valeur = float(value)
    
    @property
    def appreciation(self) -> str:
        """Retourne une appréciation basée sur la note"""
        if self._valeur >= 18:
            return "Excellent"
        elif self._valeur >= 16:
            return "Très bien"
        elif self._valeur >= 14:
            return "Bien"
        elif self._valeur >= 12:
            return "Assez bien"
        elif self._valeur >= 10:
            return "Passable"
        else:
            return "Insuffisant"
    
    def est_reussie(self) -> bool:
        """Vérifie si la note est suffisante (>= 10)"""
        return self._valeur >= 10
    
    def to_dict(self) -> dict:
        """Convertit l'objet en dictionnaire pour la sérialisation JSON"""
        return {
            "id": self.id,
            "etudiant_id": self.etudiant_id,
            "evaluation_id": self.evaluation_id,
            "valeur": self._valeur,
            "commentaire": self.commentaire,
            "date_creation": self.date_creation
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """Crée un objet Note à partir d'un dictionnaire"""
        return cls(
            etudiant_id=data.get("etudiant_id", 1),
            evaluation_id=data.get("evaluation_id", 1),
            valeur=data.get("valeur", 0.0),
            commentaire=data.get("commentaire", ""),
            id=data.get("id"),
            date_creation=data.get("date_creation")
        )
    
    def __str__(self) -> str:
        return f"Note {self._valeur}/20 ({self.appreciation})"
    
    def __repr__(self) -> str:
        return f"Note(id={self.id}, valeur={self._valeur}, etudiant_id={self.etudiant_id})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Note):
            return False
        return self.id == other.id and self.id is not None
    
    def __lt__(self, other) -> bool:
        """Permet la comparaison des notes"""
        if not isinstance(other, Note):
            return NotImplemented
        return self._valeur < other._valeur