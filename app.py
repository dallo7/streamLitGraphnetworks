import streamlit as st
from pyvis.network import Network
import streamlit.components.v1 as components
import base64
import networkx as nx
import pandas as pd

net = Network(height="750px", width="100%", bgcolor="#1a1a1a",
              font_color="#00FFFF")

# set the physics layout of the network
net.barnes_hut()

df = pd.read_csv("customer1.csv")

# assuming df is your DataFrame and 'A' and 'B' are the columns
# df['genderCategory'] = df['gender'].astype(str) + "-" + df['category'].astype(str)
#
# df['genderCategory'] = df['gender'].astype(str) + "-" + df['category'].astype(str)
#
# df['categoryShopping'] = df['category'].astype(str) + "-" + df['shoppingMall'].astype(str)

# mapping = {'Standard Class': 1, 'Same Day': 2, 'Second Class': 3, 'First Class': 4}
#
# df['weights'] = df['shipMode'].replace(mapping)

# print(df['weights'])
# exit()
# #
# df.to_csv('customer1.csv')
# exit()

img = "products.jpeg"
img1 = "market.jpeg"
img2 = "region.jpeg"
img3 = "ship.jpeg"
img4 = "states.jpeg"
img6 = "face4.jpeg"


def b64_image(image_filename):
    with open(image_filename, 'rb') as f:
        image = f.read()
    return 'data:image/png;base64,' + base64.b64encode(image).decode('utf-8')


source = df['shipMode']
tar = df['customerName']
targ = df['segment']
targe = df['state']
target = df['region']
targett = df['category']
weight = df['weights']

edge_data = zip(source, tar, targ, targe, target, targett, weight)

for e in edge_data:
    src = e[0]
    dst = e[1]
    dstt = e[2]
    dsttt = e[3]
    dstttt = e[4]
    dsttttt = e[5]
    w = e[6]

    net.add_node(src, src, shape='circularImage', image=b64_image(img3), borderWidthSelected=4,
                 color={'highlight': '#00ffff', 'highlight.border': '#00ffff'},
                 font='14px cursive purple',
                 title=src)

    net.add_node(dst, dst, shape='circularImage', image=b64_image(img6), borderWidthSelected=4,
                 color={'highlight': '#00ffff', 'highlight.border': '#00ffff'},
                 font='14px cursive purple',
                 title=dst)

    net.add_node(dstt, dstt, shape='circularImage', image=b64_image(img1), borderWidthSelected=4,
                 color={'highlight': '#00ffff', 'highlight.border': '#00ffff'},
                 font='14px cursive purple',
                 title=dstt)

    net.add_node(dsttt, dsttt, shape='circularImage', image=b64_image(img4), borderWidthSelected=4,
                 color={'highlight': '#00ffff', 'highlight.border': '#00ffff'},
                 font='14px cursive purple',
                 title=dsttt)

    net.add_node(dstttt, dstttt, shape='circularImage', image=b64_image(img2), borderWidthSelected=4,
                 color={'highlight': '#00ffff', 'highlight.border': '#00ffff'},
                 font='14px cursive purple',
                 title=dstttt)

    net.add_node(dsttttt, dsttttt, shape='circularImage', image=b64_image(img), borderWidthSelected=4,
                 color={'highlight': '#00ffff', 'highlight.border': '#00ffff'},
                 font='14px cursive purple',
                 title=dsttttt)

    net.add_edge(src, dst, value=w)
    net.add_edge(dst, dstt, value=w)
    net.add_edge(dstt, dsttt, value=w)
    net.add_edge(dsttt, dstttt, value=w)
    net.add_edge(dstttt, dsttttt, value=w)

    # print(f'i am {src}, i live in {dst}, i am {w}')

neighbor_map = net.get_adj_list()

# print(net.nodes)
# exit()

# add neighbor data to node hover data
for node in net.nodes:
    node["title"] += "\n".join(neighbor_map[node["id"]])
    node["value"] = len(neighbor_map[node["id"]])

    # Save on Streamlit Sharing via Git
    try:
        path = '/tmp'
        htmlFile = open(f'{path}/graphNet.html', 'r', encoding='utf-8')
        source_code = htmlFile.read()
        components.html(source_code, height=900, width=900)

    # Save to local storage
    except:
        net.save_graph('graphNet.html')
        htmlFile = open('graphNet.html', 'r', encoding='utf-8')

    # Load HTML file in HTML component for display on Streamlit page
    components.html(htmlFile.read(),  height=800, width=800)

# Footer
st.markdown(
    """
    <br>
    <h6><a href="https://github.com/kennethleungty/Pyvis-Network-Graph-Streamlit" target="_blank">GitHub Repo</a></h6>
    <h6><a href="https://kennethleungty.medium.com" target="_blank">Medium article</a></h6>
    <h6>Disclaimer: This app is NOT intended to provide any form of medical advice or recommendations. Please consult your doctor or pharmacist for professional advice relating to any drug therapy.</h6>
    """, unsafe_allow_html=True
)

