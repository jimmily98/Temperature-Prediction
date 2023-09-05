import streamlit as st

st.markdown("<h1 style='text-align: center;'>Data and Parameters</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Remarque</h1>", unsafe_allow_html=True)
st.markdown('Jusqu\'à présent, le modèle n\'a pas complètement résolu le problème, car la puissance calculée diffère considérablement de la puissance réelle. Certains des calculs et des mesures sont énumérés dans le tableau ci-dessous.')
st.markdown('Nous pouvons constater deux différences :')
st.markdown('1. aux deux températures, \
            la puissance réelle mesurée est nettement supérieure à la puissance calculée')
st.markdown('2. dans la puissance mesurée, \
            la puissance du congélateur diminue à mesure que la température diminue, \
            ce qui est conforme à la loi des moteurs thermiques. \
            En revanche, dans la puissance calculée, \
            la puissance du congélateur augmente lorsque la température diminue, \
            ce qui n\'est pas conforme à la loi des moteurs thermiques.')
st.markdown('Une telle divergence peut être due aux raisons suivantes :')
st.markdown('1. la valeur de K est surestimée dans le calcul et la chaleur dissipée par les parois est supérieure à la valeur réelle.')
st.markdown('2. l\'effet de la convection n\'est pas pris en compte et la puissance totale calculée est faible.')