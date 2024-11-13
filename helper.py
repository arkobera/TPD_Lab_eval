import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st
import matplotlib.colors as mcolors
import plotly.graph_objs as go
from plotly.subplots import make_subplots



terror = pd.read_csv("C:\\Users\\91991\\Desktop\\Streamlit\\GlobalTerror\\globalterrorismdb_0718dist.csv",encoding="latin")
terror.rename(columns={'iyear':'Year',
                       'imonth':'Month',
                       'iday':'Day',
                       'country_txt':'Country',
                       'region_txt':'Region',
                       'attacktype1_txt':'AttackType',
                       'target1':'Target',
                       'nkill':'Killed',
                       'nwound':'Wounded',
                       'summary':'Summary',
                       'gname':'Group',
                       'targtype1_txt':'Target_type',
                       'weaptype1_txt':'Weapon_type',
                       'motive':'Motive'},inplace=True)
terror_cleaned = terror[['Year','Month','Day','Country','Region','city','latitude','longitude','AttackType','Killed','Wounded','Target','Summary','Group','Target_type','Weapon_type','Motive']]
terror_cleaned['casualities'] = terror_cleaned['Killed']+terror_cleaned['Wounded']
colors = [mcolors.to_hex(c) for c in plt.cm.Reds(np.linspace(0.3, 0.9, 25))]



def country_wise_terrorism():
    Country = terror_cleaned['Country'].value_counts().head(10)
    fig = px.bar(
        Country,
        x=Country.index,
        y=Country.values,
        title="Country-wise Terrorism Rate",
        labels={'x': 'Country', 'y': 'Count'},
        color_discrete_sequence=[colors]
    )
    st.plotly_chart(fig, use_container_width=True)



def region_wise_terrorism():
    Reg = terror_cleaned['Region'].value_counts().head(10)
    fig = px.bar(
        Reg,
        x=Reg.index,
        y=Reg.values,
        title="Region-wise Terrorism Rate",
        labels={'x': 'Region', 'y': 'Count'},
        color_discrete_sequence=[colors]
    )
    st.plotly_chart(fig, use_container_width=True)



def city_wise_terrorism():
    terror_cleaned['city'].fillna("Unknown", inplace=True)
    City = terror_cleaned['city'].value_counts()[1:10]
    fig = px.bar(
        City,
        x=City.index,
        y=City.values,
        title="Cities with Most Terror Groups",
        labels={'x': 'City', 'y': 'Count'},
        color_discrete_sequence=[colors]
    )
    st.plotly_chart(fig, use_container_width=True)


def map_analysis():
    coordinate_df = terror_cleaned[(~terror_cleaned['latitude'].isna()) & (~terror_cleaned['longitude'].isna())]
    def plot_coordinates_on_map(df, lat_col='latitude', lon_col='longitude', zoom=2, map_style="carto-positron"):
        fig = px.scatter_mapbox(
            df,
            lat=lat_col,
            lon=lon_col,
            zoom=zoom,
            mapbox_style="open-street-map", 
            title="Geographic Coordinates of Terrorism Incidents",
            color_discrete_sequence=["red"], 
            opacity=0.6 
        )
        
        fig.update_layout(
            mapbox_style="carto-positron",  
            coloraxis_showscale=False, 
            geo=dict(
                scope='world',
                showland=True,
                landcolor="lightgray"  
            ),
        )
        st.plotly_chart(fig, use_container_width=True)
    plot_coordinates_on_map(coordinate_df)


def attack_type():
    AttackType = terror_cleaned['AttackType'].value_counts().head(10)
    fig = px.bar(
        AttackType,
        x=AttackType.index,
        y=AttackType.values,
        title="Type of Attack",
        labels={'x': 'Attack Type', 'y': 'Count'},
        color_discrete_sequence=[colors]
    )
    st.plotly_chart(fig, use_container_width=True)



def country_wise_casualty_count():
    casual_df = terror_cleaned[~terror_cleaned['casualities'].isna()]
    CountryCasualties = casual_df.groupby("Country")['casualities'].sum().sort_values(ascending=False).head(10)
    fig = px.bar(
        CountryCasualties,
        x=CountryCasualties.index,
        y=CountryCasualties.values,
        title="Country-wise Casualties",
        labels={'x': 'Country', 'y': 'Casualties'},
        color_discrete_sequence=[colors]
    )
    st.plotly_chart(fig, use_container_width=True)



