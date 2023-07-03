# import packages
import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np
np.bool = np.bool_

# set the page details
st.set_page_config(
    page_title="Financial Inclusion in Africa",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# set the title of the page
st.title("Financial Inclusion in Africa")

# load the dataset
df = pd.read_csv("financial_inclusion.csv")

# split the first row into 4 columns
select1, select2, select3, select4 = st.columns(4)

# select data based on the year
with select1:
    year_filter = st.multiselect(
        label="Select Year",
        options=df["year"].unique(),
        default=df["year"].unique(),
    )

# select data based on the gender
with select2:
    gender_filter = st.multiselect(
        label="Select Gender",
        options=df["gender_of_respondent"].unique(),
        default=df["gender_of_respondent"].unique(),
    )

# select data based on the country
with select3:
    country_filter = st.multiselect(
        label="Select Country",
        options=df["country"].unique(),
        default=df["country"].unique(),
    )
#
#     # select data based on the location
with select4:
    location_filter = st.multiselect(
        label="Select location",
        options=df["location_type"].unique(),
        default=df["location_type"].unique(),
    )

# # fetch data based on the filters
df_filtered = df.query(
    "year == @year_filter & gender_of_respondent == @gender_filter & country == @country_filter"
    " & location_type == @location_filter"
)

# Design the 1st row with 3 columns
col1, col2, col3 = st.columns(3)

# Draw a Pie chart using gender data
with col1:
    # filter the gender data
    gender = df_filtered["gender_of_respondent"].value_counts()
    gender_labels = gender.index.tolist()
    gender_values = gender.values.tolist()
    # format output in dataframe
    gender_counts = pd.DataFrame({"name": gender_labels, "total": gender_values})

    # plot the pie chart
    fig_gender = px.pie(
        gender_counts,
        values="total",
        names="name",
        hole=0.5,
        color="name",
        color_discrete_map={
            "Male": "RoyalBlue",
            "Female": "green",
        },
        title="<b>Gender Distributions</b>",
    )
    # customize the chart layout
    fig_gender.update_layout(
        title={"x": 0.5},
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False)),
        yaxis=(dict(showgrid=False)),
    )

    # show the pie chart on the dashboard
    st.plotly_chart(fig_gender, use_container_width=True)

# draw a bar plot using bank account data
with col2:
    # filter the bank account data
    bank = df_filtered["bank_account"].value_counts()
    bank_labels = bank.index.tolist()
    bank_values = bank.values.tolist()

    # format the output in dataframe
    bank_counts = pd.DataFrame({"name": bank_labels, "total": bank_values})

    # plot the bar chart
    fig_bank = px.bar(
        bank_counts,
        y="name",
        x="total",
        orientation="h",
        title="<b>Bank Access</b>",
    )

    # customize the layout
    fig_bank.update_layout(
        title={"x": 0.5},
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False)),
        yaxis=(dict(showgrid=False)),
    )
    # show the bar chart on the dashboard
    st.plotly_chart(fig_bank, use_container_width=True)

# draw a bar chart using cellphone access data
with col3:
    # filter the cellphone access data
    cellphone = df_filtered["cellphone_access"].value_counts()
    cellphone_labels = cellphone.index.tolist()
    cellphone_values = cellphone.values.tolist()
    # format the output in dataframe
    cellphone_counts = pd.DataFrame({"name": cellphone_labels, "total": cellphone_values})

    # plot the bar chart
    fig_cellphone = px.bar(
        cellphone_counts,
        y="name",
        x="total",
        orientation="h",
        title="<b>Cellphone Access</b>",
    )
    # customize the layout
    fig_cellphone.update_layout(
        title={"x": 0.5},
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False)),
        yaxis=(dict(showgrid=False)),
    )
    # show bar chart on the dashboard
    st.plotly_chart(fig_cellphone, use_container_width=True)

# Design the 2nd row with 2 columns
col1, col2 = st.columns([2, 1])

# Draw a bar chart using the job type data
with col1:
    # filter the job type data
    job = df_filtered["job_type"].value_counts()
    job_labels = job.index.tolist()
    job_values = job.values.tolist()
    # format the output in dataframe
    job_counts = pd.DataFrame({"job_type": job_labels, "total": job_values})

    # plot the bar chart
    fig_job = px.bar(
        job_counts,
        y="total",
        x="job_type",
        title="<b>Job Type</b>",
        text='total',

    )

    # customize the layout
    fig_job.update_layout(
        title={"x": 0.5},
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False)),
        yaxis=(dict(showgrid=False)),
    )
