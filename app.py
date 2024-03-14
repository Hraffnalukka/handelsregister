import streamlit as st
from handelsregister import HandelsRegister
import argparse

# Titel der App
st.title('Handelsregister Suche')

# Definition der Suchfunktion


def search_company(schlagwoerter='uniper', schlagwortOptionen=2, ergebnisseProSeite=100, debug=False):
    args = argparse.Namespace(
        debug=False, force=False, schlagwoerter=schlagwoerter, schlagwortOptionen=2)

    h = HandelsRegister(args)
    h.open_startpage()
    companies = h.search_company()
    return companies


# Button für die Suche
if st.button('Search for Uniper'):
    with st.spinner('Searching...'):
        companies = search_company(debug=True)
        if companies and len(companies) > 0:
            # Hinzufügen von enumerate für einen Index
            # Verwende `enumerate` für den Index
            # Verwende `enumerate` für den Index
            st.text(f"Found {len(companies)} companies")
            for index, company in enumerate(companies):
                with st.container():  # Nutze einen Container für jedes Unternehmen
                    st.subheader(f"Company: {company['name']}")
                    st.text(f"Court: {company['court']}")
                    st.text(f"State: {company['state']}")
                    st.text(f"Status: {company['status']}")

                    # Verwende einen Expander für die Dokumente
                    with st.expander("Documents"):
                        documents_formatted = company['documents'].replace("Current", "\n- Current").replace("Chronological", "\n- Chronological").replace("Historical", "\n- Historical").replace(
                            "Document", "\n- Document").replace("Entity", "\n- Entity").replace("Publications", "\n- Publications").replace("Structured", "\n- Structured")
                        # Hier nutzen wir st.markdown oder st.text, um die formatierten Dokumente anzuzeigen
                        st.markdown(documents_formatted)

                    with st.expander("History"):
                        for item in company['history']:
                            st.text(f"{item[0]}, {item[1]}")
                    # Fügt eine Trennlinie zwischen Unternehmen ein
                    st.markdown("---")
        else:
            st.error('No companies found.')
