import json
import os
from typing import Dict, List, Any, Optional

class JsonHandler:
    def __init__(self, base_path: str = "data/"):
        self.base_path = base_path
        os.makedirs(base_path, exist_ok=True)
    
    def read_json(self, filename: str) -> List[Dict[str, Any]]:
        """Lit un fichier JSON et retourne les données"""
        filepath = os.path.join(self.base_path, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def write_json(self, filename: str, data: List[Dict[str, Any]]) -> bool:
        """Écrit des données dans un fichier JSON"""
        filepath = os.path.join(self.base_path, filename)
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Erreur écriture {filename}: {e}")
            return False
    
    def add_item(self, filename: str, item: Dict[str, Any]) -> Optional[int]:
        """Ajoute un élément au fichier JSON et retourne son ID"""
        data = self.read_json(filename)
        
        # Générer un nouvel ID
        max_id = max([item.get('id', 0) for item in data]) if data else 0
        item['id'] = max_id + 1
        
        data.append(item)
        
        if self.write_json(filename, data):
            return item['id']
        return None
    
    def get_by_id(self, filename: str, item_id: int) -> Optional[Dict[str, Any]]:
        """Récupère un élément par son ID"""
        data = self.read_json(filename)
        for item in data:
            if item.get('id') == item_id:
                return item
        return None
    
    def update_by_id(self, filename: str, item_id: int, updates: Dict[str, Any]) -> bool:
        """Met à jour un élément par son ID"""
        data = self.read_json(filename)
        for i, item in enumerate(data):
            if item.get('id') == item_id:
                data[i].update(updates)
                return self.write_json(filename, data)
        return False
    
    def delete_by_id(self, filename: str, item_id: int) -> bool:
        """Supprime un élément par son ID"""
        data = self.read_json(filename)
        original_length = len(data)
        data = [item for item in data if item.get('id') != item_id]
        
        if len(data) < original_length:
            return self.write_json(filename, data)
        return False