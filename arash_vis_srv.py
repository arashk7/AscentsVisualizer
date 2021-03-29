import streamlit as st
import streamlit.components.v1 as components



def init():
    components.iframe("http://localhost:56367" , height=500)

selected_box = st.sidebar.selectbox(
    'Choose one of the items:',
    ('Vis 2D','Vis 3D')
)


if selected_box == 'Vis 2D':
    init()