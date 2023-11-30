import streamlit as st
import random
from sistema import recommendK
from dataset import users
from style import page_style
 
movies_to_rate = random.sample(list(users['Usuario1'].keys()), 5)

def recommend_app():
    st.markdown(page_style, unsafe_allow_html=True)

    st.title("Sistema de Recomendação Colaborativo de Filmes Natalinos")

    st.write(f"Desenvolvido por: Larry Amaral Reis e Sarah Portela Salehi")

    st.divider()

    name_input_placeholder = st.empty()

    username = name_input_placeholder.text_input("Digite seu nome:")

    if username:
        name_input_placeholder.empty()

        st.write(f"Olá, {username}! Informe suas avaliações para os filmes:")

        new_user_ratings = {}
        for movie in movies_to_rate:
            has_watched = st.checkbox(f"Você assistiu {movie}?")
            if has_watched:
                rating = st.slider(f"Avaliação para {movie} (de 0 a 5):", 0.0, 5.0, 0.0, step=0.5)
                new_user_ratings[movie] = rating
        st.divider()
        if st.button("Recomendar Filmes"):
            recommendations = recommendK(new_user_ratings, users, 5, 3)
            st.write(f"Avaliações registradas, {username}. Calculando recomendações...")

            if recommendations:
                st.write(f"Recomendações para {username}:")
                for recommendation in recommendations:
                    st.write(f"{recommendation[0]}")
            else:
                st.write("Desculpe, não conseguimos fazer uma recomendação neste momento.")
