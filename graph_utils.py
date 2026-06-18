# graph_utils.py

import networkx as nx

import matplotlib.pyplot as plt

import pandas as pd




#########################################

# BLOCKCHAIN GRAPH

#########################################


def blockchain_graph(

        blockchain

):



    G=nx.DiGraph()



    for block in blockchain.chain:



        G.add_node(

        block.index,

        label=f"B{block.index}"

        )




    for i in range(

    1,

    len(blockchain.chain)

    ):



        G.add_edge(

        i-1,

        i

        )




    fig,ax=plt.subplots(

    figsize=(14,4)

    )



    pos=nx.spring_layout(

    G,

    seed=42

    )



    nx.draw(

    G,

    pos,

    with_labels=True,

    node_size=3000,

    font_size=10,

    arrows=True,

    ax=ax

    )



    plt.title(

    "Blockchain Ledger"

    )



    return fig




#########################################

# BLOCKCHAIN WITH FRAUD

#########################################



def blockchain_fraud_graph(

        blockchain,

        fraud_blocks

):



    G=nx.DiGraph()



    colors=[]



    for block in blockchain.chain:



        G.add_node(

        block.index

        )



        if block.index in fraud_blocks:



            colors.append(

            "red"

            )



        else:



            colors.append(

            "lightblue"

            )






    for i in range(

    1,

    len(blockchain.chain)

    ):



        G.add_edge(

        i-1,

        i

        )




    fig,ax=plt.subplots(

    figsize=(14,4)

    )



    pos=nx.spring_layout(

    G,

    seed=42

    )



    nx.draw(

    G,

    pos,

    node_color=colors,

    with_labels=True,

    node_size=3000,

    font_size=10,

    arrows=True,

    ax=ax

    )



    plt.title(

    "Blockchain Fraud Detection"

    )



    return fig






#########################################

# PROPERTY OWNERSHIP

#########################################



def ownership_graph(

        smart_contract,

        property_id

):



    history=smart_contract.get_history(

    property_id

    )



    G=nx.DiGraph()




    for i in range(

    len(history)

    ):



        owner=history[i]["owner"]



        G.add_node(

        owner

        )



        if i>0:



            prev=history[i-1]["owner"]



            G.add_edge(

            prev,

            owner

            )





    fig,ax=plt.subplots(

    figsize=(10,4)

    )



    pos=nx.spring_layout(

    G,

    seed=42

    )



    nx.draw(

    G,

    pos,

    with_labels=True,

    node_size=3500,

    arrows=True,

    ax=ax

    )



    plt.title(

    f"Ownership History : {property_id}"

    )



    return fig






#########################################

# TOKEN OWNERSHIP GRAPH

#########################################



def token_graph(

        token,

        property_id

):



    holders=token.get_holders(

    property_id

    )



    G=nx.Graph()




    G.add_node(

    property_id

    )




    for holder,tokens in holders.items():



        G.add_node(

        holder

        )



        G.add_edge(

        property_id,

        holder,

        weight=tokens

        )





    fig,ax=plt.subplots(

    figsize=(10,6)

    )



    pos=nx.spring_layout(

    G,

    seed=42

    )



    nx.draw(

    G,

    pos,

    with_labels=True,

    node_size=3500,

    ax=ax

    )



    labels=nx.get_edge_attributes(

    G,

    "weight"

    )



    nx.draw_networkx_edge_labels(

    G,

    pos,

    edge_labels=labels

    )



    plt.title(

    f"Token Ownership : {property_id}"

    )



    return fig






#########################################

# TOKEN FRAUD GRAPH

#########################################



def token_fraud_graph(

        token,

        property_id,

        fraud_holder=None

):



    holders=token.get_holders(

    property_id

    )



    G=nx.Graph()



    colors=[]




    G.add_node(

    property_id

    )



    colors.append(

    "lightblue"

    )






    for holder,tokens in holders.items():



        G.add_node(

        holder

        )



        G.add_edge(

        property_id,

        holder,

        weight=tokens

        )



        if holder==fraud_holder:



            colors.append(

            "red"

            )



        else:



            colors.append(

            "lightgreen"

            )





    fig,ax=plt.subplots(

    figsize=(10,6)

    )



    pos=nx.spring_layout(

    G,

    seed=42

    )



    nx.draw(

    G,

    pos,

    node_color=colors,

    with_labels=True,

    node_size=3500,

    ax=ax

    )



    labels=nx.get_edge_attributes(

    G,

    "weight"

    )



    nx.draw_networkx_edge_labels(

    G,

    pos,

    edge_labels=labels

    )



    plt.title(

    "Token Fraud Detection"

    )



    return fig






#########################################

# PROPERTY TABLE

#########################################



def property_table(

        properties

):



    rows=[]




    for pid,p in properties.items():



        rows.append(



        {

        "Property ID":

        pid,



        "Name":

        p["property_name"],



        "Owner":

        p["owner"],



        "Location":

        p["location"],



        "Value":

        p["value"]

        }



        )




    return pd.DataFrame(

    rows

    )






#########################################

# TOKEN TABLE

#########################################



def token_table(

        token,

        property_id

):



    return token.holders_df(

    property_id

    )