def target():
    terror_cleaned['Target'].fillna('Unknown', inplace=True)
    Target = terror_cleaned['Target'].value_counts()[1:10]
    fig = px.bar(
        Target,
        x=Target.index,
        y=Target.values,
        title="Usual Terror Targets",
        labels={'x': 'Target', 'y': 'Count'},
        color_discrete_sequence=[colors]
    )
    st.plotly_chart(fig, use_container_width=True)



def target_type():
    terror_cleaned['Target_type'].fillna('Unknown', inplace=True)
    TargetType = terror_cleaned['Target_type'].value_counts().head(10)
    fig = px.bar(
        TargetType,
        x=TargetType.index,
        y=TargetType.values,
        title="Usual Terror Target Types",
        labels={'x': 'Target Type', 'y': 'Count'},
        color_discrete_sequence=[colors]
    )
    st.plotly_chart(fig, use_container_width=True)



def active_groups():
    group_df = terror_cleaned[~terror_cleaned['Group'].isna()]
    ActiveGroups = group_df['Group'].value_counts()[1:10]
    fig = px.bar(
        ActiveGroups,
        x=ActiveGroups.index,
        y=ActiveGroups.values,
        title="Most Active Terror Groups",
        labels={'x': 'Group', 'y': 'Count'},
        color_discrete_sequence=[colors]
    )
    fig.update_layout(xaxis={'categoryorder':'total descending'}, xaxis_tickangle=90)
    st.plotly_chart(fig, use_container_width=True)

def common_weapons():
    WeaponType = terror_cleaned['Weapon_type'].value_counts().head(10)
    fig = px.bar(
        WeaponType,
        x=WeaponType.index,
        y=WeaponType.values,
        title="Most Commonly Used Weapons",
        labels={'x': 'Weapon Type', 'y': 'Count'},
        color_discrete_sequence=[colors]
    )
    st.plotly_chart(fig, use_container_width=True)



def trend_over_years_treemap():
    yearly_data = terror_cleaned.groupby('Year')[['Killed', 'Wounded', 'casualities']].sum().reset_index()
    yearly_data_melted = yearly_data.melt(id_vars='Year', 
                                          value_vars=['Killed', 'Wounded', 'casualities'], 
                                          var_name='Category', 
                                          value_name='Count')
    fig = px.treemap(
        yearly_data_melted,
        path=['Year', 'Category'],
        values='Count',
        color='Count', 
        color_continuous_scale="Reds",
        title="Distribution of Killed, Wounded, and Casualties Over Years"
    )

    fig.update_layout(
        coloraxis_colorbar=dict(title="Total Count"),
        title_font_size=14
    )
    return fig 

def region_wise_average():
    region_casualties = terror_cleaned.groupby('Region')[['casualities', 'Killed', 'Wounded']].mean().reset_index()
    fig = make_subplots(rows=1, cols=3, subplot_titles=("Average Casualties by Region", "Average Killed by Region", "Average Wounded by Region"))
    fig.add_trace(go.Bar(
        x=region_casualties['Region'],
        y=region_casualties['casualities'],
        name="Casualties",
        marker_color="red"
    ), row=1, col=1)
    fig.add_trace(go.Bar(
        x=region_casualties['Region'],
        y=region_casualties['Killed'],
        name="Killed",
        marker_color="darkred"
    ), row=1, col=2)
    fig.add_trace(go.Bar(
        x=region_casualties['Region'],
        y=region_casualties['Wounded'],
        name="Wounded",
        marker_color="orange"
    ), row=1, col=3)
    fig.update_layout(
        title="Average Casualties, Killed, and Wounded by Region",
        showlegend=False,
        height=600
    )
    fig.update_xaxes(tickangle=90)
    return fig  



def top_25_groups_analysis():
    top_25_groups = terror_cleaned['Group'].value_counts().nlargest(25).index
    top_25_data = terror_cleaned[terror_cleaned['Group'].isin(top_25_groups)]
    fig = make_subplots(rows=1, cols=3, subplot_titles=("Average Casualties by Top 25 Groups",
                                                        "Average Killed by Top 25 Groups",
                                                        "Average Wounded by Top 25 Groups"))
    casualties_avg = top_25_data.groupby('Group')['casualities'].mean().reindex(top_25_groups)
    fig.add_trace(go.Bar(
        x=casualties_avg.index,
        y=casualties_avg.values,
        name='Average Casualties',
        marker_color='firebrick'
    ), row=1, col=1)
    killed_avg = top_25_data.groupby('Group')['Killed'].mean().reindex(top_25_groups)
    fig.add_trace(go.Bar(
        x=killed_avg.index,
        y=killed_avg.values,
        name='Average Killed',
        marker_color='darkred'
    ), row=1, col=2)
    wounded_avg = top_25_data.groupby('Group')['Wounded'].mean().reindex(top_25_groups)
    fig.add_trace(go.Bar(
        x=wounded_avg.index,
        y=wounded_avg.values,
        name='Average Wounded',
        marker_color='orangered'
    ), row=1, col=3)
    fig.update_layout(
        title="Average Casualties, Killed, and Wounded by Top 25 Terrorist Groups",
        showlegend=False,
        height=600
    )
    fig.update_xaxes(tickangle=90)
    return fig 



