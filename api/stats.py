from fastapi import APIRouter
from data_manager.data_loader import DataLoader

router = APIRouter()
data_loader = DataLoader("data/")

@router.get("/stats")
def get_stats():
    """Récupère les statistiques du système"""
    try:
        professeurs = data_loader.load_professeurs()
        etudiants = data_loader.load_etudiants()
        cours = data_loader.load_cours()
        notes = data_loader.load_notes()
        
        stats = {
            "nb_professeurs": len(professeurs),
            "nb_etudiants": len(etudiants),
            "nb_cours": len(cours),
            "nb_notes": len(notes),
        }
        
        if notes:
            moyenne = sum(note.valeur for note in notes) / len(notes)
            stats["moyenne_generale"] = round(moyenne, 2)
        else:
            stats["moyenne_generale"] = 0
        
        return stats
    
    except Exception as e:
        return {"error": f"Erreur lors du calcul des statistiques: {str(e)}"}

@router.get("/health")
def health_check():
    """Vérification de l'état de santé de l'API"""
    return {"status": "ok", "message": "API éducative fonctionnelle"}