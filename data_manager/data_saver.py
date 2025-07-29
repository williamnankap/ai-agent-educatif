import json
import os
from typing import List, Dict, Any
from datetime import datetime

class DataSaver:
    def __init__(self, data_path: str = "data/"):
        self.data_path = data_path
        # Créer le dossier s'il n'existe pas
        os.makedirs(data_path, exist_ok=True)
    
    def save_json_file(self, filename: str, data: List[Dict[str, Any]]) -> bool:
        """Sauvegarde des données dans un fichier JSON"""
        file_path = os.path.join(self.data_path, filename)
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Erreur lors de la sauvegarde de {filename}: {e}")
            return False
    
    def save_professeurs(self, data: List[Dict[str, Any]]) -> bool:
        return self.save_json_file("professeurs.json", data)
    
    def save_etudiants(self, data: List[Dict[str, Any]]) -> bool:
        return self.save_json_file("etudiants.json", data)
    
    def save_cours(self, data: List[Dict[str, Any]]) -> bool:
        return self.save_json_file("cours.json", data)
    
    def save_evaluations(self, data: List[Dict[str, Any]]) -> bool:
        return self.save_json_file("evaluations.json", data)
    
    def save_notes(self, data: List[Dict[str, Any]]) -> bool:
        return self.save_json_file("notes.json", data)
    
    def save_reviews(self, data: List[Dict[str, Any]]) -> bool:
        return self.save_json_file("reviews.json", data)
    
    def _load_json_file(self, filename: str) -> List[Dict[str, Any]]:
        """Charge un fichier JSON"""
        file_path = os.path.join(self.data_path, filename)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f"Erreur lors du chargement de {filename}: {e}")
            return []
    
    def save_professeur(self, professeur) -> object:
        """Sauvegarde un professeur individuel"""
        professeurs = self._load_json_file("professeurs.json")
        
        if hasattr(professeur, 'id') and professeur.id:
            for i, p in enumerate(professeurs):
                if p.get('id') == professeur.id:
                    professeurs[i] = professeur.to_dict()
                    break
        else:
            new_id = (max([p.get('id', 0) for p in professeurs]) if professeurs else 0) + 1
            professeur.id = new_id
            professeur_dict = professeur.to_dict()
            professeur_dict['date_creation'] = datetime.now().isoformat()
            professeurs.append(professeur_dict)
        
        self.save_professeurs(professeurs)
        return professeur
    
    def save_etudiant(self, etudiant) -> object:
        """Sauvegarde un étudiant individuel"""
        etudiants = self._load_json_file("etudiants.json")
        
        if hasattr(etudiant, 'id') and etudiant.id:
            for i, e in enumerate(etudiants):
                if e.get('id') == etudiant.id:
                    etudiants[i] = etudiant.to_dict()
                    break
        else:
            new_id = (max([e.get('id', 0) for e in etudiants]) if etudiants else 0) + 1
            etudiant.id = new_id
            etudiant_dict = etudiant.to_dict()
            etudiant_dict['date_creation'] = datetime.now().isoformat()
            etudiants.append(etudiant_dict)
        
        self.save_etudiants(etudiants)
        return etudiant
    
    def save_cours(self, cours) -> object:
        """Sauvegarde un cours individuel"""
        cours_list = self._load_json_file("cours.json")
        
        if hasattr(cours, 'id') and cours.id:
            for i, c in enumerate(cours_list):
                if c.get('id') == cours.id:
                    cours_list[i] = cours.to_dict()
                    break
        else:
            new_id = (max([c.get('id', 0) for c in cours_list]) if cours_list else 0) + 1
            cours.id = new_id
            cours_dict = cours.to_dict()
            cours_dict['date_creation'] = datetime.now().isoformat()
            cours_list.append(cours_dict)
        
        self.save_json_file("cours.json", cours_list)
        return cours
    
    def save_note(self, note) -> object:
        """Sauvegarde une note individuelle"""
        notes = self._load_json_file("notes.json")
        
        if hasattr(note, 'id') and note.id:
            for i, n in enumerate(notes):
                if n.get('id') == note.id:
                    notes[i] = note.to_dict()
                    break
        else:
            new_id = (max([n.get('id', 0) for n in notes]) if notes else 0) + 1
            note.id = new_id
            note_dict = note.to_dict()
            note_dict['date_creation'] = datetime.now().isoformat()
            notes.append(note_dict)
        
        self.save_notes(notes)
        return note
    
    def delete_professeur(self, prof_id: int) -> bool:
        """Supprime un professeur"""
        professeurs = self._load_json_file("professeurs.json")
        original_count = len(professeurs)
        professeurs = [p for p in professeurs if p.get('id') != prof_id]
        
        if len(professeurs) < original_count:
            self.save_professeurs(professeurs)
            return True
        return False
    
    def delete_etudiant(self, etudiant_id: int) -> bool:
        """Supprime un étudiant"""
        etudiants = self._load_json_file("etudiants.json")
        original_count = len(etudiants)
        etudiants = [e for e in etudiants if e.get('id') != etudiant_id]
        
        if len(etudiants) < original_count:
            self.save_etudiants(etudiants)
            return True
        return False
    
    def delete_cours(self, cours_id: int) -> bool:
        """Supprime un cours"""
        cours_list = self._load_json_file("cours.json")
        original_count = len(cours_list)
        cours_list = [c for c in cours_list if c.get('id') != cours_id]
        
        if len(cours_list) < original_count:
            self.save_json_file("cours.json", cours_list)
            return True
        return False