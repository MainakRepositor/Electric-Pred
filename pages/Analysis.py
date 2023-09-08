import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go
import streamlit as st
import altair as alt

st.title('Energy Consumption Analysis')

# Importing the dataset
data = pd.read_csv('datasets/energy_dataset.csv', delimiter=',', nrows = None)

# Creating a Bar chart to show the generation of fossil gas over time
data['time'] = pd.to_datetime(data['time'], utc=True)
energy_source = "generation fossil gas"
data['year'] = data['time'].dt.year
grouped_data = data.groupby('year')[energy_source].sum().reset_index()
fig = go.Figure()
fig.add_trace(go.Bar(x=grouped_data['year'], y=grouped_data[energy_source], marker_color='skyblue'))
fig.update_layout(
    title='Generation of Fossil Gas Over Time (Grouped by Year)',
    xaxis_title='Year',
    yaxis_title='Generation (MW)',
    xaxis=dict(type='category'),
    showlegend=False
)
st.subheader('Fossil Gas Generation Over Time (Grouped by Year)')
st.plotly_chart(fig)

# Creating a Bar chart to showWind Offshore Energy Generation Over Time
data['time'] = pd.to_datetime(data['time'], utc=True)
data['year'] = data['time'].dt.year
energy_source = "generation fossil oil"
grouped_data = data.groupby('year')[energy_source].sum().reset_index()

fig = go.Figure()
fig.add_trace(go.Bar(x=grouped_data['year'], y=grouped_data[energy_source], marker_color='blue'))
fig.update_layout(
    title='Generation of Fossil Oil Energy Over Time (Grouped by Year)',
    xaxis_title='Year',
    yaxis_title='Generation (MW)',
    xaxis=dict(type='category'),
    showlegend=False
)
st.subheader('Fossil Oil Generation Over Time (Grouped by Year)')
st.plotly_chart(fig)

# Creating a Bar chart to show Wind Offshore Generation Over Time
data['time'] = pd.to_datetime(data['time'], utc=True)
data['year'] = data['time'].dt.year
energy_source = "generation nuclear"
grouped_data = data.groupby('year')[energy_source].sum().reset_index()
fig = px.bar(grouped_data, x='year', y=energy_source, title='Generation of Nuclear Energy Over Time (Grouped by Year)',
             labels={'year': 'Year', energy_source: 'Generation (MW)'},
             template='plotly_white')
st.subheader('Nuclear Generation Over Time (Grouped by Year)')
st.plotly_chart(fig)

# Creating a Bar chart to show the Forecasted Load vs Actual Load
st.subheader('Proportion of Forecasted Load vs. Actual Load')
data['time'] = pd.to_datetime(data['time'])
total_forecasted_load = data['total load forecast'].sum()
total_actual_load = data['total load actual'].sum()
fig = go.Figure()
fig.add_trace(go.Bar(x=['Forecasted Load', 'Actual Load'],
                     y=[total_forecasted_load, total_actual_load],
                     marker_color=['skyblue', 'lightcoral']))
fig.update_layout(
    xaxis_title='Load Type',
    yaxis_title='Total Load (MW)',
    title='Proportion of Forecasted Load vs. Actual Load',
    showlegend=False
)
st.plotly_chart(fig)

# Creating a Line chart to show the generation of fossil hard coal over time"""
energy_source = "generation fossil hard coal"
data['year'] = data['time'].dt.year
grouped_data = data.groupby('year')[energy_source].sum().reset_index()
fig = go.Figure()
fig.add_trace(go.Scatter(x=grouped_data['year'], y=grouped_data[energy_source], mode='lines', line=dict(color='green')))
fig.update_layout(
    title='Generation of Fossil Hard Coal Over Time (Grouped by Year)',
    xaxis_title='Year',
    yaxis_title='Generation (MW)',
    xaxis=dict(type='category'),
    xaxis_tickangle=-45
)
st.subheader('Fossil Hard Coal Generation Over Time (Grouped by Year)')
st.plotly_chart(fig)

# Creating a Line chart to show the generation of fossil oil over time
data['time'] = pd.to_datetime(data['time'], utc=True)
data['year'] = data['time'].dt.year
grouped_data = data.groupby('year')['generation fossil oil'].sum().reset_index()

fig_fossil_oil = go.Figure()
fig_fossil_oil.add_trace(go.Scatter(x=grouped_data['year'], y=grouped_data['generation fossil oil'], mode='lines', line=dict(color='red')))
fig_fossil_oil.update_layout(
    title='Generation of Fossil Oil Over Time (Grouped by Year)',
    xaxis_title='Year',
    yaxis_title='Generation (MW)',
    xaxis=dict(type='category'),
    xaxis_tickangle=-45
)
st.subheader('Fossil Oil Generation Over Time (Grouped by Year)')
st.plotly_chart(fig_fossil_oil)

# Create a Line chart to show Nuclear Energy Generation Over Time (Grouped by Year)
data['time'] = pd.to_datetime(data['time'], utc=True)
data['year'] = data['time'].dt.year
grouped_data = data.groupby('year')['generation nuclear'].sum().reset_index()

fig_nuclear_energy = go.Figure()
fig_nuclear_energy.add_trace(go.Scatter(x=grouped_data['year'], y=grouped_data['generation nuclear'], mode='lines', line=dict(color='blue')))
fig_nuclear_energy.update_layout(
    title='Generation of Nuclear Energy Over Time (Grouped by Year)',
    xaxis_title='Year',
    yaxis_title='Generation (MW)',
    xaxis=dict(type='category'),
    xaxis_tickangle=-45
)
st.subheader('Nuclear Energy Generation Over Time (Grouped by Year)')
st.plotly_chart(fig_nuclear_energy)

