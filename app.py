import streamlit as st

#inicialiacao das variaveis de estado
st.titlo("Sistema de cadastro")
if "pagina" not in st.session_state:
    st.session_state.pagina = "menu"
#tela de menu 

if st .session_state.pagina == "menu":
    st .title("Menu principal")
    st write("escolha uma opcao: ")
#tela de cadastro
#tela de login

