import streamlit as st

st.set_page_config(page_title="Geospatial Analysis of Hospitals in Peru", layout="wide")

tab1, tab2, tab3 = st.tabs(["Data Desctription", "Static Maps & Department Analysis", "Dynamic Maps"])

with tab1:

     st.markdown(
"""
# Data Desctription
The purpose of this application is to present a geospatial analysis of hospitals in Peru, both at the departmental level and at the population center level. Through this visualization, we aim to identify patterns in their geographic distribution as well as potential gaps in access to healthcare services.

Our code is hosted in the following GithHub repository: https://github.com/
"""
     )

with tab2:
     st.markdown("### Static Maps & Department Analysis")
    
     import streamlit as st
     import matplotlib.pyplot as plt
     import seaborn as sns
     import pandas as pd

     st.subheader("Distribution of hospitals across departments")
     # Leer el DataFrame desde la carpeta data/
     summary_table = pd.read_csv("data/summary_table.csv")
     # Mostrar en tabla interactiva
     st.dataframe(summary_table)

with tab3:
    st.markdown("### Dynamic Maps")
