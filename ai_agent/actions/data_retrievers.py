import json


class DataRetrievers:
    """Classe pour gérer la récupération de données du système éducatif"""
    
    def get_etudiants(self, data: dict) -> str:
        """Récupère la liste des étudiants"""
        try:
            with open("data/etudiants.json", 'r') as f:
                etudiants = json.load(f)
            
            if not etudiants:
                return "📋 Aucun étudiant enregistré"
            
            result = "📋 **Liste des étudiants :**\n\n"
            for etudiant in etudiants:
                result += f"• **{etudiant.get('nom', 'N/A')}** (ID: {etudiant.get('id', 'N/A')})\n"
                result += f"  📧 {etudiant.get('email', 'N/A')}\n"
                result += f"  🎓 Numéro: {etudiant.get('numero_etudiant', 'N/A')}\n\n"
            
            return result
            
        except Exception as e:
            return f"❌ Erreur: {str(e)}"
    
    def get_professeurs(self, data: dict) -> str:
        """Récupère la liste des professeurs"""
        try:
            with open("data/professeurs.json", 'r') as f:
                professeurs = json.load(f)
            
            if not professeurs:
                return "📋 Aucun professeur enregistré"
            
            result = "📋 **Liste des professeurs :**\n\n"
            for prof in professeurs:
                result += f"• **{prof.get('nom', 'N/A')}** (ID: {prof.get('id', 'N/A')})\n"
                result += f"  📧 {prof.get('email', 'N/A')}\n"
                result += f"  🎯 Spécialité: {prof.get('specialite', 'N/A')}\n\n"
            
            return result
            
        except Exception as e:
            return f"❌ Erreur: {str(e)}"
    
    def get_cours(self, data: dict) -> str:
        """Récupère la liste des cours"""
        try:
            with open("data/cours.json", 'r') as f:
                cours = json.load(f)
            
            if not cours:
                return "📋 Aucun cours enregistré"
            
            result = "📋 **Liste des cours :**\n\n"
            for c in cours:
                result += f"• **{c.get('nom', 'N/A')}** (ID: {c.get('id', 'N/A')})\n"
                result += f"  🔖 Code: {c.get('code', 'N/A')}\n"
                result += f"  ⭐ Crédits: {c.get('credits', 'N/A')}\n"
                result += f"  👨‍🏫 Professeur ID: {c.get('professeur_id', 'N/A')}\n\n"
            
            return result
            
        except Exception as e:
            return f"❌ Erreur: {str(e)}"
    
    def get_notes(self, data: dict) -> str:
        """Récupère la liste des notes"""
        try:
            with open("data/notes.json", 'r') as f:
                notes = json.load(f)
            
            if not notes:
                return "📋 Aucune note enregistrée"
            
            result = "📋 **Liste des notes :**\n\n"
            for note in notes:
                result += f"• **Note: {note.get('valeur', 'N/A')}/20** (ID: {note.get('id', 'N/A')})\n"
                result += f"  🎓 Étudiant ID: {note.get('etudiant_id', 'N/A')}\n"
                result += f"  📝 Évaluation ID: {note.get('evaluation_id', 'N/A')}\n"
                if note.get('commentaire'):
                    result += f"  💬 {note.get('commentaire')}\n"
                result += "\n"
            
            return result
            
        except Exception as e:
            return f"❌ Erreur: {str(e)}"
    
    def get_stats(self, data: dict) -> str:
        """Récupère les statistiques du système"""
        try:
            # Récupération des données pour calculer les stats
            current_data = self._get_current_data()
            stats = current_data.get('stats', {})
            
            result = "📊 **Statistiques du système :**\n\n"
            result += f"👨‍🏫 Professeurs: {stats.get('nb_professeurs', 0)}\n"
            result += f"🎓 Étudiants: {stats.get('nb_etudiants', 0)}\n"
            result += f"📚 Cours: {stats.get('nb_cours', 0)}\n"
            result += f"📝 Évaluations: {stats.get('nb_evaluations', 0)}\n"
            result += f"📋 Notes: {stats.get('nb_notes', 0)}\n"
            result += f"⭐ Reviews: {stats.get('nb_reviews', 0)}\n"
            
            return result
            
        except Exception as e:
            return f"❌ Erreur: {str(e)}"
    
    def get_reviews(self, data: dict) -> str:
        """Récupère la liste des reviews"""
        try:
            with open("data/reviews.json", 'r') as f:
                reviews = json.load(f)
            
            if not reviews:
                return "📋 Aucune review enregistrée"
            
            result = "📋 **Liste des reviews :**\n\n"
            for review in reviews:
                result += f"• **Note: {review.get('note', 'N/A')}/5** (ID: {review.get('id', 'N/A')})\n"
                result += f"  🎓 Étudiant ID: {review.get('etudiant_id', 'N/A')}\n"
                result += f"  📚 Cours ID: {review.get('cours_id', 'N/A')}\n"
                if review.get('commentaire'):
                    result += f"  💬 {review.get('commentaire')}\n"
                result += "\n"
            
            return result
            
        except Exception as e:
            return f"❌ Erreur: {str(e)}"
    
    def get_evaluations(self, data: dict) -> str:
        """Récupère la liste des évaluations"""
        try:
            with open("data/evaluations.json", 'r') as f:
                evaluations = json.load(f)
            
            if not evaluations:
                return "📋 Aucune évaluation enregistrée"
            
            result = "📋 **Liste des évaluations :**\n\n"
            for evaluation in evaluations:
                result += f"• **{evaluation.get('nom', 'N/A')}** (ID: {evaluation.get('id', 'N/A')})\n"
                result += f"  📚 Cours ID: {evaluation.get('cours_id', 'N/A')}\n"
                result += f"  📝 Type: {evaluation.get('type', 'N/A')}\n"
                result += f"  ⚖️ Coefficient: {evaluation.get('coefficient', 'N/A')}\n\n"
            
            return result
            
        except Exception as e:
            return f"❌ Erreur: {str(e)}"
    
    def _get_current_data(self) -> dict:
        """Récupère les données actuelles du système pour les stats"""
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