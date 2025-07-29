from fastapi import APIRouter, HTTPException
from typing import List, Optional
from data_manager.data_loader import DataLoader
from data_manager.data_saver import DataSaver
from entities.professeur import Professeur
from entities.etudiant import Etudiant
from entities.cours import Cours
from entities.note import Note

router = APIRouter()
data_loader = DataLoader("data/")
data_saver = DataSaver("data/")

# Professeurs routes
@router.get("/professeurs", response_model=List[dict])
def get_professeurs():
    """Récupère tous les professeurs"""
    professeurs = data_loader.load_professeurs()
    return [p.to_dict() for p in professeurs]

@router.get("/professeurs/{prof_id}")
def get_professeur(prof_id: int):
    """Récupère un professeur par ID"""
    prof = data_loader.get_professeur_by_id(prof_id)
    if not prof:
        raise HTTPException(status_code=404, detail="Professeur non trouvé")
    return prof.to_dict()

@router.post("/professeurs")
def create_professeur(nom: str, email: str, specialite: str):
    """Crée un nouveau professeur"""
    prof = Professeur(nom=nom, email=email, specialite=specialite)
    saved_prof = data_saver.save_professeur(prof)
    return {"message": "Professeur créé", "id": saved_prof.id, "data": saved_prof.to_dict()}

@router.put("/professeurs/{prof_id}")
def update_professeur(prof_id: int, nom: Optional[str] = None, email: Optional[str] = None, specialite: Optional[str] = None):
    """Met à jour un professeur"""
    prof = data_loader.get_professeur_by_id(prof_id)
    if not prof:
        raise HTTPException(status_code=404, detail="Professeur non trouvé")
    
    if nom: prof.nom = nom
    if email: prof.email = email
    if specialite: prof.specialite = specialite
    
    saved_prof = data_saver.save_professeur(prof)
    return {"message": "Professeur mis à jour", "data": saved_prof.to_dict()}

@router.delete("/professeurs/{prof_id}")
def delete_professeur(prof_id: int):
    """Supprime un professeur"""
    success = data_saver.delete_professeur(prof_id)
    if not success:
        raise HTTPException(status_code=404, detail="Professeur non trouvé")
    return {"message": "Professeur supprimé"}

# Étudiants routes
@router.get("/etudiants", response_model=List[dict])
def get_etudiants():
    """Récupère tous les étudiants"""
    etudiants = data_loader.load_etudiants()
    return [e.to_dict() for e in etudiants]

@router.get("/etudiants/{etudiant_id}")
def get_etudiant(etudiant_id: int):
    """Récupère un étudiant par ID"""
    etudiant = data_loader.get_etudiant_by_id(etudiant_id)
    if not etudiant:
        raise HTTPException(status_code=404, detail="Étudiant non trouvé")
    return etudiant.to_dict()

@router.post("/etudiants")
def create_etudiant(nom: str, email: str, numero_etudiant: str, date_naissance: str):
    """Crée un nouvel étudiant"""
    etudiant = Etudiant(nom=nom, email=email, numero_etudiant=numero_etudiant, date_naissance=date_naissance)
    saved_etudiant = data_saver.save_etudiant(etudiant)
    return {"message": "Étudiant créé", "id": saved_etudiant.id, "data": saved_etudiant.to_dict()}

@router.put("/etudiants/{etudiant_id}")
def update_etudiant(etudiant_id: int, nom: Optional[str] = None, email: Optional[str] = None, numero_etudiant: Optional[str] = None):
    """Met à jour un étudiant"""
    etudiant = data_loader.get_etudiant_by_id(etudiant_id)
    if not etudiant:
        raise HTTPException(status_code=404, detail="Étudiant non trouvé")
    
    if nom: etudiant.nom = nom
    if email: etudiant.email = email
    if numero_etudiant: etudiant.numero_etudiant = numero_etudiant
    
    saved_etudiant = data_saver.save_etudiant(etudiant)
    return {"message": "Étudiant mis à jour", "data": saved_etudiant.to_dict()}

@router.delete("/etudiants/{etudiant_id}")
def delete_etudiant(etudiant_id: int):
    """Supprime un étudiant"""
    success = data_saver.delete_etudiant(etudiant_id)
    if not success:
        raise HTTPException(status_code=404, detail="Étudiant non trouvé")
    return {"message": "Étudiant supprimé"}

# Cours routes
@router.get("/cours", response_model=List[dict])
def get_cours():
    """Récupère tous les cours"""
    cours = data_loader.load_cours()
    return [c.to_dict() for c in cours]

@router.get("/cours/{cours_id}")
def get_cours_by_id(cours_id: int):
    """Récupère un cours par ID"""
    cours = data_loader.get_cours_by_id(cours_id)
    if not cours:
        raise HTTPException(status_code=404, detail="Cours non trouvé")
    return cours.to_dict()

@router.post("/cours")
def create_cours(nom: str, code: str, description: str, credits: int, professeur_id: Optional[int] = None):
    """Crée un nouveau cours"""
    cours = Cours(nom=nom, code=code, description=description, credits=credits, professeur_id=professeur_id)
    saved_cours = data_saver.save_cours(cours)
    return {"message": "Cours créé", "id": saved_cours.id, "data": saved_cours.to_dict()}

@router.put("/cours/{cours_id}")
def update_cours(cours_id: int, nom: Optional[str] = None, code: Optional[str] = None, description: Optional[str] = None, credits: Optional[int] = None, professeur_id: Optional[int] = None):
    """Met à jour un cours"""
    cours = data_loader.get_cours_by_id(cours_id)
    if not cours:
        raise HTTPException(status_code=404, detail="Cours non trouvé")
    
    if nom: cours.nom = nom
    if code: cours.code = code
    if description: cours.description = description
    if credits: cours.credits = credits
    if professeur_id is not None: cours.professeur_id = professeur_id
    
    saved_cours = data_saver.save_cours(cours)
    return {"message": "Cours mis à jour", "data": saved_cours.to_dict()}

@router.delete("/cours/{cours_id}")
def delete_cours(cours_id: int):
    """Supprime un cours"""
    success = data_saver.delete_cours(cours_id)
    if not success:
        raise HTTPException(status_code=404, detail="Cours non trouvé")
    return {"message": "Cours supprimé"}

# Notes routes
@router.get("/notes", response_model=List[dict])
def get_notes():
    """Récupère toutes les notes"""
    notes = data_loader.load_notes()
    return [n.to_dict() for n in notes]

@router.post("/notes")
def create_note(etudiant_id: int, evaluation_id: int, valeur: float, commentaire: Optional[str] = None):
    """Crée une nouvelle note"""
    note = Note(etudiant_id=etudiant_id, evaluation_id=evaluation_id, valeur=valeur, commentaire=commentaire)
    saved_note = data_saver.save_note(note)
    return {"message": "Note créée", "id": saved_note.id, "data": saved_note.to_dict()}