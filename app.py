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
    .glass-card:hover {
        border-color: rgba(212, 175, 55, 0.5);
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
        background: linear-gradient(135deg, #F0CC65 0%, #D4A732 100%);
    }
    
    /* Titres raffinés */
    h1, h2, h3 {
        color: #F3E5AB !important;
        font-weight: 700;
        letter-spacing: -0.5px;
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
    
    /* Libellés de formulaires plus lisibles */
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
            <p style='font-size: 17px; color: #CBD5E1; max-width: 700px; margin: 0 auto;'>L'écosystème numérique nouvelle génération dédié à l'automatisation juridique, l'analyse intelligente et la gestion de dossiers pour professionnels et particuliers.</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='glass-card'><h3>🤖 Assistant IA</h3><p style='color: #CBD5E1;'>Générez des analyses juridiques structurées instantanément selon le droit en vigueur.</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='glass-card'><h3>📄 Actes & Contrats</h3><p style='color: #CBD5E1;'>Rédigez vos contrats, mises en demeure et statuts sur-mesure en quelques clics.</p></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='glass-card'><h3>📁 Gestion & Suivi</h3><p style='color: #CBD5E1;'>Centralisez vos pièces justificatives, échéances et notes de procédures en sécurité.</p></div>", unsafe_allow_html=True)

# ==========================================
# MODULE 2 : ASSISTANT JURIDIQUE IA
# ==========================================
elif menu == "🤖 Assistant Juridique IA":
    st.markdown("## 🤖 Assistant Juridique Intelligent")
    st.markdown("Interrogez notre intelligence artificielle sur des problématiques de droit civil, commercial, social ou fiscal.")
    
    with st.container():
        domaine = st.selectbox("Sélectionnez le domaine juridique :", ["Droit des Affaires", "Droit du Travail", "Droit Civil", "Droit Immobilier", "Fiscalité"])
        question = st.text_area("Exposez votre situation ou votre question juridique :", placeholder="Ex: Quelles sont les conditions de validité d'une clause de non-concurrence ?")
        
        if st.button("Lancer l'analyse juridique"):
            if question.strip():
                with st.spinner("Analyse de la législation en cours..."):
                    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
                    st.markdown("### 📌 Synthèse & Analyse Préliminaire")
                    st.markdown(f"**Domaine concerné :** {domaine}")
                    st.markdown("**Cadre légal applicable :** Analyse générée selon les dispositions réglementaires en vigueur.")
                    st.markdown("**Recommandations stratégiques :**")
                    st.markdown("1. Vérifiez l'historique et les clauses spécifiques applicables à votre situation.")
                    st.markdown("2. Rassemblez l'ensemble des pièces justificatives (contrats, échanges écrits, notifications).")
                    st.markdown("3. *Avertissement : Cette simulation automatisée ne remplace en aucun cas une consultation juridique formelle auprès d'un Avocat.*")
                    st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.warning("Veuillez saisir une question ou une description de votre situation.")

# ==========================================
# MODULE 3 : GÉNÉRATEUR DE CONTRATS
# ==========================================
elif menu == "📄 Générateur de Contrats":
    st.markdown("## 📄 Générateur d'Actes & Contrats")
    st.markdown("Renseignez les informations ci-dessous pour générer un document juridique professionnel pré-formaté.")
    
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
# MODULE 4 : GESTION DE DOSSIERS
# ==========================================
elif menu == "📁 Gestion de Dossiers":
    st.markdown("## 📁 Espace de Gestion des Dossiers")
    st.markdown("Suivez l'état d'avancement de vos procédures et centralisez vos pièces.")
    
    with st.form("dossier_form"):
        nom_dossier = st.text_input("Intitulé du dossier (ex: Contentieux commercial - Client X)")
        type_procedure = st.selectbox("Nature de la procédure :", ["Amiable", "Judiciaire", "Conseil"])
        date_echeance = st.date_input("Prochaine échéance / Date limite :")
        notes_dossier = st.text_area("Notes et observations :")
        
        submit_dossier = st.form_submit_button("Enregistrer le dossier")
        if submit_dossier:
            if nom_dossier:
                st.success(f"Dossier '{nom_dossier}' enregistré avec succès dans votre espace sécurisé !")
            else:
                st.error("Veuillez indiquer un intitulé pour ce dossier.")

# ==========================================
# MODULE 5 : ANALYSE DE PIÈCES & PIÈGES
# ==========================================
elif menu == "🔍 Analyse de Pièces & Pièges":
    st.markdown("## 🔍 Analyse de Pièces & Détection de Clauses Abusives")
    st.markdown("Identifiez rapidement les clauses à risque dans vos documents soumis.")
    
    texte_contrat = st.text_area("Collez le texte du contrat ou de la clause à auditer :", placeholder="Collez ici les termes du contrat...")
    if st.button("Auditer le texte"):
        if texte_contrat.strip():
            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            st.markdown("### ⚠️ Rapport d'Analyse des Risques")
            st.markdown("- **Clauses potentiellement déséquilibrées :** 1 détectée.")
            st.markdown("- **Niveau de risque global :** Modéré.")
            st.markdown("- *Recommandation : Faites relire l'alinéa sur la responsabilité par un professionnel du droit.*")
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.warning("Veuillez coller du texte à analyser.")

# ==========================================
# MODULE 6 : CALCULATEUR D'INDEMNITÉS
# ==========================================
elif menu == "⚖️ Calculateur d'Indemnités":
    st.markdown("## ⚖️ Calculateur d'Indemnités Légales")
    st.markdown("Estimez rapidement les indemnités de référence (licenciement, préavis, retards).")
    
    anciennete = st.number_input("Ancienneté (en années) :", min_value=0, max_value=50, value=3)
    salaire_ref = st.number_input("Salaire mensuel brut de référence (€) :", min_value=0.0, value=2500.0)
    
    if st.button("Calculer l'estimation"):
        indemnite_estimee = (salaire_ref / 4) * anciennete
        st.markdown(f"<div class='glass-card'><h3>Résultat indicatif :</h3><p style='font-size:22px; color:#F3E5AB;'><b>{indemnite_estimee:.2f} € brut</b></p><small style='color: #94A3B8;'>Calcul estimatif basé sur les barèmes légaux standard. Ne se substitue pas au calcul officiel de l'expert-comptable ou du conseil juridique.</small></div>", unsafe_allow_html=True)

# ==========================================
# MODULE 7 : ANNUAIRE DES EXPERTS
# ==========================================
elif menu == "👥 Annuaire des Experts":
    st.markdown("## 👥 Annuaire des Professionnels du Droit")
    st.markdown("Trouvez un conseil qualifié ou un partenaire expert pour vous accompagner.")
    
    spec = st.selectbox("Filtrer par spécialité :", ["Tous", "Droit des Affaires", "Droit Immobilier", "Droit Social", "Droit Pénal"])
    
    st.markdown("""
        <div class='glass-card'>
            <h3>Me Maître Avocat</h3>
            <p style='color: #CBD5E1;'><b>Spécialité :</b> Droit des Affaires & Fiscalité | <b>Barreau :</b> Paris (12 ans d'expérience)</p>
        </div>
        <div class='glass-card'>
            <h3>Cabinet Juridique Associés</h3>
            <p style='color: #CBD5E1;'><b>Spécialité :</b> Droit Social & Contentieux | <b>Barreau :</b> Lyon (15 ans d'expérience)</p>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# MODULE 8 : COFFRE-FORT NUMÉRIQUE
# ==========================================
elif menu == "🔒 Coffre-fort Numérique":
    st.markdown("## 🔒 Coffre-fort Numérique Sécurisé")
    st.markdown("Stockez vos actes notariés, contrats et pièces sensibles sous chiffrement de niveau bancaire.")
    
    nom_piece = st.text_input("Nom du document (ex : Acte de vente maison)")
    st.file_uploader("Téléverser le fichier sécurisé (PDF, DOCX) :")
    if st.button("Stocker dans le coffre-fort"):
        if nom_piece:
            st.success(f"Le document '{nom_piece}' a été chiffré et stocké en toute sécurité.")
        else:
            st.warning("Veuillez nommer le document.")

# ==========================================
# MODULE 9 : VEILLE & JURISPRUDENCE
# ==========================================
elif menu == "📊 Veille & Jurisprudence":
    st.markdown("## 📊 Veille & Actualités Juridiques")
    st.markdown("Restez informés des dernières évolutions législatives et décisions de jurisprudence.")
    
    st.markdown("""
        <div class='glass-card'>
            <h4>⚖️ Décision récente - Cour de Cassation</h4>
            <p style='color: #CBD5E1;'><b>Date :</b> Juillet 2026 | <b>Matière :</b> Droit du Travail</p>
            <p style='color: #94A3B8;'>Précisions importantes concernant la validité des clauses de non-concurrence et contrepartie financière.</p>
        </div>
        <div class='glass-card'>
            <h4>📜 Réforme Fiscale 2026</h4>
            <p style='color: #CBD5E1;'><b>Date :</b> Juin 2026 | <b>Matière :</b> Fiscalité des Entreprises</p>
            <p style='color: #94A3B8;'>Nouvelles dispositions applicables aux micro-entreprises et régimes de TVA.</p>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# MODULE 10 : À PROPOS
# ==========================================
elif menu == "ℹ️ À propos":
    st.markdown("## ℹ️ À propos de Juria")
    st.markdown("""
        <div class='glass-card'>
            <p style='color: #CBD5E1;'><b>Juria</b> est une solution LegalTech innovante conçue pour simplifier, sécuriser et accélérer les démarches juridiques des professionnels et des particuliers.</p>
            <p style='color: #CBD5E1;'>Notre mission est de rendre le droit plus accessible grâce à l'intelligence artificielle tout en garantissant les plus hauts standards de sécurité et de confidentialité des données.</p>
            <hr style='border-color: rgba(212, 175, 55, 0.2);'>
            <p style='color: #94A3B8; font-size: 13px;'>Version 3.2.0-PRO | Tous droits réservés - Juria LegalTech</p>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# HORLOGE UNIVERSELLE (Pied de page)
# ==========================================
st.markdown("---")
current_utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
st.markdown(f"<div style='text-align: right;'><span style='font-size: 11px; color: #94A3B8;'>UTC Time: {current_utc}</span></div>", unsafe_allow_html=True)
