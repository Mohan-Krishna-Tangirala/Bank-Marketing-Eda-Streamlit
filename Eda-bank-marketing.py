import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

st.set_page_config(page_title="EDA - Bank Marketing")
st.title('Interactive Data Explorer')

with st.expander("About this app"):
    st.markdown("**What can this app do?**")
    st.info("This app presents the results of the Exploratory Data Analysis (EDA) performed on the Bank Marketing dataset ")
    


df1 = pd.read_csv("eda-bank-marketing.csv")


st.write('Sample of DataFrame')
df1.drop(columns = "contact", axis = 1, inplace = True)
df1_cleaned = df1.loc[:, ~df1.columns.str.contains('^Unnamed')]
st.dataframe(df1_cleaned.head(30))


# Altair pie chart

response_counts = df1['response'].value_counts(normalize=True).reset_index()
response_counts.columns = ['response', 'percentage']

pie_chart = alt.Chart(response_counts).mark_arc().encode(
    theta=alt.Theta(field="percentage", type="quantitative", stack=True),
    color=alt.Color(field="response", type="nominal"),
    tooltip=['response', 'percentage:Q']
).properties(
    width=400,
    height=400,
    title='Response'
)

pie_chart


avg_response = df1.groupby("marital", as_index=False)["response_flag"].mean()

# Altair bar chart
bar_chart = alt.Chart(avg_response).mark_bar().encode(
    x=alt.X('marital:N', title='Marital Status', sort='-y'),
    y=alt.Y('response_flag:Q', title='Average Response'),
    color=alt.Color('marital:N', legend=None),  # Add color based on marital status
    tooltip=['marital', 'response_flag']
).properties(
    width=400,
    height=300,
    title='Average Response by Marital Status'
)

bar_chart

box_plot = alt.Chart(df1).mark_boxplot().encode(
    x=alt.X('response:N', title='Response'),
    y=alt.Y('balance:Q', title='Balance'),
    color='response:N'
).properties(
    width=400,
    height=300,
    title='Box Plot of Balance by Response'
)

box_plot

box_plot = alt.Chart(df1).mark_boxplot().encode(
    x=alt.X('response:N', title='Response'),
    y=alt.Y('salary:Q', title='Salary'),
    color='response:N'
).properties(
    width=400,
    height=300,
    title='Box Plot of Salary by Response'
)

box_plot






