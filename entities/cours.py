from datetime import datetime


class Cours:
    """Classe représentant un cours dans le système éducatif"""
    
    def __init__(self, nom: str, code: str, description: str, credits: int,
                 professeur_id: int = None, id: int = None, date_creation: str = None):
        self.id = id
        self._nom = nom  # Attribut privé avec validation
        self._code = code  # Attribut privé avec validation
        self.description = description
        self.credits = credits
        self.professeur_id = professeur_id
        self.date_creation = date_creation or datetime.now().isoformat()
        self.etudiants_inscrits = []  # Liste des étudiants inscrits
        self.evaluations = []  # Liste des évaluations du cours
    
    @property
    def nom(self) -> str:
        """Nom du cours avec validation"""
        return self._nom
    
    @nom.setter
    def nom(self, value: str):
        if not value or not value.strip():
            raise ValueError("Le nom du cours ne peut pas être vide")
        self._nom = value.strip()
    
    @property
    def code(self) -> str:
        """Code du cours avec validation (ex: PY001)"""
        return self._code
    
    @code.setter
    def code(self, value: str):
        if not value or not value.strip():
            raise ValueError("Le code du cours ne peut pas être vide")
        self._code = value.strip().upper()
    
    def ajouter_etudiant(self, etudiant_id: int):
        """Inscrit un étudiant au cours"""
        if etudiant_id not in self.etudiants_inscrits:
            self.etudiants_inscrits.append(etudiant_id)
    
    def retirer_etudiant(self, etudiant_id: int):
        """Désinscrit un étudiant du cours"""
        if etudiant_id in self.etudiants_inscrits:
            self.etudiants_inscrits.remove(etudiant_id)
    
    def ajouter_evaluation(self, evaluation_id: int):
        """Ajoute une évaluation au cours"""
        if evaluation_id not in self.evaluations:
            self.evaluations.append(evaluation_id)
    
    def to_dict(self) -> dict:
        """Convertit l'objet en dictionnaire pour la sérialisation JSON"""
        return {
            "id": self.id,
            "nom": self._nom,
            "code": self._code,
            "description": self.description,
            "credits": self.credits,
            "professeur_id": self.professeur_id,
            "date_creation": self.date_creation,
            "etudiants_inscrits": self.etudiants_inscrits,
            "evaluations": self.evaluations
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """Crée un objet Cours à partir d'un dictionnaire"""
        cours = cls(
            nom=data.get("nom", ""),
            code=data.get("code", ""),
            description=data.get("description", ""),
            credits=data.get("credits", 3),
            professeur_id=data.get("professeur_id"),
            id=data.get("id"),
            date_creation=data.get("date_creation")
        )
        cours.etudiants_inscrits = data.get("etudiants_inscrits", [])
        cours.evaluations = data.get("evaluations", [])
        return cours
    
    def __str__(self) -> str:
        return f"Cours {self._nom} ({self._code}) - {self.credits} crédits"
    
    def __repr__(self) -> str:
        return f"Cours(id={self.id}, nom='{self._nom}', code='{self._code}')"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Cours):
            return False
        return self.id == other.id and self.id is not None