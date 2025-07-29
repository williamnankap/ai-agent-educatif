import json
from ..actions.entity_creators import EntityCreators
from ..actions.data_retrievers import DataRetrievers


class ActionProcessor:
    """Classe pour traiter les actions JSON et router vers les bons handlers"""
    
    def __init__(self):
        self.entity_creators = EntityCreators()
        self.data_retrievers = DataRetrievers()
        
    def execute_actions(self, response_text: str) -> str:
        """Détecte et exécute les actions JSON"""
        actions = [
            ("create_professeur", self.entity_creators.create_professeur),
            ("create_etudiant", self.entity_creators.create_etudiant),
            ("create_cours", self.entity_creators.create_cours),
            ("create_evaluation", self.entity_creators.create_evaluation),
            ("create_note", self.entity_creators.create_note),
            ("create_review", self.entity_creators.create_review),
            ("get_etudiants", self.data_retrievers.get_etudiants),
            ("get_professeurs", self.data_retrievers.get_professeurs),
            ("get_cours", self.data_retrievers.get_cours),
            ("get_notes", self.data_retrievers.get_notes),
            ("get_stats", self.data_retrievers.get_stats),
            ("get_reviews", self.data_retrievers.get_reviews),
            ("get_evaluations", self.data_retrievers.get_evaluations)
        ]
        
        # Cherche les patterns JSON avec différentes variantes
        for action_type, handler in actions:
            patterns = [
                f'{{"action": "{action_type}"',
                f'{{"action":"{action_type}"',
                f'{{ "action": "{action_type}"',
                f'{{ "action":"{action_type}"'
            ]
            
            for pattern in patterns:
                if pattern in response_text:
                    return self._handle_json_action(response_text, action_type, handler)
        
        return response_text
    
    def _handle_json_action(self, response_text: str, action_type: str, handler_func):
        """Gère l'exécution d'une action JSON"""
        try:
            # Trouve le début du JSON
            patterns = [
                f'{{"action": "{action_type}"',
                f'{{"action":"{action_type}"',
                f'{{ "action": "{action_type}"',
                f'{{ "action":"{action_type}"'
            ]
            
            start = -1
            for pattern in patterns:
                start = response_text.find(pattern)
                if start != -1:
                    break
            
            if start == -1:
                return response_text + "\n\n❌ JSON non trouvé"
            
            # Trouve la fin du JSON en comptant les accolades
            brace_count = 0
            end = start
            for i, char in enumerate(response_text[start:]):
                if char == '{':
                    brace_count += 1
                elif char == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        end = start + i + 1
                        break
            
            json_str = response_text[start:end]
            print(f"DEBUG: Extracted JSON: {json_str}")  # Debug
            
            data = json.loads(json_str)
            result = handler_func(data)
            
            return result  # Retourne juste le résultat, pas le texte original
            
        except Exception as e:
            return response_text + f"\n\n❌ Erreur JSON: {str(e)}"