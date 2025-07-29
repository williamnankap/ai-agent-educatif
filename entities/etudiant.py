from datetime import datetime
import re


class Etudiant:
    """Classe représentant un étudiant dans le système éducatif"""
    
    def __init__(self, nom: str, email: str, numero_etudiant: str, 
                 date_naissance: str = None, id: int = None, date_creation: str = None):
        self.id = id
        self.nom = nom
        self._email = email  # Attribut privé avec validation
        self._numero_etudiant = numero_etudiant  # Attribut privé avec validation
        self.date_naissance = date_naissance
        self.date_creation = date_creation or datetime.now().isoformat()
        self.cours_inscrits = []  # Liste des cours auxquels l'étudiant est inscrit
        self.notes = []  # Liste des notes obtenues
    
    @property
    def email(self) -> str:
        """Adresse email avec validation"""
        return self._email
    
    @email.setter
    def email(self, value: str):
        if not value or "@" not in value:
            raise ValueError("L'email doit contenir un @")
        self._email = value.lower().strip()
    
    @property
    def numero_etudiant(self) -> str:
        """Numéro unique d'étudiant avec validation (ex: E2024001)"""
        return self._numero_etudiant
    
    @numero_etudiant.setter
    def numero_etudiant(self, value: str):
        if not value or not value.strip():
            raise ValueError("Le numéro étudiant ne peut pas être vide")
        # Validation du format (ex: E2024001)
        if not re.match(r'^E\d{7}$', value.strip()):
            raise ValueError("Le numéro étudiant doit avoir le format E suivi de 7 chiffres")
        self._numero_etudiant = value.strip().upper()
    
    @property
    def age(self) -> int:
        """Calcule l'âge de l'étudiant à partir de sa date de naissance"""
        if not self.date_naissance:
            return None
        
        today = datetime.now().date()
        birth_date = datetime.fromisoformat(self.date_naissance).date()
        age = today.year - birth_date.year
        
        # Ajustement si l'anniversaire n'est pas encore passé cette année
        if today < birth_date.replace(year=today.year):
            age -= 1
        
        return age
    
    def inscrire_cours(self, cours_id: int):
        """Inscrit l'étudiant à un cours"""
        if cours_id not in self.cours_inscrits:
            self.cours_inscrits.append(cours_id)
    
    def desinscrire_cours(self, cours_id: int):
        """Désinscrit l'étudiant d'un cours"""
        if cours_id in self.cours_inscrits:
            self.cours_inscrits.remove(cours_id)
    
    def ajouter_note(self, note_id: int):
        """Ajoute une note à l'historique de l'étudiant"""
        if note_id not in self.notes:
            self.notes.append(note_id)
    
    def calculer_moyenne(self, notes_details: list = None) -> float:
        """Calcule la moyenne générale de l'étudiant"""
        if not notes_details:
            return 0.0
        
        total = sum(note.get('valeur', 0) for note in notes_details if note.get('etudiant_id') == self.id)
        count = len([note for note in notes_details if note.get('etudiant_id') == self.id])
        
        return round(total / count, 2) if count > 0 else 0.0
    
    def to_dict(self) -> dict:
        """Convertit l'objet en dictionnaire pour la sérialisation JSON"""
        return {
            "id": self.id,
            "nom": self.nom,
            "email": self._email,
            "numero_etudiant": self._numero_etudiant,
            "date_naissance": self.date_naissance,
            "date_creation": self.date_creation,
            "cours_inscrits": self.cours_inscrits,
            "notes": self.notes
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """Crée un objet Etudiant à partir d'un dictionnaire"""
        etudiant = cls(
            nom=data.get("nom", ""),
            email=data.get("email", ""),
            numero_etudiant=data.get("numero_etudiant", ""),
            date_naissance=data.get("date_naissance"),
            id=data.get("id"),
            date_creation=data.get("date_creation")
        )
        etudiant.cours_inscrits = data.get("cours_inscrits", [])
        etudiant.notes = data.get("notes", [])
        return etudiant
    
    def __str__(self) -> str:
        return f"Étudiant {self.nom} ({self._numero_etudiant})"
    
    def __repr__(self) -> str:
        return f"Etudiant(id={self.id}, nom='{self.nom}', numero='{self._numero_etudiant}')"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Etudiant):
            return False
        return self.id == other.id and self.id is not None