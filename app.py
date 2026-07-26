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
# STYLE CSS AVANCÉ & TEXTE EN NOIR LORS DE LA SAISIE
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
    
    /* Forcer l'écriture en NOIR lors de la saisie dans les champs de texte */
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
        color: #000000 !important;
        background-color: #FFFFFF !important;
        -webkit-text-fill-color: #000000 !important;
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
        [
            "🏠 Accueil", 
            "🤖 Assistant Juridique IA", 
            "📄 Générateur de Contrats", 
            "📁 Gestion de Dossiers", 
            "👥 Annuaire des Experts", 
            "ℹ️ À propos"
        ]
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
                <h3>📁 Suivi de Dossiers</h3>
                <p>Centralisez l'ensemble de vos pièces justificatives, échéances et suivis de procédures en toute sécurité.</p>
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
        
    details = st.text_area("Détails spécifiques et clauses particulières :")
    
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
# PAGE 4 : GESTION DE DOSSIERS
# ==========================================
elif menu == "📁 Gestion de Dossiers":
    st.markdown("## 📁 Espace de Gestion des Dossiers")
    st.markdown("Suivez l'état d'avancement de vos procédures et centralisez vos pièces.")
    
    with st.form("dossier_form"):
        nom_dossier = st.text_input("Intitulé du dossier (ex: Contentieux commercial - Client X)")
        type_procedure = st.selectbox("Nature de la procédure :", ["amiable", "judiciaire", "conseil"])
        date_echeance = st.date_input("Prochaine échéance / Date limite :")
        notes_dossier = st.text_area("Notes et observations :")
        
        submit_dossier = st.form_submit_button("Enregistrer le dossier")
        
        if submit_dossier:
            if nom_dossier:
                st.success(f"Dossier '{nom_dossier}' enregistré avec succès dans votre espace sécurisé !")
            else:
                st.error("Veuillez indiquer un intitulé pour ce dossier.")

# ==========================================
# PAGE 5 : ANNUAIRE DES EXPERTS
# ==========================================
elif menu == "👥 Annuaire des Experts":
    st.markdown("## 👥 Annuaire des Professionnels du Droit")
    st.markdown("Trouvez un conseil qualifié ou un partenaire expert pour vous accompagner.")
    
    spec = st.selectbox("Filtrer par spécialité :", ["Tous", "Droit des Affaires", "Droit Immobilier", "Droit Social", "Droit Pénal"])
    
    st.markdown("""
        <div class='glass-card'>
            <h3>Me Maître Avocat</h3>
            <p><b>Spécialité :</b> Droit des Affaires & Fiscalité</p>
            <p><b>Barreau :</b> Paris | <b>Expérience :</b> 12 ans</p>
            <p><i>Disponible pour consultations en ligne et accompagnement stratégique.</i></p>
        </div>
        <div class='glass-card'>
            <h3>Cabinet Juridique Associés</h3>
            <p><b>Spécialité :</b> Droit Social & Contentieux du Travail</p>
            <p><b>Barreau :</b> Lyon | <b>Expérience :</b> 15 ans</p>
            <p><i>Accompagnement complet des entreprises et des salariés.</i></p>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# PAGE 6 : À PROPOS
# ==========================================
elif menu == "ℹ️ À propos":
    st.markdown("## ℹ️ À propos de Juria")
    st.markdown("""
        <div class='glass-card'>
            <p><b>Juria</b> est une solution LegalTech innovante conçue pour simplifier, sécuriser et accélérer les démarches juridiques des professionnels et des particuliers.</p>
            <p>Notre mission est de rendre le droit plus accessible grâce à l'intelligence artificielle tout en garantissant les plus hauts standards de sécurité et de confidentialité des données.</p>
            <hr>
            <p style='color: #A0AAB2; font-size: 13px;'>Version 2.1.0-PRO | Tous droits réservés - Juria LegalTech</p>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# HORLOGE UNIVERSELLE (Pied de page)
# ==========================================
st.markdown("---")
current_utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
st.markdown(f"<div style='text-align: right;'><span style='font-size: 11px; color: #A0AAB2;'>UTC Time: {current_utc}</span></div>", unsafe_allow_html=True)
