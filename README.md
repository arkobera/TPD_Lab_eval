
---

# Terrorism Analysis Dashboard with Streamlit

This repository contains a Streamlit-based dashboard for analyzing terrorism data. The dashboard provides a series of visualizations and analyses based on a comprehensive terrorism dataset, showcasing univariate, bivariate, and multivariate insights. 

## Features

- **Univariate Analysis**: Examines individual variables such as top affected countries, regions, and cities, as well as common attack types and targets.
- **Bivariate & Multivariate Analysis**: Provides a deeper look into trends and relationships, including yearly casualties, average casualties by region, and the most active terrorist groups.
- **Custom Analysis**: Allows users to select a specific country and explore various aspects like terrorist groups, attack types, and casualties.

## Dashboard Sections

### Univariate Analysis
- **Country, Region, and City-wise Terrorism**: Displays the countries, regions, and cities most impacted by terrorism.
- **Attack Types and Target Types**: Visualizes the most common types of attacks and targets.
- **Top Terrorist Groups and Casualties**: Highlights the most active terrorist groups and the impact on civilians and other targets.

### Bivariate & Multivariate Analysis
- **Trends in Casualties Over Time**: Shows changes in casualties, wounded, and killed over the years.
- **Region-Wise Averages**: Analyzes average casualties, deaths, and injuries across different regions.
- **Top Terrorist Groups**: Examines casualties caused by the top terrorist groups.
- **Casualties by Region and Attack Type**: Provides insights into casualty distribution by attack types across regions.

### Custom Analysis
- Allows users to select a country and view a detailed breakdown of terrorism data within that country, including maps, group counts, and attack types.

## Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/arkobera/TPD_Lab_eval.git]
   cd TPD_Lab_eval
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the dataset:
   - Download the dataset from [Global Terrorism Database (GTD)](https://www.kaggle.com/START-UMD/gtd) on Kaggle.
   - Place the downloaded dataset (usually a `.csv` file) in the root directory of this repository.

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Files

- `app.py`: Main Streamlit app file that structures the application layout and dashboard sections.
- `helper.py`: Contains helper functions to generate visualizations and analyses.
- `requirements.txt`: Lists the dependencies required to run the application.

## Screenshots

![image](https://github.com/user-attachments/assets/6a0d127e-7305-4687-9f38-0ec2ffae4a3d)


## Dataset

This application uses the Global Terrorism Database (GTD) dataset, which can be downloaded from [Kaggle](https://www.kaggle.com/datasets/START-UMD/gtd).

## Acknowledgments

- **Global Terrorism Database (GTD)**: For providing the comprehensive dataset on global terrorism incidents.

## License

This project is licensed under the MIT License.

---