# Creating a Pie chart to show the proportion of fossil fuel generation
st.subheader('Proportion of Fossil Fuel Generation')
data['time'] = pd.to_datetime(data['time'])
fossil_fuels = ["generation fossil brown coal/lignite", "generation fossil hard coal",
                "generation fossil gas"]
total_generation_fossil_fuels = data[fossil_fuels].sum()
fig = go.Figure()
fig.add_trace(go.Pie(labels=total_generation_fossil_fuels.index,
                     values=total_generation_fossil_fuels.values,
                     marker=dict(colors=['gold', 'lightcoral', 'skyblue','red']),
                     textinfo='percent+label'))
st.plotly_chart(fig)

# Creating a Pie Chart
fossil_fuel_generation = data[fossil_fuels].sum()
fossil_fuel_labels = [col.split()[-2] for col in fossil_fuels]
st.subheader('Interactive Pie Charts - Energy Generation Proportions')
renewable_energy = ["generation geothermal", "generation hydro pumped storage aggregated",
                    "generation hydro pumped storage consumption",
                    "generation hydro run-of-river and poundage",
                    "generation hydro water reservoir", "generation marine",
                    "generation other renewable", "generation solar", "generation waste",
                    "generation wind offshore", "generation wind onshore"]

renewable_energy_generation = data[renewable_energy].sum()
renewable_energy_labels = [col.split()[-1] for col in renewable_energy]
fig2 = go.Figure(go.Pie(labels=renewable_energy_labels, values=renewable_energy_generation))
fig2.update_layout(title='Proportion of Renewable Energy Generation')

st.plotly_chart(fig2)



# Creating a Histogram for Fossil Gas Generation
st.subheader('Fossil Gas Generation')
data['time'] = pd.to_datetime(data['time'])
gas_generation = data["generation fossil gas"]
fig = go.Figure()
fig.add_trace(go.Histogram(x=gas_generation, nbinsx=20, marker_color='skyblue', opacity=0.7))

fig.update_layout(
    xaxis_title='Generation (MW)',
    yaxis_title='Frequency',
    title='Fossil Gas Generation',
    bargap=0.1
)
st.plotly_chart(fig)


# Creating a Histogram for Fossil Hard Coal Generation
st.subheader('Fossil Hard Coal Generation')
data['time'] = pd.to_datetime(data['time'])
hard_coal_generation = data["generation fossil hard coal"]
fig = go.Figure()
fig.add_trace(go.Histogram(x=hard_coal_generation, nbinsx=20, marker_color='darkorange', opacity=0.7))
fig.update_layout(
    xaxis_title='Generation (MW)',
    yaxis_title='Frequency',
    title='Fossil Hard Coal Generation',
    bargap=0.1
)
st.plotly_chart(fig)

# Creating a Histogram for Total Fossil Fuel Generation
st.subheader('Total Fossil Fuel Generation Over Time')
data['time'] = pd.to_datetime(data['time'])
fossil_fuels = ["generation fossil hard coal", "generation fossil oil",
                "generation fossil oil shale", "generation fossil peat"]
grouped_data = data.groupby('time')[fossil_fuels].sum()
total_generation = grouped_data.values.flatten()
fig = go.Figure()
fig.add_trace(go.Histogram(x=total_generation, nbinsx=20, marker_color='skyblue', opacity=0.7))

fig.update_layout(
    xaxis_title='Total Generation (MW)',
    yaxis_title='Frequency',
    title='Total Fossil Fuel Generation Over Time',
    bargap=0.1
)
st.plotly_chart(fig)


data['time'] = pd.to_datetime(data['time'], utc=True)

# Creating a Stack Area Chart for Nuclear Generation
data['time'] = pd.to_datetime(data['time'])
st.subheader('Nuclear Generation Over Time')
fig = go.Figure()
fig.add_trace(go.Scatter(x=data['time'], y=data['generation nuclear'], line=dict(color='purple')))

fig.update_layout(
    xaxis_title='Time',
    yaxis_title='Generation (MW)',
    title='Nuclear Generation Over Time',
)
st.plotly_chart(fig)

# Creating a Line Area Chart for Solar Generation
data['time'] = pd.to_datetime(data['time'])
data_resampled = data.resample('Y', on='time').sum()
fig = go.Figure()
fig.add_trace(go.Scatter(x=data_resampled.index, y=data_resampled['generation solar'], line=dict(color='orange')))
fig.update_layout(
    xaxis_title='Year',
    yaxis_title='Generation (MW)',
    title='Solar Generation Over Time',
)
st.plotly_chart(fig)



# Line chart with dual y-axes - Nuclear Generation vs. Fossil Gas Generation
data['time'] = pd.to_datetime(data['time'])
data_resampled = data.resample('Y', on='time').sum()
fig_line_dual = go.Figure()
fig_line_dual.add_trace(go.Scatter(x=data_resampled.index, y=data_resampled['generation nuclear'], 
                                   mode='lines', line=dict(color='purple'), name='Nuclear Generation (MW)'))

fig_line_dual.add_trace(go.Scatter(x=data_resampled.index, y=data_resampled['generation fossil gas'], 
                                   mode='lines', line=dict(color='blue'), name='Fossil Gas Generation (MW)'))

fig_line_dual.update_layout(
    title='Nuclear Generation vs. Fossil Gas Generation Over Time',
    xaxis_title='Year',
    yaxis_title='Generation (MW)',
    xaxis_tickangle=-45,
    legend=dict(x=0.02, y=0.98),
    yaxis=dict(title='Nuclear Generation (MW)', color='purple'),
    yaxis2=dict(title='Fossil Gas Generation (MW)', color='blue', overlaying='y', side='right')
)
st.plotly_chart(fig_line_dual)

