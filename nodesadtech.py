import streamlit as st
import pandas as pd
import networkx as nx
from pyvis.network import Network
import matplotlib.pyplot as plt

# Data Preparation
data = {
    'Campaign_ID': [1000, 1000, 1000, 1001, 1003],
    'Advertiser': ['Advertiser_A', 'Advertiser_B', 'Advertiser_C', 'Advertiser_A', 'Advertiser_A'],
    'Impressions': [9684, 3519, 4752, 1877, 2646],
    'Clicks': [586, 820, 326, 437, 106]
}
df_adtech = pd.DataFrame(data)

# Setup Streamlit
st.title('AdTech Data Node Graph Visualization')
metric_choice = st.selectbox('Choose the metric for edges:', ['Impressions', 'Clicks'])

# Create Graph
G = nx.Graph()

# Adding Nodes
for node in df_adtech['Campaign_ID'].unique():
    G.add_node(str(node), title='Campaign', color='blue')
for node in df_adtech['Advertiser'].unique():
    G.add_node(node, title='Advertiser', color='red')

# Adding Edges
for _, row in df_adtech.iterrows():
    G.add_edge(str(row['Campaign_ID']), row['Advertiser'], weight=row[metric_choice])

# Visualization with PyVis - more interactive
nt = Network('500px', '800px', notebook=True)
nt.from_nx(G)
nt.show('nx.html')
st.components.v1.html(nt.generate_html(), height=800)

# Alternatively, using NetworkX for simple display
pos = nx.spring_layout(G, seed=42)  # for consistent layout
plt.figure(figsize=(10, 7))
edges = G.edges(data=True)
weights = [G[u][v]['weight'] / 100 for u, v in edges]
nx.draw(G, pos, edges=edges, with_labels=True, font_weight='bold', node_color=list(nx.get_node_attributes(G, 'color').values()), width=weights)
plt.title('Graph Representation with NetworkX')
st.pyplot(plt)
