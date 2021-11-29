import streamlit as st
import pandas as pd
import cufflinks as cf
import datetime
import plotly.express as px
from application_service.BuildingComponents import StreamlitComponent

#### SIDEBAR

# Sidebar title
st.sidebar.markdown('''
# Electricity Load Data Demo
Showing electricity usage by area-time slice in NY State
''')
st.write('---')

# Sidebar filters
st.sidebar.subheader('Query parameters')
aggregation = st.sidebar.selectbox("Aggregation", ['daily', 'hourly', 'weekly', 'monthly', 'yearly'])
start_date = st.sidebar.date_input("Start date", datetime.date(2021, 1, 1))
end_date = st.sidebar.date_input("End date", datetime.date(2021, 4, 13))
ny_areas = ['CAPITL', 'CENTRL', 'DUNWOD', 'GENESE', 'H Q', 'HUD VL', 'LONGIL', 'MHK VL', 'MILLWD', 'N.Y.C.', 'NORTH', 'NPX', 'O H', 'PJM', 'WEST']
selected_areas = st.sidebar.multiselect("Select part of NY State", ny_areas)

if not selected_areas: selected_areas = ["N.Y.C."]

#### BODY

# App Title
st.title('''
Electricity demand by {}
For areas: {}
'''.format(aggregation, ', '.join([i for i in selected_areas])))
st.write('---')

# Show data
@st.cache(suppress_st_warning=True, show_spinner=False, allow_output_mutation=True)
def load_fig(start_date, end_date, ny_areas, aggregation):
    fig = StreamlitComponent.plot_line_chart(start_date, end_date, ny_areas, aggregation)
    return fig

fig = load_fig(start_date, end_date, selected_areas, aggregation)
st.header('**Energy Demand Trend**')
st.plotly_chart(fig)
