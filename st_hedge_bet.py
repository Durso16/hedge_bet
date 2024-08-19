# -*- coding: utf-8 -*-
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title and introduction
st.title("Hedge Bet Simulator")
st.write("This app allows you to simulate hedge bets and visualize the results.")

# Sidebar for user inputs
with st.sidebar:
    aposta_a = st.slider('Aposta Time A ($)', min_value=1.0, max_value=200.0, value=100.0, step=1.0)
    odd_a = st.number_input('Odd Time A', min_value=1.0, value=1.5, step=0.01)
    aposta_b = st.slider('Aposta Time B ($)', min_value=1.0, max_value=200.0, value=100.0, step=1.0)
    odd_b = st.number_input('Odd Time B', min_value=1.0, value=2.5, step=0.01)

# Calculating potential profits
profit_a = aposta_a * (odd_a - 1) - aposta_b
profit_b = aposta_b * (odd_b - 1) - aposta_a

# Display the results
st.write("## Resultados:")
st.write(f"**Lucro se o Time A ganhar:** ${profit_a:.2f}")
st.write(f"**Lucro se o Time B ganhar:** ${profit_b:.2f}")

# Plot the profits
st.write("## Gráfico dos lucros potenciais")
fig, ax = plt.subplots()
teams = ['Time A', 'Time B']
profits = [profit_a, profit_b]
ax.bar(teams, profits, color=['blue', 'red'])
ax.set_ylabel('Lucro ($)')
ax.set_title('Lucro Potencial por Resultado')
st.pyplot(fig)

# Display additional information
st.write("Ajuste as apostas e odds na barra lateral para ver os efeitos nos lucros potenciais.")
