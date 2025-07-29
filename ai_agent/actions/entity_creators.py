import json
from datetime import datetime


class EntityCreators:
    """Classe pour gérer la création d'entités dans le système éducatif"""
    
    def create_professeur(self, data: dict) -> str:
        """Crée un professeur"""
        try:
            nom = data.get("nom", "Professeur Inconnu")
            email = data.get("email", f"{nom.lower().replace(' ', '.')}@university.com")
            specialite = data.get("specialite", "Enseignement général")
            
            json_path = "data/professeurs.json"
            with open(json_path, 'r') as f:
                professeurs = json.load(f)
            
            new_id = (max([p.get('id', 0) for p in professeurs]) if professeurs else 0) + 1
            
            nouveau = {
                "id": new_id,
                "nom": nom,
                "email": email,
                "specialite": specialite,
                "date_creation": datetime.now().isoformat()
            }
            
            professeurs.append(nouveau)
            
            with open(json_path, 'w') as f:
                json.dump(professeurs, f, indent=2, ensure_ascii=False)
            
            return f"✅ Professeur {nom} créé (ID: {new_id})"
            
        except Exception as e:
            return f"❌ Erreur: {str(e)}"
    
    def create_etudiant(self, data: dict) -> str:
        """Crée un étudiant"""
        try:
            nom = data.get("nom", "Étudiant Inconnu")
            email = data.get("email", f"{nom.lower().replace(' ', '.')}@student.com")
            
            # Calcul du numéro d'étudiant
            try:
                with open("data/etudiants.json", 'r') as f:
                    existing_students = json.load(f)
                numero = data.get("numero_etudiant", f"E2024{len(existing_students) + 1:03d}")
            except:
                numero = data.get("numero_etudiant", "E2024001")
            
            json_path = "data/etudiants.json"
            with open(json_path, 'r') as f:
                etudiants = json.load(f)
            
            new_id = (max([e.get('id', 0) for e in etudiants]) if etudiants else 0) + 1
            
            nouveau = {
                "id": new_id,
                "nom": nom,
                "email": email,
                "numero_etudiant": numero,
                "date_creation": datetime.now().isoformat()
            }
            
            etudiants.append(nouveau)
            
            with open(json_path, 'w') as f:
                json.dump(etudiants, f, indent=2, ensure_ascii=False)
            
            return f"✅ Étudiant {nom} créé (ID: {new_id})"
            
        except Exception as e:
            return f"❌ Erreur: {str(e)}"
    
    def create_cours(self, data: dict) -> str:
        """Crée un cours"""
        try:
            nom = data.get("nom", "Cours Inconnu")
            code = data.get("code", f"{nom[:3].upper()}001")
            credits = data.get("credits", 3)
            professeur_id = data.get("professeur_id", 1)
            
            json_path = "data/cours.json"
            with open(json_path, 'r') as f:
                cours = json.load(f)
            
            new_id = (max([c.get('id', 0) for c in cours]) if cours else 0) + 1
            
            nouveau = {
                "id": new_id,
                "nom": nom,
                "code": code,
                "credits": credits,
                "professeur_id": professeur_id,
                "date_creation": datetime.now().isoformat()
            }
            
            cours.append(nouveau)
            
            with open(json_path, 'w') as f:
                json.dump(cours, f, indent=2, ensure_ascii=False)
            
            return f"✅ Cours {nom} créé (ID: {new_id})"
            
        except Exception as e:
            return f"❌ Erreur: {str(e)}"
    
    def create_evaluation(self, data: dict) -> str:
        """Crée une évaluation"""
        try:
            nom = data.get("nom", "Évaluation")
            cours_id = data.get("cours_id", 1)
            eval_type = data.get("type", "controle")
            coefficient = data.get("coefficient", 1)
            
            json_path = "data/evaluations.json"
            with open(json_path, 'r') as f:
                evaluations = json.load(f)
            
            new_id = (max([e.get('id', 0) for e in evaluations]) if evaluations else 0) + 1
            
            nouveau = {
                "id": new_id,
                "nom": nom,
                "cours_id": cours_id,
                "type": eval_type,
                "coefficient": coefficient,
                "date_creation": datetime.now().isoformat()
            }
            
            evaluations.append(nouveau)
            
            with open(json_path, 'w') as f:
                json.dump(evaluations, f, indent=2, ensure_ascii=False)
            
            return f"✅ Évaluation {nom} créée (ID: {new_id})"
            
        except Exception as e:
            return f"❌ Erreur: {str(e)}"
    
    def create_note(self, data: dict) -> str:
        """Crée une note"""
        try:
            etudiant_id = data.get("etudiant_id", 1)
            evaluation_id = data.get("evaluation_id", 1)
            valeur = data.get("valeur", 10.0)
            commentaire = data.get("commentaire", "")
            
            json_path = "data/notes.json"
            with open(json_path, 'r') as f:
                notes = json.load(f)
            
            new_id = (max([n.get('id', 0) for n in notes]) if notes else 0) + 1
            
            nouveau = {
                "id": new_id,
                "etudiant_id": etudiant_id,
                "evaluation_id": evaluation_id,
                "valeur": float(valeur),
                "commentaire": commentaire,
                "date_creation": datetime.now().isoformat()
            }
            
            notes.append(nouveau)
            
            with open(json_path, 'w') as f:
                json.dump(notes, f, indent=2, ensure_ascii=False)
            
            return f"✅ Note {valeur}/20 créée (ID: {new_id})"
            
        except Exception as e:
            return f"❌ Erreur: {str(e)}"
    
    def create_review(self, data: dict) -> str:
        """Crée une review"""
        try:
            etudiant_id = data.get("etudiant_id", 1)
            cours_id = data.get("cours_id", 1)
            note = data.get("note", 3)
            commentaire = data.get("commentaire", "Pas de commentaire")
            
            json_path = "data/reviews.json"
            with open(json_path, 'r') as f:
                reviews = json.load(f)
            
            new_id = (max([r.get('id', 0) for r in reviews]) if reviews else 0) + 1
            
            nouveau = {
                "id": new_id,
                "etudiant_id": etudiant_id,
                "cours_id": cours_id,
                "note": int(note),
                "commentaire": commentaire,
                "date_creation": datetime.now().isoformat()
            }
            
            reviews.append(nouveau)
            
            with open(json_path, 'w') as f:
                json.dump(reviews, f, indent=2, ensure_ascii=False)
            
            return f"✅ Review {note}/5 créée (ID: {new_id})"
            
        except Exception as e:
            return f"❌ Erreur: {str(e)}"