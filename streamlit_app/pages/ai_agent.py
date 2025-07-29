import streamlit as st
from ai_agent.agent import EducationalAgent

def show():
    st.title("🤖 Agent IA Éducatif")
    
    # Initialiser l'agent
    if 'agent' not in st.session_state:
        st.session_state.agent = EducationalAgent()
    
    # Initialiser l'historique des messages
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    # Afficher l'historique des messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Zone de saisie pour les messages
    if prompt := st.chat_input("Posez votre question ou utilisez un JSON..."):
        # Ajouter le message utilisateur
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Obtenir la réponse de l'agent
        with st.chat_message("assistant"):
            with st.spinner("Traitement..."):
                response = st.session_state.agent.process_query(prompt)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Boutons d'exemple
    st.sidebar.markdown("### 💡 Exemples")
    
    col1, col2 = st.sidebar.columns(2)
    
    with col1:
        if st.button("➕ Professeur", key="btn_prof"):
            example = '{"action": "create_professeur", "nom": "Dr. Dupont", "specialite": "Mathématiques"}'
            st.session_state.messages.append({"role": "user", "content": example})
            response = st.session_state.agent.process_query(example)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
        
        if st.button("➕ Étudiant", key="btn_etud"):
            example = '{"action": "create_etudiant", "nom": "Marie Martin", "numero_etudiant": "E2024003"}'
            st.session_state.messages.append({"role": "user", "content": example})
            response = st.session_state.agent.process_query(example)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
            
        if st.button("➕ Cours", key="btn_cours"):
            example = '{"action": "create_cours", "nom": "Python Avancé", "code": "PY101", "credits": 4, "professeur_id": 1}'
            st.session_state.messages.append({"role": "user", "content": example})
            response = st.session_state.agent.process_query(example)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
    
    with col2:
        if st.button("➕ Évaluation", key="btn_eval"):
            example = '{"action": "create_evaluation", "nom": "Examen Final", "cours_id": 1, "type": "examen"}'
            st.session_state.messages.append({"role": "user", "content": example})
            response = st.session_state.agent.process_query(example)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
            
        if st.button("➕ Note", key="btn_note"):
            example = '{"action": "create_note", "etudiant_id": 1, "evaluation_id": 1, "valeur": 16.5}'
            st.session_state.messages.append({"role": "user", "content": example})
            response = st.session_state.agent.process_query(example)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
            
        if st.button("➕ Review", key="btn_review"):
            example = '{"action": "create_review", "etudiant_id": 1, "cours_id": 1, "note": 5, "commentaire": "Excellent cours"}'
            st.session_state.messages.append({"role": "user", "content": example})
            response = st.session_state.agent.process_query(example)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()
    
    if st.sidebar.button("🗑️ Effacer historique"):
        st.session_state.messages = []
        st.rerun()