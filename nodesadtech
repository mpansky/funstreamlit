# Import libraries
import streamlit as st
import pandas as pd
import networkx as nx
from pyvis.network import Network
import tempfile

# Simulate Data Frame
@st.cache
def load_data():
    # Simulated data
    data = {
        'website': ['SiteA', 'SiteB', 'SiteC', 'SiteA', 'SiteD'],
        'advertiser': ['Ad1', 'Ad2', 'Ad3', 'Ad1', 'Ad2'],
        'impressions': [100, 150, 200, 250, 300]
    }
    return pd.DataFrame(data)

# Data preprocessing (example function)
def preprocess_data(df):
    # Example preprocessing: filtering based on impressions
    return df[df['impressions'] > 100]

# Visualization as Node Graph
def visualize_as_nodegraph(df):
    G = nx.from_pandas_edgelist(df, source='website', target='advertiser')
    net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white", notebook=True)
    net.from_nx(G)
    net.show("graph.html")
    return "graph.html"

# Streamlit App
def main():
    st.title('AdTech Data Visualization App')
    
    # Load and preprocess data
    data = load_data()
    processed_data = preprocess_data(data)
    
    # Display data table
    st.write("Processed AdTech Data:")
    st.dataframe(processed_data)
    
    # Visualize data
    if st.button('Generate Node Graph'):
        path = visualize_as_nodegraph(processed_data)
        # Use the HTML file in Streamlit
        with open(path, 'r') as f:
            html_file = f.read()
            st.components.v1.html(html_file, height=800)

if __name__ == "__main__":
    main()
