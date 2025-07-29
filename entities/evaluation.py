from datetime import datetime


class Evaluation:
    """Classe représentant une évaluation dans un cours"""
    
    def __init__(self, nom: str, cours_id: int, type: str, coefficient: float,
                 id: int = None, date_creation: str = None):
        self.id = id
        self._nom = nom  # Attribut privé avec validation
        self.cours_id = cours_id
        self.type = type
        self._coefficient = coefficient  # Attribut privé avec validation
        self.date_creation = date_creation or datetime.now().isoformat()
        self.notes = []  # Liste des notes pour cette évaluation
    
    @property
    def nom(self) -> str:
        """Nom de l'évaluation avec validation"""
        return self._nom
    
    @nom.setter
    def nom(self, value: str):
        if not value or not value.strip():
            raise ValueError("Le nom de l'évaluation ne peut pas être vide")
        self._nom = value.strip()
    
    @property
    def coefficient(self) -> float:
        """Coefficient de l'évaluation avec validation"""
        return self._coefficient
    
    @coefficient.setter
    def coefficient(self, value: float):
        if value <= 0:
            raise ValueError("Le coefficient doit être positif")
        if value > 10:
            raise ValueError("Le coefficient ne peut pas dépasser 10")
        self._coefficient = float(value)
    
    def ajouter_note(self, note_id: int):
        """Ajoute une note à cette évaluation"""
        if note_id not in self.notes:
            self.notes.append(note_id)
    
    def calculer_moyenne(self, notes_details: list = None) -> float:
        """Calcule la moyenne pour cette évaluation"""
        if not notes_details:
            return 0.0
        
        notes_evaluation = [note.get('valeur', 0) for note in notes_details 
                           if note.get('evaluation_id') == self.id]
        
        return round(sum(notes_evaluation) / len(notes_evaluation), 2) if notes_evaluation else 0.0
    
    def to_dict(self) -> dict:
        """Convertit l'objet en dictionnaire pour la sérialisation JSON"""
        return {
            "id": self.id,
            "nom": self._nom,
            "cours_id": self.cours_id,
            "type": self.type,
            "coefficient": self._coefficient,
            "date_creation": self.date_creation,
            "notes": self.notes
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """Crée un objet Evaluation à partir d'un dictionnaire"""
        evaluation = cls(
            nom=data.get("nom", ""),
            cours_id=data.get("cours_id", 1),
            type=data.get("type", "controle"),
            coefficient=data.get("coefficient", 1.0),
            id=data.get("id"),
            date_creation=data.get("date_creation")
        )
        evaluation.notes = data.get("notes", [])
        return evaluation
    
    def __str__(self) -> str:
        return f"Évaluation {self._nom} (coeff: {self._coefficient})"
    
    def __repr__(self) -> str:
        return f"Evaluation(id={self.id}, nom='{self._nom}', coefficient={self._coefficient})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Evaluation):
            return False
        return self.id == other.id and self.id is not None