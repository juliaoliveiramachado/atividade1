import streamlit as st
import pandas as pd
import csv
st.title('Atividade de Programação')
st.caption('Julia Oliveira Machado')

df = pd.read_csv('paises.csv', sep =';')
st.dataframe(df)


#arquivo = open('paises.csv)
#for linha in arquivo:
#    st.write(linha)
