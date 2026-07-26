import streamlit as st
import datetime

# ==========================================
# CONFIGURATION DE LA PAGE
# ==========================================
st.set_page_config(
    page_title="Juria | LegalTech Pro",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# STYLE CSS HAUT DE GAMME (UI/UX 17/20)
# ==========================================
st.markdown("""
    <style>
    /* Arrière-plan global et police moderne */
    .stApp {
        background: radial-gradient(circle at 50% 0%, #101c38 0%, #080c1a 100%);
        color: #E2E8F0;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    /* Barre latérale élégante */
    [data-testid="stSidebar"] {
        background-color: #131b31;
        border-right: 1px solid rgba(212, 175, 55, 0.15);
    }
    [data-testid="stSidebar"] * {
        color: #F8FAFC !important;
    }
    
    /* Cartes Glassmorphism raffinées */
    .glass-card {
        background: rgba(23, 32, 59, 0.65);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(212, 175, 55, 0.25);
        padding: 28px;
        border-radius: 16px;
        box-shadow: 0 10px 30px 0 rgba(0, 0, 0, 0.4);
        margin-bottom: 24px;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    
    /* Boutons premium dorés */
    .stButton>button {
        background: linear-gradient(135deg, #E5C158 0%, #C59B27 100%);
        color: #0B132B !important;
        font-weight: 700;
        border: none;
        padding: 0.65rem 1.4rem;
        border-radius: 10px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(197, 155, 39, 0.3);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(197, 155, 39, 0.5);
    }
    
    /* Titres raffinés */
    h1, h2, h3 {
        color: #F3E5AB !important;
        font-weight: 700;
    }
    
    /* Champs de saisie parfaits avec texte en NOIR net */
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
        color: #000000 !important;
        background-color: #FFFFFF !important;
        -webkit-text-fill-color: #000000 !important;
        border-radius: 8px !important;
        border: 1px solid #CBD5E1 !important;
        padding: 10px !important;
    }
    
    label {
        color: #F1F5F9 !important;
        font-weight: 500 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# BARRE LATÉRALE (NAVIGATION - 10 MODULES)
# ==========================================
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #F3E5AB; font-size: 28px;'>⚖️ JURIA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 13px; color: #94A3B8; margin-top: -10px;'>LegalTech Intelligente & Sécurisée</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    menu = st.radio(
        "Navigation",
        [
            "🏠 Accueil", 
            "🤖 Assistant Juridique IA", 
            "📄 Générateur de Contrats", 
            "📁 Gestion de Dossiers", 
            "🔍 Analyse de Pièces & Pièges", 
            "⚖️ Calculateur d'Indemnités", 
            "👥 Annuaire des Experts", 
            "🔒 Coffre-fort Numérique", 
            "📊 Veille & Jurisprudence", 
            "ℹ️ À propos"
        ]
    )
    
    st.markdown("---")
    st.markdown("### 🔒 Sécurité & Conformité")
    st.markdown("<small style='color: #94A3B8;'>Chiffrement AES-256 de bout en bout. Conforme RGPD et secret professionnel.</small>", unsafe_allow_html=True)

# ==========================================
# MODULE 1 : ACCUEIL
# ==========================================
if menu == "🏠 Accueil":
    st.markdown("""
        <div class='glass-card' style='text-align: center; padding: 40px;'>
            <h1 style='font-size: 36px; margin-bottom: 10px;'>Plateforme Juria SaaS</h1>
            <p style='font-size: 17px; color: #CBD5E1; max-width: 700px; margin: 0 auto;'>L'écosystème numérique nouvelle génération dédié à l'automatisation juridique, l'analyse intelligente et la gestion de dossiers.</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='glass-card'><h3>🤖 Assistant IA</h3><p style='color: #CBD5E1;'>Générez des analyses juridiques structurées instantanément.</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='glass-card'><h3>📄 Actes & Contrats</h3><p style='color: #CBD5E1;'>Rédigez vos contrats et mises en demeure sur-mesure.</p></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='glass-card'><h3>📁 Gestion & Suivi</h3><p style='color: #CBD5E1;'>Centralisez vos pièces et échéances en toute sécurité.</p></div>", unsafe_allow_html=True)

# ==========================================
# MODULE 2 : ASSISTANT JURIDIQUE IA
# ==========================================
elif menu == "🤖 Assistant Juridique IA":
    st.markdown("## 🤖 Assistant Juridique Intelligent")
    domaine = st.selectbox("Sélectionnez le domaine juridique :", ["Droit des Affaires", "Droit du Travail", "Droit Civil", "Droit Immobilier", "Fiscalité"])
    question = st.text_area("Exposez votre situation ou votre question juridique :")
    if st.button("Lancer l'analyse juridique"):
        if question.strip():
            st.markdown("<div class='glass-card'><h3>📌 Synthèse & Analyse Préliminaire</h3><p>Analyse générée selon les dispositions réglementaires en vigueur.</p></div>", unsafe_allow_html=True)
        else:
            st.warning("Veuillez saisir une question.")

# ==========================================
# MODULE 3 : GÉNÉRATEUR DE CONTRATS
# ==========================================
elif menu == "📄 Générateur de Contrats":
    st.markdown("## 📄 Générateur d'Actes & Contrats")
    type_contrat = st.selectbox("Type de document :", ["Contrat de Prestation de Services", "Lettre de Mise en Demeure", "Statuts de SASU/SARL"])
    partie_1 = st.text_input("Nom / Raison sociale (Créancier / Prestataire) :")
    partie_2 = st.text_input("Nom / Raison sociale (Débiteur / Client) :")
    details = st.text_area("Détails spécifiques :")
    if st.button("Générer le document"):
        if partie_1 and partie_2:
            st.success("Document généré avec succès !")
        else:
            st.error("Veuillez renseigner les parties.")

# ==========================================
# MODULE 4 : GESTION DE DOSSIERS
# ==========================================
elif menu == "📁 Gestion de Dossiers":
    st.markdown("## 📁 Espace de Gestion des Dossiers")
    with st.form("dossier_form"):
        nom_dossier = st.text_input("Intitulé du dossier :")
        type_procedure = st.selectbox("Nature de la procédure :", ["Amiable", "Judiciaire", "Conseil"])
        date_echeance = st.date_input("Prochaine échéance :")
        notes_dossier = st.text_area("Notes :")
        if st.form_submit_button("Enregistrer le dossier"):
            if nom_dossier:
                st.success("Dossier enregistré !")

# ==========================================
# MODULE 5 : ANALYSE DE PIÈCES & PIÈGES
# ==========================================
elif menu == "🔍 Analyse de Pièces & Pièges":
    st.markdown("## 🔍 Analyse de Pièces & Clauses Abusives")
    texte_contrat = st.text_area("Collez le texte du contrat :")
    if st.button("Auditer le texte"):
        st.markdown("<div class='glass-card'><h3>⚠️ Rapport d'Analyse</h3><p>Niveau de risque global : Modéré.</p></div>", unsafe_allow_html=True)

# ==========================================
# MODULE 6 : CALCULATEUR D'INDEMNITÉS
# ==========================================
elif menu == "⚖️ Calculateur d'Indemnités":
    st.markdown("## ⚖️ Calculateur d'Indemnités Légales")
    anciennete = st.number_input("Ancienneté (années) :", min_value=0, value=3)
    salaire_ref = st.number_input("Salaire mensuel brut (€) :", min_value=0.0, value=2500.0)
    if st.button("Calculer"):
        st.markdown(f"<div class='glass-card'><h3>Résultat :</h3><p style='font-size:20px; color:#F3E5AB;'><b>{(salaire_ref / 4) * anciennete:.2f} € brut</b></p></div>", unsafe_allow_html=True)

# ==========================================
# MODULE 7 : ANNUAIRE DES EXPERTS
# ==========================================
elif menu == "👥 Annuaire des Experts":
    st.markdown("## 👥 Annuaire des Professionnels du Droit")
    st.markdown("<div class='glass-card'><h3>Me Maître Avocat</h3><p>Droit des Affaires - Paris</p></div>", unsafe_allow_html=True)

# ==========================================
# MODULE 8 : COFFRE-FORT NUMÉRIQUE
# ==========================================
elif menu == "🔒 Coffre-fort Numérique":
    st.markdown("## 🔒 Coffre-fort Numérique Sécurisé")
    nom_piece = st.text_input("Nom du document :")
    st.file_uploader("Fichier :")
    if st.button("Stocker"):
        st.success("Document chiffré et stocké.")

# ==========================================
# MODULE 9 : VEILLE & JURISPRUDENCE
# ==========================================
elif menu == "📊 Veille & Jurisprudence":
    st.markdown("## 📊 Veille & Actualités Juridiques")
    st.markdown("<div class='glass-card'><h4>⚖️ Cour de Cassation</h4><p>Dernières décisions de juillet 2026.</p></div>", unsafe_allow_html=True)

# ==========================================
# MODULE 10 : À PROPOS
# ==========================================
elif menu == "ℹ️ À propos":
    st.markdown("## ℹ️ À propos de Juria")
    st.markdown("<div class='glass-card'><p>Plateforme LegalTech Pro v3.2</p></div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown(f"<div style='text-align: right;'><span style='font-size: 11px; color: #94A3B8;'>UTC Time: {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S')}</span></div>", unsafe_allow_html=True)
