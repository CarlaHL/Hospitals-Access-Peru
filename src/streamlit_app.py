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

     #Título
     st.title("Hospitals by Department")

     # Aquí asumo que summary_table ya está definido
     fig, ax = plt.subplots(figsize=(12, 6))
     sns.barplot(
     data=summary_table,
     x="Departamento",
     y="n_hospitals_dept",
     ax=ax,
     color="steelblue"
     )
     plt.xticks(rotation=90)
     ax.set_title("Distribution of hospitals across departments")

# Mostrar en Streamlit
st.pyplot(fig)


with tab3:
    st.markdown"Dynamic Maps")
