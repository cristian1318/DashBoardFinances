import streamlit as st
import pandas as pd
import numpy as np

# Título de la aplicación
st.title("Finanzas Personales Camandre")

# Entrada de ingresos y gastos
tipo = st.selectbox("Tipo de transacción", ["Ingreso", "Gasto"])
monto = st.number_input("Monto", min_value=0.0, step=0.1)
categoria = st.text_input("Categoría")
fecha = st.date_input("Fecha")

# Botón para guardar la transacción
if st.button("Guardar"):
    st.success(f"Transacción registrada: {tipo} - {monto} en {categoria}")

# Visualización de datos (puedes usar un DataFrame)
st.header("Resumen")
df = pd.DataFrame({
    "Fecha": ["2024-12-30"],
    "Tipo": ["Ingreso"],
    "Monto": [1000.0],
    "Categoría": ["Sueldo"]
})
st.table(df)
