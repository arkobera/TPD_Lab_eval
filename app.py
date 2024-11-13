import streamlit as st
import pandas as pd
from helper import*


@st.cache_data
def load_data():
    return pd.read_csv("C:\\Users\\91991\\Desktop\\Streamlit\\GlobalTerror\\globalterrorismdb_0718dist.csv", encoding='latin1')

data = load_data()

st.sidebar.title("Global Terror Analysis")
st.sidebar.subheader("Options")

csv_data = data.to_csv(index=False)  

st.sidebar.download_button(
    label="Download Dataset",
    data=csv_data,
    file_name="global_terror_data.csv",
    mime="text/csv"
)

tab = st.sidebar.radio(
    "Choose Analysis Type",
    ("Univariate Analysis", "Bivariate & Multivariate Analysis", "Custom Analysis"),
    index=0
)

st.title("Global Terror Analysis")





if tab == "Univariate Analysis":
    st.subheader("Univariate Analysis")
    col1, col2, col3 = st.columns(3)
    with col1:
        country_wise_terrorism()
    with col2:
        region_wise_terrorism()
    with col3:
        city_wise_terrorism()
    st.write("Map Analysis")  
    map_analysis()

    col4, col5, col6 = st.columns(3)
    with col4:
        attack_type()
    with col5:
        country_wise_casualty_count()
    with col6:
        target()
    
    col7, col8, col9 = st.columns(3)
    with col7:
        target_type()
    with col8:
        active_groups()
    with col9:
        common_weapons()

    st.markdown("### Analysis Results")
    st.markdown("""
    - **Country-wise**: Iraq, Pakistan, Afghanistan, and India are at the top for terrorism activity.
    - **Region-wise**: Middle East & North Africa, South Asia, and South America report the highest incidents.
    - **Cities**: Baghdad, Karachi, and Lima face the most frequent attacks.
    - **Attack Types**: Bombing and Armed Assault are the most common forms of attack.
    - **Casualties**: Iraq leads in casualties, followed by Afghanistan and Pakistan.
    - **Target Types**: Civilians are the primary targets, followed by military personnel.
    - **Terror Groups**: Taliban is the most active, followed by ISIL and SL.
    """)



if tab == "Bivariate & Multivariate Analysis":
    st.subheader("Bivariate & Multivariate Analysis")

    st.markdown("### Trend of Killed, Wounded, and Casualties Over Years")
    st.plotly_chart(trend_over_years_treemap(), use_container_width=True)
    
    st.markdown("### Region-Wise Average Casualties, Killed, and Wounded")
    st.plotly_chart(region_wise_average(), use_container_width=True)
    
    st.markdown("### Average Casualties, Killed, and Wounded by Top 25 Terrorist Groups")
    st.plotly_chart(top_25_groups_analysis(), use_container_width=True)
    
    st.markdown("### Killing grouped with region")
    st.plotly_chart(province_year_killings_treemap(), use_container_width=True)

    st.markdown("### Casualties by region and attacktype")
    st.plotly_chart(region_attacktype_casualties(), use_container_width=True)

    st.markdown("### Analysis Results")
    st.markdown("""
    - **Year-wise Analysis**: The years 2013-2017 recorded the highest casualties. Terrorist activities have increased significantly over time, from around 516 attacks in 1973 to over 56,000 in 2015.
    - **Region-wise Casualties**: Eastern Asia has the highest overall casualties, while Sub-Saharan Africa sees the most fatalities. East Asia records the highest number of wounded individuals.
    - **Terrorist Groups**: Al-Qaeda in Iraq caused the most casualties, followed closely by FDN and LTTE.
    - **Regional Patterns**: The Middle East region has the highest number of casualties, with a peak in 2014. The Sub-Saharan region ranks second, with the highest casualties occurring in 1994.
    """)



if tab == "Custom Analysis":
    st.subheader("Custom Analysis")
    st.write("Perform custom analysis here. The following visualizations will be displayed for the selected country.")
    country = st.selectbox("Select a Country", return_country())
    bar_fig, pie_fig, treemap_fig, map_fig = custom_analysis(country)
    st.plotly_chart(bar_fig, use_container_width=True)
    st.plotly_chart(pie_fig, use_container_width=True)
    st.plotly_chart(treemap_fig, use_container_width=True)
    st.plotly_chart(map_fig, use_container_width=True)

