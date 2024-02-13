import streamlit as st

# Função para definir o estilo da aplicação
def set_app_style(page_name):
    common_style = """
        /* Estilo para a aplicação como um todo */
        .stApp {
            font-family: 'Comic Sans MS', cursive;
            color: #ffffff;
            font-size: 24px;
        }

        /* Estilo para centralizar o título */
        .st-emotion-cache-k7vsyb h1 {
            text-align: center;
            background-color: rgba(0, 0, 0, 0.5);
            padding: 10px;
            border-radius: 15px;
        }

        /* Estilo para a caixa de input flutuante do chat */
        .stChatFloatingInputContainer {
            background-color: rgba(255, 255, 255, 0.0);
            color: #000000;
        }
        .stChatFloatingInputContainer input {
            color: #000000;
            background-color: rgba(255, 255, 255, 0.5);
            border-radius: 12px;
            padding: 14px;
            font-weight: bold;
        }

        /* Estilo para os botões */
        .stButton {
            border-radius: 15px;
            padding: 12px 24px;
            font-weight: bold;
        }

        /* Estilo para caixa de seleção e área de texto */
        .stSelectbox, .stTextArea {
            background-color: rgba(255, 255, 255, 0.0);
            color: #000000;
            border-radius: 12px;
            padding: 14px;
        }

        /* Estilo para um elemento específico com classe .st-emotion-cache-janbn0 */
        .st-emotion-cache-janbn0 {
            display: flex;
            align-items: flex-start;
            gap: 0.5rem;
            padding: 1rem;
            border-radius: 0.5rem;
            background-color: rgb(5 9 33 / 71%);
        }

        .st-emotion-cache-4oy321 {
            display: flex;
            align-items: flex-start;
            gap: 0.5rem;
            padding: 1rem;
            border-radius: 0.5rem;
            background-color: rgb(5 9 33 / 71%);
        }

        /* BORDA LATERAL */
        .st-emotion-cache-1cypcdb {
            background-image: url(https://i.makeagif.com/media/12-21-2022/7_wykY.gif);
            background-size: cover;
            width: 259px
            }
    """

    specific_style = ""
    if page_name == "Conversar com Chatbot":
        specific_style = """
            /* Estilo específico para a Página 1 */
            .stApp {
                background-image: url(https://i.pinimg.com/originals/29/28/7d/29287dbe2273424039448da43132f59b.gif);
                background-size: cover;
                background-repeat: no-repeat;
                background-color: #20232a;
            }
            /* Estilo específico para os botões da Página 1 */
            .stButton {
                background-color: #ff4081;
                color: #ffffff;
            }
            .stButton:hover {
                background-color: #d81b60;
            }
        """
    elif page_name == "Add Vectorstore":
        specific_style = """
            /* Estilo específico para a Página 2 */
            .stApp {
                background-image: url(https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/7151b11e-2fcc-4b3f-86fa-2ccf2e67512a/dggaoc8-ad05a10a-cf70-4f17-87af-2ffeeeaf6ba7.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzcxNTFiMTFlLTJmY2MtNGIzZi04NmZhLTJjY2YyZTY3NTEyYVwvZGdnYW9jOC1hZDA1YTEwYS1jZjcwLTRmMTctODdhZi0yZmZlZWVhZjZiYTcuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.0qdcjKthfl33339x5-JMMtYbJ2QFzSj14F-ZFlyWwGE);
                background-size: cover;
                background-repeat: no-repeat;
                background-color: #1a1a1a;
            }
            /* Estilo específico para os botões da Página 2 */
            .stButton {
                background-color: #007bff;
                color: #ffffff;
            }
            .stButton:hover {
                background-color: #0056b3;
            }
        """
    elif page_name == "Desenvolvimento":
        specific_style = """
            /* Estilo específico para a Página 3 */
            .stApp {
                background-image: url(https://i.pinimg.com/originals/63/24/3a/63243aacfe563f25e472f9e187723df1.gif);
                background-size: cover;
                background-repeat: no-repeat;
                background-color: #0f4d75;
            }
            /* Estilo específico para os botões da Página 3 */
            .stButton {
                background-color: #28a745;
                color: #ffffff;
            }
            .stButton:hover {
                background-color: #218838;
            }
        """

    st.markdown(f"<style>{common_style}{specific_style}</style>", unsafe_allow_html=True)
