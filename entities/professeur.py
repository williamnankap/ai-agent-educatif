from datetime import datetime


class Professeur:
    """Classe représentant un professeur dans le système éducatif"""
    
    def __init__(self, nom: str, email: str, specialite: str, id: int = None, date_creation: str = None):
        self.id = id
        self._nom = nom  # Attribut privé avec validation
        self.email = email
        self._specialite = specialite  # Attribut privé avec validation
        self.date_creation = date_creation or datetime.now().isoformat()
        self.cours = []  # Liste des cours enseignés
    
    @property
    def nom(self) -> str:
        """Nom complet du professeur avec validation"""
        return self._nom
    
    @nom.setter
    def nom(self, value: str):
        if not value or not value.strip():
            raise ValueError("Le nom ne peut pas être vide")
        self._nom = value.strip()
    
    @property
    def specialite(self) -> str:
        """Spécialité d'enseignement du professeur avec validation"""
        return self._specialite
    
    @specialite.setter
    def specialite(self, value: str):
        if not value or not value.strip():
            raise ValueError("La spécialité ne peut pas être vide")
        self._specialite = value.strip()
    
    def ajouter_cours(self, cours_id: int):
        """Ajoute un cours à la liste des cours enseignés"""
        if cours_id not in self.cours:
            self.cours.append(cours_id)
    
    def retirer_cours(self, cours_id: int):
        """Retire un cours de la liste des cours enseignés"""
        if cours_id in self.cours:
            self.cours.remove(cours_id)
    
    def to_dict(self) -> dict:
        """Convertit l'objet en dictionnaire pour la sérialisation JSON"""
        return {
            "id": self.id,
            "nom": self._nom,
            "email": self.email,
            "specialite": self._specialite,
            "date_creation": self.date_creation,
            "cours": self.cours
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """Crée un objet Professeur à partir d'un dictionnaire"""
        prof = cls(
            nom=data.get("nom", ""),
            email=data.get("email", ""),
            specialite=data.get("specialite", ""),
            id=data.get("id"),
            date_creation=data.get("date_creation")
        )
        prof.cours = data.get("cours", [])
        return prof
    
    def __str__(self) -> str:
        return f"Prof. {self._nom} ({self._specialite})"
    
    def __repr__(self) -> str:
        return f"Professeur(id={self.id}, nom='{self._nom}', specialite='{self._specialite}')"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Professeur):
            return False
        return self.id == other.id and self.id is not None