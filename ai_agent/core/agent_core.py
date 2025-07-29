import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


class EducationalAgent:
    def __init__(self):
        from data_manager.data_loader import DataLoader
        from data_manager.data_saver import DataSaver
        from ..utils.action_processor import ActionProcessor
        
        self.data_loader = DataLoader("data/")
        self.data_saver = DataSaver("data/")
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.action_processor = ActionProcessor()
        
    def process_query(self, query: str) -> str:
        """Traite une requête utilisateur via OpenAI"""
        try:
            system_prompt = self._create_system_prompt()
            current_data = self._get_current_data()
            
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Données: {json.dumps(current_data, indent=2, ensure_ascii=False)}\n\nQuestion: {query}"}
                ],
                temperature=0.7,
                max_tokens=500
            )
            
            ai_response = response.choices[0].message.content
            final_response = self.action_processor.execute_actions(ai_response)
            
            return final_response
            
        except Exception as e:
            return f"Erreur: {str(e)}"
    
    def _create_system_prompt(self) -> str:
        """Prompt système simple"""
        return """Tu es un assistant IA éducatif.

IMPORTANT: Si l'utilisateur fournit directement un JSON de création, réponds UNIQUEMENT avec ce JSON exact, sans texte supplémentaire.

Pour créer des entités, utilise ces formats JSON exacts :

PROFESSEUR:
{"action": "create_professeur", "nom": "Jean Dupont", "specialite": "Mathématiques"}

ÉTUDIANT:  
{"action": "create_etudiant", "nom": "Marie Martin", "numero_etudiant": "E2024003"}

COURS:
{"action": "create_cours", "nom": "Python", "code": "PY001", "credits": 3, "professeur_id": 1}

ÉVALUATION:
{"action": "create_evaluation", "nom": "Examen Final", "cours_id": 1, "type": "examen", "coefficient": 2}

NOTE:
{"action": "create_note", "etudiant_id": 1, "evaluation_id": 1, "valeur": 15.5, "commentaire": "Bon travail"}

REVIEW:
{"action": "create_review", "etudiant_id": 1, "cours_id": 1, "note": 4, "commentaire": "Excellent cours"}

Pour consulter des données, utilise ces actions :
{"action": "get_etudiants"}
{"action": "get_professeurs"}
{"action": "get_cours"}
{"action": "get_notes"}
{"action": "get_stats"}
{"action": "get_reviews"}
{"action": "get_evaluations"}

Si l'utilisateur pose une question, réponds naturellement puis ajoute le JSON si nécessaire pour effectuer une action."""
    
    def _get_current_data(self) -> dict:
        """Récupère les données du système"""
        try:
            with open("data/professeurs.json", 'r') as f:
                professeurs = json.load(f)
            with open("data/etudiants.json", 'r') as f:  
                etudiants = json.load(f)
            with open("data/cours.json", 'r') as f:
                cours = json.load(f)
            with open("data/evaluations.json", 'r') as f:
                evaluations = json.load(f)
            with open("data/notes.json", 'r') as f:
                notes = json.load(f)
            with open("data/reviews.json", 'r') as f:
                reviews = json.load(f)
                
            return {
                "professeurs": professeurs,
                "etudiants": etudiants, 
                "cours": cours,
                "evaluations": evaluations,
                "notes": notes,
                "reviews": reviews,
                "stats": {
                    "nb_professeurs": len(professeurs),
                    "nb_etudiants": len(etudiants),
                    "nb_cours": len(cours),
                    "nb_evaluations": len(evaluations),
                    "nb_notes": len(notes),
                    "nb_reviews": len(reviews)
                }
            }
        except Exception:
            return {"erreur": "Impossible de charger les données"}