#
#     # show the bar chart on the dashboard
    st.plotly_chart(fig_job, use_container_width=True)

# Draw a pie chart using the education level data
with col2:
    # filter the education level data
    education = df_filtered["education_level"].value_counts()
    education_labels = education.index.tolist()
    education_values = education.values.tolist()
    # format the output in dataframe
    education_counts = pd.DataFrame({"level": education_labels, "total": education_values})

    # plot a pie chart
    fig_education = px.pie(
        education_counts,
        values="total",
        names="level",
        hole=0.5,
        color="level",
        title="<b>Education Level</b>",
    )

    # customize the layout
    fig_education.update_layout(
        title={"x": 0.5},
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False)),
        yaxis=(dict(showgrid=False)),
    )
    # show the pie chart on the dashboard
    st.plotly_chart(fig_education, use_container_width=True)

# Design the 3rd row with 2 columns
col1, col2 = st.columns(2)

# Draw a bar chart using relationship with head data
with col1:
    # filter relation with head data
    relationship_with_head = df_filtered["relationship_with_head"].value_counts()
    relation_labels = relationship_with_head.index.tolist()
    relation_values = relationship_with_head.values.tolist()
    # format the output in dataframe
    relation_counts = pd.DataFrame({"relation": relation_labels, "total": relation_values})

    # plot the bar chart
    fig_relation = px.bar(
        relation_counts,
        y="relation",
        x="total",
        orientation="h",
        title="<b>Relation with Head</b>",
        text='total'
    )
    # customize the layout
    fig_relation.update_layout(
        title={"x": 0.5},
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False)),
        yaxis=(dict(showgrid=False)),
    )

    # show the bar chart on the dashboard
    st.plotly_chart(fig_relation, use_container_width=True)

# Draw a bar chart using marital status data
with col2:
    # filter the marital status data
    marital_status = df_filtered["marital_status"].value_counts()
    marital_status_labels = marital_status.index.tolist()
    marital_status_values = marital_status.values.tolist()
    # customize the output in dataframe
    marital_status_counts = pd.DataFrame({"marital_status": marital_status_labels, "total":
        marital_status_values})

    # draw the bar chart
    fig_marital_status = px.bar(
        marital_status_counts,
        y="marital_status",
        x="total",
        orientation="h",
        title="<b>Marital Status</b>",
        text='total'
    )

    # customize the layout
    fig_marital_status.update_layout(
        title={"x": 0.5},
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False)),
        yaxis=(dict(showgrid=False)),
    )
    # show the bar chart on the dashboard
    st.plotly_chart(fig_marital_status, use_container_width=True)

# Design the 4th row with 2 columns
col1, col2 = st.columns(2)

with col1:
    # plot a histogram chart for household size data
    fig_household = px.histogram(
        df_filtered,
        x="household_size",
        title="<b>Household Size</b>",
    )

    # customize the layout
    fig_household.update_layout(
        title={"x": 0.5},
        bargap=0.2,
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False)),
        yaxis=(dict(showgrid=False)),
    )
    # show the histogram chart on the dashboard
    st.plotly_chart(fig_household, use_container_width=True)

with col2:
    # plot a histogram chart for age of respondent data
    fig_age = px.histogram(
        df_filtered,
        x="age_of_respondent",
        title="<b>Age of Responded</b>",
    )

    # customize the layout
    fig_age.update_layout(
        title={"x": 0.5},
        bargap=0.2,
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False)),
        yaxis=(dict(showgrid=False)),
    )
    # show the histogram chart on the dashboard
    st.plotly_chart(fig_age, use_container_width=True)

# Draw a scatter plot in the entire row
scatter_fig = px.scatter(
    df_filtered,
    x="age_of_respondent",
    y="household_size",
    size="household_size",
    color="relationship_with_head",
    title='<b> Age of Respondent vs Household Size </b>'
)

# customize the layout
scatter_fig.update_layout(
    title={"x": 0.5},
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False)),
    yaxis=(dict(showgrid=False)),
    )

# show scatter plot chart on the dashboard
st.plotly_chart(scatter_fig, use_container_width=True)

# # show filtered data in table
st.markdown("### Filtered Data")
st.dataframe(df_filtered, width=1200)
