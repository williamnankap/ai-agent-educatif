import json
import os
from typing import List, Dict, Any

class DataLoader:
    def __init__(self, data_path: str = "data/"):
        self.data_path = data_path
    
    def load_json_file(self, filename: str) -> List[Dict[str, Any]]:
        """Charge un fichier JSON et retourne la liste des données"""
        file_path = os.path.join(self.data_path, filename)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
    
    def load_professeurs(self) -> List[Dict[str, Any]]:
        return self.load_json_file("professeurs.json")
    
    def load_etudiants(self) -> List[Dict[str, Any]]:
        return self.load_json_file("etudiants.json")
    
    def load_cours(self) -> List[Dict[str, Any]]:
        return self.load_json_file("cours.json")
    
    def load_evaluations(self) -> List[Dict[str, Any]]:
        return self.load_json_file("evaluations.json")
    
    def load_notes(self) -> List[Dict[str, Any]]:
        return self.load_json_file("notes.json")
    
    def load_reviews(self) -> List[Dict[str, Any]]:
        return self.load_json_file("reviews.json")
    
    def load_all_data(self) -> Dict[str, List[Dict[str, Any]]]:
        """Charge toutes les données du système"""
        return {
            "professeurs": self.load_professeurs(),
            "etudiants": self.load_etudiants(),
            "cours": self.load_cours(),
            "evaluations": self.load_evaluations(),
            "notes": self.load_notes(),
            "reviews": self.load_reviews()
        }