def province_year_killings_treemap():
    top_regions = terror_cleaned.nlargest(50, 'Killed')
    fig = px.treemap(
        top_regions,
        path=['Region', 'Year'],
        values='Killed',              
        color='Wounded',              
        color_continuous_scale="Reds",  
        title="Killings in Provinces/Years - Size Proportional to Number of Killings (Top 50 Regions Only)"
    )
    fig.update_layout(
        coloraxis_colorbar=dict(title="Number of Wounded"),
        title_font_size=14
    )
    return fig  


def region_attacktype_casualties():
    grouped_data = terror_cleaned.groupby(['Region', 'AttackType'])['casualities'].sum().unstack()
    fig = go.Figure()
    for attack_type in grouped_data.columns:
        fig.add_trace(go.Bar(
            x=grouped_data.index,
            y=grouped_data[attack_type],
            name=attack_type
        ))

    fig.update_layout(
        barmode='stack', 
        title='Stacked Bar Chart of Casualties by Region and Attack Type',
        xaxis_title='Region',
        yaxis_title='Total Casualties',
        xaxis_tickangle=90,
        height=600,
        showlegend=True
    )
    return fig


def custom_analysis(country):
    country_df = terror_cleaned[terror_cleaned['Country'] == country]
    country_df['casualities'].fillna(country_df['casualities'].median(), inplace=True)
    country_df['Wounded'].fillna(country_df['Wounded'].median(), inplace=True)
    country_df['Killed'].fillna(country_df['Killed'].median(), inplace=True)
    group_counts = country_df['Group'].value_counts().head(25)
    bar_fig = go.Figure(go.Bar(
        x=group_counts.index,
        y=group_counts.values,
        marker_color='darkred'
    ))
    bar_fig.update_layout(
        title=f'Top 25 Terrorist Groups in {country}',
        xaxis_title='Group',
        yaxis_title='Count',
        xaxis_tickangle=90
    )
    attack_counts = country_df['AttackType'].value_counts()
    if attack_counts.sum() == 0 or attack_counts.isnull().all():
        pie_fig = go.Figure(go.Pie(
            labels=["No Data Available"],
            values=[1],
            hole=0.4,
            title=f'Distribution of Attack Types in {country}'
        ))
    else:
        attack_counts = attack_counts[attack_counts > 0]
        if attack_counts.sum() > 0:
            pie_fig = px.pie(country_df, names=attack_counts.index, values=attack_counts.values,
                             hole=0.4, title=f'Distribution of Attack Types in {country}')
            pie_fig.update_traces(textinfo='percent+label')
        else:
            pie_fig = go.Figure(go.Pie(
                labels=["No Data Available"],
                values=[1],
                hole=0.4,
                title=f'Distribution of Attack Types in {country}'
            ))

    treemap_fig = px.treemap(
        country_df,
        path=['Region', 'AttackType'],
        values='casualities',
        color='casualities',
        color_continuous_scale="Reds",
        title=f'Casualties by Region and AttackType in {country}'
    )
    country_df_map = country_df.dropna(subset=['latitude', 'longitude'])
    if not country_df_map.empty:
        map_fig = px.scatter_mapbox(
            country_df_map,
            lat="latitude",
            lon="longitude",
            color="casualities",
            size="casualities",
            hover_name="Group",
            hover_data=["AttackType", "Killed", "Wounded"],
            color_continuous_scale="Reds",
            title=f"Location of Attacks in {country}",
            size_max=15
        )
        map_fig.update_layout(
            mapbox_style="carto-positron",
            mapbox_zoom=3,
            mapbox_center={"lat": country_df_map['latitude'].mean(), "lon": country_df_map['longitude'].mean()}
        )
    else:
        map_fig = go.Figure()
        map_fig.update_layout(title=f"No Valid Latitude/Longitude Data in {country}")
    
    return bar_fig, pie_fig, treemap_fig, map_fig



def return_country():
    return terror_cleaned['Country'].value_counts()[:30].index




