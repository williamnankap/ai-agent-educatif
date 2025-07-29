import streamlit as st

def show():
    st.title("📚 Documentation - Commandes JSON")
    
    st.markdown("""
    Cette page présente tous les formats JSON disponibles pour interagir avec l'Agent IA.
    Vous pouvez copier-coller ces exemples directement dans le chat.
    """)
    
    # Professeurs
    st.markdown("## 👨‍🏫 Professeurs")
    
    st.markdown("**Créer un professeur :**")
    st.code('''{"action": "create_professeur", "nom": "Dr. Jean Dupont", "specialite": "Mathématiques"}''', language="json")
    
    st.markdown("**Paramètres :**")
    st.markdown("""
    - `nom` : Nom complet du professeur
    - `specialite` : Domaine d'expertise
    """)
    
    st.divider()
    
    # Étudiants
    st.markdown("## 👨‍🎓 Étudiants")
    
    st.markdown("**Créer un étudiant :**")
    st.code('''{"action": "create_etudiant", "nom": "Marie Martin", "numero_etudiant": "E2024003"}''', language="json")
    
    st.markdown("**Paramètres :**")
    st.markdown("""
    - `nom` : Nom complet de l'étudiant
    - `numero_etudiant` : Numéro d'identification unique (format E2024XXX)
    """)
    
    st.divider()
    
    # Cours
    st.markdown("## 📖 Cours")
    
    st.markdown("**Créer un cours :**")
    st.code('''{"action": "create_cours", "nom": "Python Avancé", "code": "PY101", "credits": 4, "professeur_id": 1}''', language="json")
    
    st.markdown("**Paramètres :**")
    st.markdown("""
    - `nom` : Nom du cours
    - `code` : Code unique du cours
    - `credits` : Nombre de crédits (nombre entier)
    - `professeur_id` : ID du professeur responsable
    """)
    
    st.divider()
    
    # Évaluations
    st.markdown("## 📝 Évaluations")
    
    st.markdown("**Créer une évaluation :**")
    st.code('''{"action": "create_evaluation", "nom": "Examen Final", "cours_id": 1, "type": "examen", "coefficient": 2}''', language="json")
    
    st.markdown("**Paramètres :**")
    st.markdown("""
    - `nom` : Nom de l'évaluation
    - `cours_id` : ID du cours associé
    - `type` : Type d'évaluation (examen, controle, projet, etc.)
    - `coefficient` : Coefficient de l'évaluation
    """)
    
    st.divider()
    
    # Notes
    st.markdown("## 📊 Notes")
    
    st.markdown("**Créer une note :**")
    st.code('''{"action": "create_note", "etudiant_id": 1, "evaluation_id": 1, "valeur": 15.5, "commentaire": "Bon travail"}''', language="json")
    
    st.markdown("**Paramètres :**")
    st.markdown("""
    - `etudiant_id` : ID de l'étudiant
    - `evaluation_id` : ID de l'évaluation
    - `valeur` : Note obtenue (nombre décimal)
    - `commentaire` : Commentaire sur la performance (optionnel)
    """)
    
    st.divider()
    
    # Reviews
    st.markdown("## ⭐ Reviews")
    
    st.markdown("**Créer une review :**")
    st.code('''{"action": "create_review", "etudiant_id": 1, "cours_id": 1, "note": 4, "commentaire": "Excellent cours, très instructif"}''', language="json")
    
    st.markdown("**Paramètres :**")
    st.markdown("""
    - `etudiant_id` : ID de l'étudiant qui donne l'avis
    - `cours_id` : ID du cours évalué
    - `note` : Note de satisfaction (1 à 5)
    - `commentaire` : Commentaire détaillé sur le cours
    """)
    
    st.divider()
    
    # Conseils d'utilisation
    st.markdown("## 💡 Conseils d'utilisation")
    
    st.info("""
    **Pour utiliser ces commandes :**
    1. Copiez le format JSON désiré
    2. Modifiez les valeurs selon vos besoins
    3. Collez dans le chat de l'Agent IA
    4. L'agent executera automatiquement la commande
    
    **Vous pouvez aussi poser des questions en langage naturel !**
    - "Combien de professeurs avons-nous ?"
    - "Liste tous les cours disponibles"
    - "Quelles sont les notes de l'étudiant 1 ?"
    """)
    
    st.success("✅ Toutes les entités supportent maintenant la création via JSON !")