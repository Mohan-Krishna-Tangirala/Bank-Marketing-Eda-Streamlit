import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

st.set_page_config(page_title="EDA - Bank Marketing", layout="wide")
st.title('Interactive Data Explorer')


st.markdown(
    """
    <style>
    .stApp {
        max-width: 1200px; /* Increase the maximum width of the app */
        margin: auto;      /* Center align the app */
    }
    .chart-container {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)


with st.expander("About this app"):
    st.markdown("**What can this app do?**")
    st.info("This app presents the results of the Exploratory Data Analysis (EDA) performed on the Bank Marketing dataset ")


df1 = pd.read_csv("eda-bank-marketing.csv")
df1.drop(columns="contact", axis=1, inplace=True)
df1_cleaned = df1.loc[:, ~df1.columns.str.contains('^Unnamed')]



response_counts = df1['response'].value_counts(normalize=True).reset_index()
response_counts.columns = ['response', 'percentage']

pie_chart = alt.Chart(response_counts).mark_arc().encode(
    theta=alt.Theta(field="percentage", type="quantitative", stack=True),
    color=alt.Color(field="response", type="nominal"),
    tooltip=['response', 'percentage:Q']
).properties(
    width=300,
    height=300,
    title='Response'
)

avg_response = df1.groupby("marital", as_index=False)["response_flag"].mean()

bar_chart = alt.Chart(avg_response).mark_bar().encode(
    x=alt.X('marital:N', title='Marital Status', sort='-y'),
    y=alt.Y('response_flag:Q', title='Average Response'),
    color=alt.Color('marital:N', legend=None),
    tooltip=['marital', 'response_flag']
).properties(
    width=500,  
    height=300,
    title='Average Response by Marital Status'
)

balance_box_plot = alt.Chart(df1).mark_boxplot().encode(
    x=alt.X('response:N', title='Response'),
    y=alt.Y('balance:Q', title='Balance'),
    color='response:N'
).properties(
    width=300,
    height=300,
    title='Box Plot of Balance by Response'
)

salary_box_plot = alt.Chart(df1).mark_boxplot().encode(
    x=alt.X('response:N', title='Response'),
    y=alt.Y('salary:Q', title='Salary'),
    color='response:N'
).properties(
    width=300,
    height=300,
    title='Box Plot of Salary by Response'
)


col1, col2 = st.columns(2)
with col1:
    st.altair_chart(pie_chart, use_container_width=True)
with col2:
    st.altair_chart(bar_chart, use_container_width=True)


col3, col4 = st.columns(2)
with col3:
    st.altair_chart(balance_box_plot, use_container_width=True)
with col4:
    st.altair_chart(salary_box_plot, use_container_width=True)



st.write('Sample of DataFrame')
st.dataframe(df1_cleaned.head(30))
