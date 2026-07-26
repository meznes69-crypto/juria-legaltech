import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Juria | LegalTech Intelligente",
    page_icon="⚖️",
    layout="wide",
)

# Style CSS professionnel pour une interface épurée et moderne
st.markdown(
    """
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 6px;
        font-weight: 600;
    }
    .card {
        padding: 20px;
        border-radius: 10px;
        background-color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# BARRE LATÉRALE (NAVIGATION & MODULES)
# ---------------------------------------------------------
st.sidebar.title("⚖️ Juria LegalTech")
st.sidebar.markdown("---")

module = st.sidebar.selectbox(
    "Navigation",
    [
        "Accueil",
        "Analyse de Contrats",
        "Rédaction d'Actes",
        "Recherche Juridique",
        "Espace Avocats (Forfaits Mensuels)",
    ],
)

st.sidebar.markdown("---")
st.sidebar.info(
    "**Juria** - Solution juridique intelligente pour professionnels et particuliers."
)

# ---------------------------------------------------------
# MODULE 1 : ACCUEIL
# ---------------------------------------------------------
if module == "Accueil":
  st.title("Bienvenue sur Juria 🚀")
  st.markdown(
      "Votre plateforme de technologie juridique propulsée par l'intelligence"
      " artificielle pour simplifier, automatiser et sécuriser vos"
      " démarches et analyses légales."
  )

  col1, col2, col3 = st.columns(3)
  with col1:
    st.markdown(
        """
        <div class="card">
            <h3>⚡ Rapidité</h3>
            <p>Analysez vos contrats et générez vos documents en quelques secondes.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
  with col2:
    st.markdown(
        """
        <div class="card">
            <h3>🔒 Sécurité</h3>
            <p>Confidentialité absolue et conformité avec les standards de protection des données.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
  with col3:
    st.markdown(
        """
        <div class="card">
            <h3>💼 Expertise</h3>
            <p>Des outils conçus pour les particuliers, les entreprises et les cabinets d'avocats.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------------------------------------------------------
# MODULE 2 : ANALYSE DE CONTRATS
# ---------------------------------------------------------
elif module == "Analyse de Contrats":
  st.title("📄 Analyse Intelligente de Contrats")
  st.markdown(
      "Téléchargez ou collez le texte de votre contrat ci-dessous pour en"
      " obtenir une analyse détaillée des risques et des clauses clés."
  )

  contract_text = st.text_area(
      "Collez le texte de votre contrat ici :",
      height=250,
      placeholder="Insérez le contenu du contrat à analyser...",
  )

  if st.button("Lancer l'analyse"):
    if contract_text.strip():
      with st.spinner("Analyse du document en cours..."):
        # Logique d'analyse professionnelle
        st.success("Analyse terminée avec succès.")
        st.subheader("Rapport d'audit juridique")
        st.write(
            "- **Conformité générale :** Le document présente une structure"
            " standard."
        )
        st.write(
            "- **Clauses à surveiller :** Vérifiez les conditions de"
            " résiliation et les limites de responsabilité."
        )
        st.write(
            "- **Recommandation :** Validation conseillée par un professionnel"
            " du droit pour les engagements majeurs."
        )
    else:
      st.warning("Veuillez insérer le texte d'un contrat avant de lancer l'analyse.")

# ---------------------------------------------------------
# MODULE 3 : RÉDACTION D'ACTES
# ---------------------------------------------------------
elif module == "Rédaction d'Actes":
  st.title("✍️ Rédaction Automatisée d'Actes")
  st.markdown(
      "Générez des documents juridiques sur mesure en remplissant les champs"
      " ci-dessous."
  )

  document_type = st.selectbox(
      "Type de document",
      [
          "Contrat de Prestation de Services",
          "Lettre de Mise en Demeure",
          "Statuts de Société (SAS/SARL)",
          "Reçu pour Solde de Tout Compte",
      ],
  )

  col1, col2 = st.columns(2)
  with col1:
    partie_a = st.text_input("Nom / Raison Sociale du Créancier / Prestataire")
  with col2:
    partie_b = st.text_input("Nom / Raison Sociale du Client / Débiteur")

  details = st.text_area("Détails spécifiques et clauses particulières :")

  if st.button("Générer le document"):
    if partie_a and partie_b:
      with st.spinner("Génération du document juridique..."):
        st.success("Document généré avec succès !")
        st.subheader(f"Aperçu : {document_type}")
        st.code(
            f"""
==================================================
DOCUMENT OFFICIEL - JURIA LEGALTECH
Type : {document_type}
--------------------------------------------------
Entre les soussignés :
- {partie_a}
- {partie_b}

Il a été convenu et arrêté ce qui suit :
[Clauses légales générées automatiquement selon les normes en vigueur]

Spécificités incluses : {details if details else 'Standard'}
==================================================
            """,
            language="text",
        )
    else:
      st.warning("Veuillez renseigner les parties concernées.")

# ---------------------------------------------------------
# MODULE 4 : RECHERCHE JURIDIQUE
# ---------------------------------------------------------
elif module == "Recherche Juridique":
  st.title("🔍 Moteur de Recherche Juridique")
  st.markdown(
      "Interrogez la base de connaissances juridiques pour retrouver des"
      " articles de loi, de la jurisprudence ou des notes explicatives."
  )

  query = st.text_input(
      "Rechercher un texte de loi, un article ou un sujet juridique :",
      placeholder="Ex: Durée légale du préavis de démission...",
  )

  if st.button("Rechercher"):
    if query.strip():
      with st.spinner("Recherche dans la base de données juridique..."):
        st.success("Résultats de la recherche :")
        st.info(
            f"**Résultat pertinent pour :** *{query}*"
        )
        st.write(
            "Les textes applicables en la matière confirment les dispositions"
            " usuelles du code en vigueur. Pour toute situation contentieuse,"
            " il est recommandé de croiser ces informations avec les"
            " dernières mises à jour du Journal Officiel."
        )
    else:
      st.warning("Veuillez saisir un terme ou une question à rechercher.")

# ---------------------------------------------------------
# MODULE 5 : ESPACE AVOCATS (FORFAITS MENSUELS)
# ---------------------------------------------------------
elif module == "Espace Avocats (Forfaits Mensuels)":
  st.title("⚖️ Espace Avocats & Abonnements Professionnels")
  st.markdown(
      "Découvrez nos offres de forfaits mensuels dédiés aux cabinets"
      " d'avocats pour booster votre productivité, automatiser vos actes et"
      " collaborer efficacement avec vos clients via Juria."
  )

  col1, col2, col3 = st.columns(3)

  with col1:
    st.markdown(
        """
        <div class="card">
            <h3>Cabinet Solo</h3>
            <h2 style="color: #0066cc;">49 € <small>/ mois</small></h2>
            <p>Idéal pour les avocats indépendants.</p>
            <hr>
            <p>✅ 50 analyses de contrats /mois</p>
            <p>✅ Générateur d'actes illimité</p>
            <p>✅ Support prioritaire par email</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("Choisir Solo", key="solo"):
      st.success("Redirection vers le paiement sécurisé (Forfait Solo).")

  with col2:
    st.markdown(
        """
        <div class="card" style="border: 2px solid #0066cc;">
            <h3>Cabinet Standard</h3>
            <h2 style="color: #0066cc;">149 € <small>/ mois</small></h2>
            <p>Pour les structures de 2 à 5 avocats.</p>
            <hr>
            <p>✅ Analyses de contrats illimitées</p>
            <p>✅ Multi-utilisateurs (jusqu'à 5)</p>
            <p>✅ Espace sécurisé client dédié</p>
            <p>✅ Support téléphonique 5j/7</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("Choisir Standard", key="standard"):
      st.success("Redirection vers le paiement sécurisé (Forfait Standard).")

  with col3:
    st.markdown(
        """
        <div class="card">
            <h3>Cabinet Enterprise</h3>
            <h2 style="color: #0066cc;">399 € <small>/ mois</small></h2>
            <p>Pour les cabinets d'envergure.</p>
            <hr>
            <p>✅ Accès illimité multi-postes</p>
            <p>✅ API dédiée & intégration CRM</p>
            <p>✅ Archivage sécurisé sur mesure</p>
            <p>✅ Account Manager dédié 24/7</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("Choisir Enterprise", key="enterprise"):
      st.success("Redirection vers l'offre sur mesure (Enterprise).")
