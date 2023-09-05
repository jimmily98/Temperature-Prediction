import streamlit as st
from PIL import Image


st.markdown("<h1 style='text-align: center;'>Power Calculator</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: left;'>Introduction</h3>", unsafe_allow_html=True)
st.markdown("Le logiciel développé a pour objectif de calculer la puissance requise \
            par la machine frigorifique en fonction des paramètres spécifiques de la caisse\
             et des conditions de température. Les principes de ces calculs sont détaillés\
             dans la sous-page intitulée \"Home\".")
st.markdown("<h4 style='text-align: left;'>Remarque</h4>", unsafe_allow_html=True)
st.markdown('Jusqu\'à présent, le modèle n\'a pas complètement résolu le problème, car la puissance calculée diffère considérablement de la puissance réelle. Certains des calculs et des mesures sont énumérés dans le tableau ci-dessous.')
image1 = Image.open('tab_1.PNG')
st.image(image1, caption='Comparaison : puissance calculée et mesurée', use_column_width=True)
st.markdown('Nous pouvons constater deux différences :')
st.markdown('1. Au niveau des deux températures, \
            la puissance réelle mesurée est nettement supérieure à la puissance calculée')
st.markdown('2. Dans la puissance mesurée, \
            la puissance du congélateur diminue à mesure que la température diminue, \
            ce qui est conforme à la loi des moteurs thermiques. \
            En revanche, dans la puissance calculée, \
            la puissance du congélateur augmente lorsque la température diminue, \
            ce qui n\'est pas conforme à la loi des moteurs thermiques.')
st.markdown('Une telle divergence peut être due aux raisons suivantes :')
st.markdown('1. la valeur de K est surestimée dans le calcul et la chaleur dissipée par les parois est supérieure à la valeur réelle.')
st.markdown('2. l\'effet de la convection n\'est pas pris en compte et la puissance totale calculée est faible.')