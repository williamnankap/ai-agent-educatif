#!/usr/bin/env python3
"""
Test simple des fonctions de création
"""
import json
import os
from datetime import datetime

def test_create_prof_direct():
    """Test direct de création de professeur"""
    
    # Simuler les données
    data = {
        "nom": "Dr. Test",
        "specialite": "Test Science"
    }
    
    nom = data.get("nom", "Professeur Inconnu")
    email = data.get("email", f"{nom.lower().replace(' ', '.')}@university.com")
    specialite = data.get("specialite", "Enseignement général")
    
    json_path = "data/professeurs.json"
    
    # Lire le fichier existant
    with open(json_path, 'r') as f:
        professeurs = json.load(f)
    
    print(f"Professeurs avant: {len(professeurs)}")
    
    # Créer nouveau prof
    new_id = (max([p.get('id', 0) for p in professeurs]) if professeurs else 0) + 1
    
    nouveau = {
        "id": new_id,
        "nom": nom,
        "email": email,
        "specialite": specialite,
        "date_creation": datetime.now().isoformat()
    }
    
    professeurs.append(nouveau)
    
    # Sauvegarder
    with open(json_path, 'w') as f:
        json.dump(professeurs, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Professeur {nom} créé (ID: {new_id})")
    print(f"Professeurs après: {len(professeurs)}")

if __name__ == "__main__":
    test_create_prof_direct()