import streamlit as st
import datetime

# ==========================================
# CONFIGURATION DE LA PAGE
# ==========================================
st.set_page_config(
    page_title="Juria | LegalTech Intelligente",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# STYLE CSS AVANCÉ (Glassmorphism & Thème Pro)
# ==========================================
st.markdown("""
    <style>
    /* Fond global et typographie */
    .stApp {
        background-color: #0B132B;
        color: #E0E1DD;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    
    /* Style de la barre latérale */
    [data-testid="stSidebar"] {
        background-color: #1C2541;
        border-right: 1px solid #3A506B;
    }
    [data-testid="stSidebar"] * {
        color: #F8F9FA !important;
    }
    
    /* Cartes de style "Glassmorphism" */
    .glass-card {
        background: rgba(28, 37, 65, 0.7);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(212, 175, 55, 0.3);
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        margin-bottom: 20px;
    }
    
    /* Boutons personnalisés couleur Or */
    .stButton>button {
        background: linear-gradient(135deg, #D4AF37 0%, #AA771C 100%);
        color: #0B132B;
        font-weight: bold;
        border: none;
        padding: 0.6rem 1.2rem;
        border-radius: 8px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(212, 175, 55, 0.5);
    }
    
    /* Titres et accents dorés */
    h1, h2, h3 {
        color: #F4D03F !important;
    }
    
    /* Champs de saisie */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea, .stSelectbox>div>div>div {
        background-color: #0B132B !important;
        color: #000000 !important;
        border: 1px solid #3A506B !important;
        border-radius: 6px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# BARRE LATÉRALE (NAVIGATION)
# ==========================================
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #F4D03F;'>⚖️ JURIA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 14px; color: #A0AAB2;'>LegalTech Intelligente & Sécurisée</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    menu = st.radio(
        "Navigation",
        ["🏠 Accueil", "🤖 Assistant Juridique IA", "📄 Générateur de Contrats", "💼 Espace Avocats & Abonnements", "ℹ️ À propos"]
    )
    
    st.markdown("---")
    st.markdown("### 🔒 Sécurité & Conformité")
    st.markdown("<small>Chiffrement AES-256 de bout en bout. Conforme RGPD et secret professionnel.</small>", unsafe_allow_html=True)

# ==========================================
# PAGE 1 : ACCUEIL
# ==========================================
if menu == "🏠 Accueil":
    st.markdown("""
        <div class='glass-card' style='text-align: center;'>
            <h1>Bienvenue sur Juria LegalTech</h1>
            <p style='font-size: 18px; color: #E0E1DD;'>La plateforme SaaS de nouvelle génération dédiée aux professionnels du droit, aux entreprises et aux particuliers.</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class='glass-card'>
                <h3>🤖 Assistant IA</h3>
                <p>Posez vos questions juridiques complexes et obtenez des analyses structurées basées sur le droit en vigueur.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div class='glass-card'>
                <h3>📄 Rédaction Intelligente</h3>
                <p>Générez des contrats, mises en demeure et actes sur-mesure en quelques clics grâce à nos modèles certifiés.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
            <div class='glass-card'>
                <h3>💼 Réseau Avocats</h3>
                <p>Connectez-vous avec des experts qualifiés et gérez vos abonnements professionnels en toute simplicité.</p>
            </div>
        """, unsafe_allow_html=True)

# ==========================================
# PAGE 2 : ASSISTANT JURIDIQUE IA
# ==========================================
elif menu == "🤖 Assistant Juridique IA":
    st.markdown("## 🤖 Assistant Juridique Intelligent")
    st.markdown("Interrogez notre intelligence artificielle sur des problématiques de droit civil, commercial, social ou pénal.")
    
    domaine = st.selectbox("Sélectionnez le domaine juridique :", ["Droit des Affaires", "Droit du Travail", "Droit Civil", "Droit Immobilier", "Fiscalité"])
    question = st.text_area("Exposez votre situation ou votre question juridique :", placeholder="Ex: Quelles sont les conditions de validité d'une rupture conventionnelle ?")
    
    if st.button("Lancer l'analyse juridique"):
        if question.strip():
            with st.spinner("Analyse de la législation en cours..."):
                # Simulation d'une réponse structurée d'expert
                st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
                st.markdown("### 📌 Synthèse & Analyse Préliminaire")
                st.markdown(f"**Domaine concerné :** {domaine}")
                st.markdown("**Cadre légal applicable :** Analyse générée selon les dispositions réglementaires en vigueur.")
                st.markdown("**Recommandations :**")
                st.markdown("1. Vérifiez l'historique et les clauses spécifiques applicables à votre situation.")
                st.markdown("2. Rassemblez l'ensemble des pièces justificatives (contrats, échanges écrits, notifications).")
                st.markdown("3. *Avertissement : Cette simulation automatisée ne remplace en aucun cas une consultation juridique formelle auprès d'un Avocat inscrit au barreau.*")
                st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.warning("Veuillez saisir une question ou une description de votre situation.")

# ==========================================
# PAGE 3 : GÉNÉRATEUR DE CONTRATS
# ==========================================
elif menu == "📄 Générateur de Contrats":
    st.markdown("## 📄 Générateur d'Actes & Contrats")
    st.markdown("Remplissez les champs ci-dessous pour générer un document juridique pré-formaté.")
    
    type_contrat = st.selectbox("Type de document :", ["Contrat de Prestation de Services", "Lettre de Mise en Demeure", "Statuts de SASU/SARL"])
    
    col_a, col_b = st.columns(2)
    with col_a:
        partie_1 = st.text_input("Nom / Raison sociale (Créancier / Prestataire) :")
    with col_b:
        partie_2 = st.text_input("Nom / Raison sociale (Débiteur / Client) :")
        
, details = st.text_area("Détails spécifiques et clauses particulières :")
    
    if st.button("Générer le document"):
        if partie_1 and partie_2:
            st.success("Document généré avec succès !")
            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            st.markdown(f"### Aperçu : {type_contrat}")
            st.markdown(f"**Entre les soussignés :** {partie_1} et {partie_2}")
            st.markdown("---")
            st.markdown(f"**Dispositions particulières :**\n{details}")
            st.markdown("---")
            st.markdown("*Fait à Paris, le document est prêt pour relecture et signature électronique.*")
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.error("Veuillez renseigner au moins les noms des parties concernées.")

# ==========================================
# PAGE 4 : ESPACE AVOCATS & ABONNEMENTS
# ==========================================
elif menu == "💼 Espace Avocats & Abonnements":
    st.markdown("## 💼 Espace Professionnel & Abonnements Avocats")
    st.markdown("Optimisez votre cabinet grâce à nos offres sur-mesure conçues pour booster votre visibilité et automatiser vos actes.")
    
    col_p1, col_p2, col_p3 = st.columns(3)
    
    with col_p1:
        st.markdown("""
            <div class='glass-card'>
                <h3 style='text-align: center;'>Standard</h3>
                <h2 style='text-align: center; color: #F4D03F;'>49 € <small>/mois</small></h2>
                <hr>
                <p><b>✔️ Annuaire Juria :</b> Référencement de base</p>
                <p><b>✔️ IA :</b> 50 requêtes / mois</p>
                <p><b>✔️ Modèles :</b> Accès standard</p>
                <br>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Choisir Standard", key="btn_std"):
            st.info("Redirection vers le portail de paiement sécurisé (Standard)...")

    with col_p2:
        st.markdown("""
            <div class='glass-card' style='border: 2px solid #F4D03F;'>
                <h3 style='text-align: center;'>Cabinet Pro</h3>
                <h2 style='text-align: center; color: #F4D03F;'>149 € <small>/mois</small></h2>
                <hr>
                <p><b>⭐ Annuaire Juria :</b> Profil mis en avant</p>
                <p><b>🤖 IA :</b> Requêtes illimitées</p>
                <p><b>📄 Modèles :</b> Personnalisation avancée</p>
                <p><b>🔒 Sécurité :</b> Support prioritaire 24/7</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Choisir Cabinet Pro", key="btn_pro"):
            st.success("Souscription en cours au forfait Cabinet Pro...")

    with col_p3:
        st.markdown("""
            <div class='glass-card'>
                <h3 style='text-align: center;'>Cabinet Enterprise</h3>
                <h2 style='text-align: center; color: #F4D03F;'>Sur devis</h2>
                <hr>
                <p><b>🏢 Multi-utilisateurs :</b> Jusqu'à 15 collaborateurs</p>
                <p><b>⚙️ API :</b> Intégration sur-mesure</p>
                <p><b>👨‍💼 Account Manager :</b> Dédié</p>
                <br>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Contacter l'équipe", key="btn_ent"):
            st.info("Un conseiller expert vous contactera sous 24h.")

# ==========================================
# PAGE 5 : À PROPOS
# ==========================================
elif menu == "ℹ️ À propos":
    st.markdown("## ℹ️ À propos de Juria")
    st.markdown("""
        <div class='glass-card'>
            <p><b>Juria</b> est une solution LegalTech innovante conçue pour simplifier, sécuriser et accélérer les démarches juridiques des professionnels et des particuliers.</p>
            <p>Notre mission est de rendre le droit plus accessible grâce à l'intelligence artificielle tout en garantissant les plus hauts standards de sécurité et de confidentialité des données.</p>
            <hr>
            <p style='color: #A0AAB2; font-size: 13px;'>Version 2.0.0-PRO | Tous droits réservés - Juria LegalTech</p>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# HORLOGE UNIVERSELLE (Pied de page)
# ==========================================
st.markdown("---")
current_utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
st.markdown(f"<div style='text-align: right;'><span style='font-size: 11px; color: #A0AAB2;'>UTC Time: {current_utc}</span></div>", unsafe_allow_html=True)
