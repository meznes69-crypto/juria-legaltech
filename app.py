import streamlit as st
import datetime

# Configuration de la page
st.set_page_config(
    page_title="Juria | LegalTech Intelligente",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Style CSS avancé : Glassmorphism, palette bleu marine profond, écriture dorée dans la sidebar et texte noir lors de la saisie
st.markdown("""
    <style>
    /* Fond global et typographie */
    .stApp {
        background-color: #0b1329;
        color: #ffffff;
        font-family: 'Inter', 'Roboto', sans-serif;
    }
    
    /* Barre latérale en bleu marine profond avec effet de verre dépoli */
    [data-testid="stSidebar"] {
        background: rgba(11, 19, 41, 0.85);
        backdrop-filter: blur(12px);
        border-right: 1px solid rgba(59, 130, 246, 0.2);
    }
    
    /* Style personnalisé pour rendre le texte de la sidebar en couleur dorée */
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] span, 
    [data-testid="stSidebar"] label, 
    [data-testid="stSidebar"] div, 
    [data-testid="stSidebar"] h3 {
        color: #d4af37 !important;
    }
    
    /* Forcer le texte saisi dans les champs de texte à devenir noir */
    input, textarea, select {
        color: #000000 !important;
    }
    
    /* Cartes en verre dépoli (Glassmorphism) */
    .glass-card {
        background: rgba(30, 58, 138, 0.25);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(96, 165, 250, 0.3);
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        margin-bottom: 20px;
        transition: all 0.3s ease;
    }
    .glass-card:hover {
        border-color: rgba(96, 165, 250, 0.6);
        box-shadow: 0 8px 32px 0 rgba(37, 99, 235, 0.2);
    }
    
    /* Boutons personnalisés futuristes */
    .stButton>button {
        background: linear-gradient(135deg, #2563eb 0%, #3b82f6 100%);
        color: white;
        border-radius: 8px;
        border: 1px solid rgba(147, 197, 253, 0.4);
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(37, 99, 235, 0.4);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #1d4ed8 0%, #2563eb 100%);
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.6);
        border-color: #60a5fa;
    }
    
    /* Séparateurs lumineux */
    hr {
        border-color: rgba(59, 130, 246, 0.3);
    }
    
    /* Monospace pour les horodatages */
    .mono-text {
        font-family: 'Courier New', Courier, monospace;
        color: #d4af37;
    }
    </style>
""", unsafe_allow_html=True)

# Barre latérale (Sidebar) avec les textes exacts demandés
st.sidebar.markdown("### **JURIA**")
st.sidebar.markdown("---")
st.sidebar.markdown("**Votre Nom / Identifiant**")
st.sidebar.write("Mounir Nasdas")
st.sidebar.markdown("---")
st.sidebar.write("Connecté en tant que : Mounir Nasdas")

st.sidebar.markdown("---")
st.sidebar.markdown("### **Navigation rapide**")

# Intégration complète des 10 modules sans aucun bug de routage
menu = st.sidebar.radio("Aller vers :", [
    "Tableau de bord",
    "IA Juridique Avancée (Gratuit)",
    "Rendez-vous Avocats",
    "Stockage sécurisé",
    "Génération de Courriers",
    "Suivi des procédures",
    "Messagerie & Suivi",
    "Signature Électronique",
    "Paiement et facturation",
    "Administrateur Back-Office"
])

st.sidebar.markdown("---")
st.sidebar.info("📌 Session active - Sécurisée SSL")

# Routage complet de tous les modules
if menu == "Tableau de bord":
    # En-tête exact demandé
    st.title("Juria - Plateforme LegalTech")
    st.markdown("### Bienvenue dans votre espace intelligent, **Mounir Nasdas**. Gérez vos dossiers et votre relation juridique en toute simplicité.")
    st.markdown("---")
    
    # Cartes individuelles de "verre" avec les métriques exactes
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
            <div class="glass-card">
                <h4 style="color: #d4af37; font-size: 16px; margin-bottom: 5px;">Dossiers en cours</h4>
                <h2 style="color: #ffffff; font-size: 28px; margin: 0;">4</h2>
                <p style="color: #d4af37; font-size: 12px; margin-top: 5px;">(Actif)</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div class="glass-card">
                <h4 style="color: #d4af37; font-size: 16px; margin-bottom: 5px;">Notifications</h4>
                <h2 style="color: #ffffff; font-size: 28px; margin: 0;">2</h2>
                <p style="color: #d4af37; font-size: 12px; margin-top: 5px;">(Non lues)</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
            <div class="glass-card">
                <h4 style="color: #d4af37; font-size: 16px; margin-bottom: 5px;">IA Juridique</h4>
                <h2 style="color: #ffffff; font-size: 28px; margin: 0;">100%</h2>
                <p style="color: #d4af37; font-size: 12px; margin-top: 5px;">(Gratuit, Illimité)</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col4:
        st.markdown("""
            <div class="glass-card">
                <h4 style="color: #d4af37; font-size: 16px; margin-bottom: 5px;">Sécurité</h4>
                <h2 style="color: #ffffff; font-size: 28px; margin: 0;">PRO</h2>
                <p style="color: #d4af37; font-size: 12px; margin-top: 5px;">(AES-256, eIDAS)</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    
    # Section Activité Récente & Centre d'Alertes
    st.markdown("### **Activité Récente & Centre d'Alertes**")
    
    st.markdown("""
        <div class="glass-card">
            <p style="margin: 0 0 10px 0; color: #ffffff;">🟡 <b>[Rendez-vous]</b> Consultation confirmée avec Me Claire Martin le <span class="mono-text">28/07/2026</span> à 14h30.</p>
            <hr style="margin: 8px 0; border-color: rgba(212, 175, 55, 0.3);">
            <p style="margin: 0; color: #ffffff;">🟡 <b>[Paiement]</b> Paiement de 150,00 € validé (Facture <span class="mono-text">FACT-2026-0001</span>).</p>
        </div>
    """, unsafe_allow_html=True)

elif menu == "IA Juridique Avancée (Gratuit)":
    st.title("🤖 IA Juridique Avancée")
    st.markdown("Posez vos questions à notre assistant juridique intelligent (Accès illimité).")
    user_query = st.text_area("Exprimez votre situation juridique :", placeholder="Ex: Rédiger une clause de non-concurrence...")
    if st.button("Lancer l'analyse"):
        if user_query.strip():
            st.success("Analyse en cours par l'IA...")
            st.info("Module opérationnel - Simulation de traitement saphir active.")
        else:
            st.warning("Veuillez saisir une question.")

elif menu == "Rendez-vous Avocats":
    st.title("📅 Rendez-vous Avocats")
    st.markdown("Planifiez une consultation ciblée avec nos avocats partenaires.")
    col1, col2 = st.columns(2)
    with col1:
        st.selectbox("Spécialité recherchée", ["Droit du travail", "Droit des affaires", "Droit immobilier", "Droit de la famille"])
        st.date_input("Date souhaitée")
    with col2:
        st.selectbox("Avocat disponible", ["Me Claire Martin", "Me Thomas Leroy"])
        st.time_input("Heure souhaitée")
    st.button("Confirmer le rendez-vous")

elif menu == "Stockage sécurisé":
    st.title("🔒 Stockage sécurisé")
    st.markdown("Vos pièces justificatives chiffrées selon les normes AES-256 et eIDAS.")
    st.file_uploader("Téléverser un document sécurisé", type=["pdf", "png", "jpg"])

elif menu == "Génération de Courriers":
    st.title("✍️ Génération de Courriers & Actes")
    st.markdown("Rédigez vos actes juridiques instantanément.")
    st.selectbox("Type de courrier", ["Mise en demeure (Impayé)", "Contestation", "Rupture conventionnelle"])
    st.text_input("Nom / Destinataire")
    st.button("Générer le document")

elif menu == "Suivi des procédures":
    st.title("📈 Suivi des procédures")
    st.markdown("État d'avancement détaillé de vos dossiers en cours.")
    st.info("Aucune alerte critique sur vos dossiers actuels.")

elif menu == "Messagerie & Suivi":
    st.title("💬 Messagerie & Suivi")
    st.markdown("Échangez en toute sécurité avec vos conseils.")
    st.text_input("Écrire un message...")
    st.button("Envoyer")

elif menu == "Signature Électronique":
    st.title("✍️ Signature Électronique")
    st.markdown("Validez vos contrats et documents officiels à distance de manière sécurisée.")
    st.warning("Aucun document en attente de signature.")

elif menu == "Paiement et facturation":
    st.title("💳 Paiement et facturation")
    st.markdown("Retrouvez l'historique de vos transactions et réglez vos honoraires.")
    st.table([
        {"Facture": "FACT-2026-0001", "Montant": "150,00 €", "Statut": "Payé"},
        {"Facture": "FACT-2026-0002", "Montant": "75,00 €", "Statut": "En attente"}
    ])

elif menu == "Administrateur Back-Office":
    st.title("⚙️ Administrateur Back-Office")
    st.markdown("Panneau de contrôle global de la plateforme Juria.")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Utilisateurs inscrits", "1,240")
    with col2:
        st.metric("Requêtes IA traitées", "8,932")
    st.button("Lancer une maintenance globale")

# Horloge universelle (UTC) dans le coin inférieur droit de la fenêtre de l'application
st.markdown("---")
current_utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
st.markdown(f"<div style='text-align: right;'><span class='mono-text' style='font-size: 11px;'>UTC Time: {current_utc}</span></div>", unsafe_allow_html=True)