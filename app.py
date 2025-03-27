import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(layout="wide")
st.title("Simulador Interativo IS-LM 📈💰")

# Parâmetros iniciais
c0, c1 = 20, 0.8
i0, i1 = 50, 5
X, m0, m1 = 20, 30, 0.1
l0, l1 = 0.5, 10
P = 1
Y = np.linspace(100, 500, 400)

st.sidebar.header("🔧 Ajustes de Política")
G = st.sidebar.slider("Gastos do Governo (G)", 0, 150, 50, step=5)
T = st.sidebar.slider("Tributação (T)", 0, 150, 50, step=5)
M = st.sidebar.slider("Oferta Monetária (M)", 50, 200, 100, step=5)

def is_curve(Y, G_val, T_val):
    return (1 / i1) * (c0 + c1 * (Y - T_val) + i0 + G_val + X - (m0 + m1 * Y) - Y)

def lm_curve(Y, M_val, P_val):
    return (M_val / P_val - l0 * Y) / (-l1)

r_IS = is_curve(Y, G, T)
r_LM = lm_curve(Y, M, P)

fig = go.Figure()
fig.add_trace(go.Scatter(x=Y, y=r_IS, name='Curva IS', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=Y, y=r_LM, name='Curva LM', line=dict(color='red')))
fig.update_layout(title='Modelo IS-LM: Análise de Políticas Econômicas',
                  xaxis_title='Y (Renda)',
                  yaxis_title='r (Taxa de Juros)',
                  height=600)

st.plotly_chart(fig, use_container_width=True)

st.markdown("📚 **Descrição:** Este simulador mostra o impacto de mudanças na política fiscal (G, T) e monetária (M) sobre as curvas IS e LM. Use os sliders à esquerda para ver como o equilíbrio macroeconômico se altera.")
