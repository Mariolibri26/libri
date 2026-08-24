import streamlit as st  # La libreria magica per il web
import pandas as pd     # Una libreria potentissima per leggere i CSV in un secondo

# 1. Impostazioni della pagina per lo schermo del telefono
st.set_page_config(page_title="I Miei Libri", page_icon="📚", layout="centered")

st.title("📚 Il Mio Archivio Libri")
st.write("Consulta il tuo catalogo in tempo reale")

# 2. Caricamento automatico del tuo file libri.csv
try:
    # Pandas legge il CSV e capisce da solo le colonne e il punto e virgola
    df = pd.read_csv("libri.csv", sep=";", encoding="utf-8", on_bad_lines="skip")
    
    # 3. Creazione della barra di ricerca (bellissima e gigante sullo schermo del telefono)
    ricerca = st.text_input("🔍 Digita il Titolo, Personaggio o Editore:")

    if ricerca:
        # Trasforma tutto in minuscolo per non fare differenze con le maiuscole
        ricerca_lower = ricerca.lower()
        
        # Filtra tutte le righe del database in un colpo solo
        risultati = df[
            df['Titolo'].str.lower().str.contains(ricerca_lower, na=False) |
            df['Personaggi'].str.lower().str.contains(ricerca_lower, na=False) |
            df['Editore'].str.lower().str.contains(ricerca_lower, na=False)
        ]
        
        # Se trova qualcosa, mostra i libri trovati sotto forma di "schede" pulite
        if not risultati.empty:
            st.success(f"Trovati {len(risultati)} riscontri in archivio:")
            for indice, riga in risultati.iterrows():
                # Crea un box visivo per ogni libro
                with st.container():
                    st.subheader(f"📖 {riga['Titolo']}")
                    st.write(f"**Personaggi:** {riga['Personaggi']}")
                    st.write(f"**Editore:** {riga['Editore']} | **Anno:** {riga['Anno di pubblicazione']}")
                    st.write(f"**In Biblioteca:** {riga['Biblioteca']}")
                    st.markdown("---")
        else:
            st.warning("❌ Questo libro non è in archivio. Puoi comprarlo!")
    else:
        # Se la barra è vuota, mostra quanti libri hai in totale
        st.info(f"In totale hai {len(df)} libri registrati in archivio.")

except Exception as e:
    st.error(f"Assicurati che il file 'libri.csv' sia nella stessa cartella: {e}")
