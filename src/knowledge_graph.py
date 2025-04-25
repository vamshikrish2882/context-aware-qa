# src/knowledge_graph.py

import networkx as nx
import matplotlib.pyplot as plt
import streamlit as st  #  Add this line

def visualize_knowledge_graph(triples):
    G = nx.DiGraph()

    for src, rel, tgt in triples:
        G.add_edge(src, tgt, label=rel)

    pos = nx.spring_layout(G, k=0.5)
    edge_labels = nx.get_edge_attributes(G, 'label')

    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=3000, font_size=10, edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    plt.title("Mini Knowledge Graph: Generative AI from BCG Report")

    #  Show in Streamlit
    st.pyplot(plt)  # << THIS is the fix
