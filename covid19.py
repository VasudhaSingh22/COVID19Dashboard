import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
st.set_page_config(layout = 'wide', page_title= 'COVID-19 Data')

@st.cache(persist = True)
def load_data(file):
    df = pd.read_csv(file)
    return df

def get_total_dataframe(dataset):
    total_df = pd.DataFrame({
        'Status':['Confirmed', 'Active', 'Recovered', 'Deaths'],
        'Number of Cases': (dataset.iloc[0]['Confirmed'], dataset.iloc[0]['Active'], dataset.iloc[0]['Recovered'], dataset.iloc[0]['Deaths'])})
    return total_df

data = load_data('state_wise.csv')
st.title('🦠 State Wise Impact of COVID-19 in India')
st.sidebar.title('Select the Parameters to analyze the Impact of COVID-19 throughout various States:')
chart = st.sidebar.selectbox('Select the Type of Chart: ', ('Bar Chart', 'Pie Chart', 'Line Chart'))
if chart == 'Bar Chart':
    c1, c2, c3 = st.columns(3)
    with c1:
        data = data.loc[data['State'] != 'State Unassigned']
        select = st.sidebar.selectbox('Select a State: ', data['State'])
        state_data = data[data['State'] == select]
        state_total = get_total_dataframe(state_data)
        state_total_graph = px.bar(state_total, x = 'Status', y = 'Number of Cases', labels={'Number of Cases':'Number of Cases in %s' %(select)}, color = 'Status')
        state_total_graph.update_xaxes(showline=True, linewidth=2, linecolor='black')
        state_total_graph.update_yaxes(showline=True, linewidth=2, linecolor='black')
        st.plotly_chart(state_total_graph)
    with c3:
        st.write('Number of Cases in {}:'.format(select))
        st.dataframe(state_total)
elif chart == 'Pie Chart':
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        data = data.loc[data['State'] != 'State Unassigned']
        select = st.sidebar.selectbox('Select a State: ', data['State'])
        state_data = data[data['State'] == select]
        state_total = get_total_dataframe(state_data)
        labels = state_total['Status']
        values = state_total['Number of Cases']
        fig = go.Figure(data = [go.Pie(labels = labels, values = values, texttemplate = ([f"{v}" for v in values]))])
        st.plotly_chart(fig)
    with c4:
        st.write('Number of Cases in {}:'.format(select))
        st.dataframe(state_total)
else:
    select_status = st.sidebar.radio("COVID-19 Patient's Status: ", ('Confirmed Cases', 'Active Cases', 'Recovered Cases', 'Deceased Cases'))
    c1, c2, c3 = st.columns(3)
    if select_status == 'Confirmed Cases':
        with c1:
            st.markdown('### Total Confirmed Cases Among States: ')
            data = data.loc[(data['State'] != 'Total') & (data['State'] != 'State Unassigned')]
            fig = px.line(data, x = 'State', y = 'Confirmed')
            st.plotly_chart(fig)
        with c3:
            df = pd.DataFrame({
                'States': data['State'],
                'Confirmed Cases': data['Confirmed']
            })
            st.dataframe(df)
    elif select_status == 'Active Cases':
        with c1:
            st.markdown('### Total Active Cases Among States: ')
            data = data.loc[(data['State'] != 'Total') & (data['State'] != 'State Unassigned')]
            fig = px.line(data, x = 'State', y = 'Active')
            st.plotly_chart(fig)
        with c3:
            df = pd.DataFrame({
                'States': data['State'],
                'Active Cases': data['Active']
            })
            st.dataframe(df)
    elif select_status == 'Recovered Cases':
        with c1:
            st.markdown('### Total Recovered Cases Among States: ')
            data = data.loc[(data['State'] != 'Total') & (data['State'] != 'State Unassigned')]
            fig = px.line(data, x = 'State', y = 'Recovered')
            st.plotly_chart(fig)
        with c3:
            df = pd.DataFrame({
                'States': data['State'],
                'Recovered Cases': data['Recovered']
            })
            st.dataframe(df)
    else:
        with c1:
            st.markdown('### Total Deceased Cases Among States: ')
            data = data.loc[(data['State'] != 'Total') & (data['State'] != 'State Unassigned')]
            fig = px.line(data, x = 'State', y = 'Deaths')
            st.plotly_chart(fig)
        with c3:
            df = pd.DataFrame({
                'States': data['State'],
                'Deceased Cases': data['Deaths']
            })
            st.dataframe(df) 