#!/usr/bin/env python3
"""
Test rapide de création de professeur
"""
import json
from ai_agent.agent import EducationalAgent

def test_create_professor():
    agent = EducationalAgent()
    
    # Test avec JSON direct
    json_command = '{"action": "create_professeur", "nom": "Test Professeur", "specialite": "Test"}'
    
    print("=== Test création professeur ===")
    print(f"Commande: {json_command}")
    
    result = agent.process_query(json_command)
    print(f"Résultat: {result}")
    
    # Vérifier le fichier
    with open("data/professeurs.json", 'r') as f:
        profs = json.load(f)
    
    print(f"Professeurs dans le fichier: {len(profs)}")
    for prof in profs:
        print(f"  - {prof}")

if __name__ == "__main__":
    test_create_professor()