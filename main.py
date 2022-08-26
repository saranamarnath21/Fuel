import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots
from streamlit_option_menu import option_menu


st.set_page_config(page_title='Tug Boat',layout="wide",page_icon='🚢')

st.header("FUEL OIL CONSUMPTION MONITORING SYSTEM")
hide_st_style = """
         <style>
         footer {visibility : hidden;}
         </style>
         """

st.markdown(hide_st_style,unsafe_allow_html=True)

selected = option_menu(
    menu_title = None,
    options=["Vessel FO Con Monitoring", "Total FO Con Monitoring", "Fuel Oil Consumption Calculation"],

    icons=["ship","ship"],
    orientation="horizontal",
    default_index=0,
    styles={
        "container": {"padding":"0!important","background-color":"#ADD8E6"},
        "icon":{"color":"orange","font-size":"15px","font-style":"Arial"},
        "nav-link": {
            "font-size":"12px",
            "text-align":"justify",
            "margin": "0px",
            "--hover-color":"eee",

        },
        "nav-link-selected":{"background-color":"#00008B"},
    },
)


if selected == "Vessel FO Con Monitoring":

    st.write("Tug Boat from Port to Vessel ")

    df1 = pd.read_csv("graph1.1.csv")
    df2 = pd.read_csv("graph2a.csv")
    df8 = pd.read_csv("graph2.1.csv")
    df9 = pd.read_csv("graph2.2.csv")

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Scatter(x=df1['UTC Date & time'], y=df1['Speed (Knots)'], name="Speed (Knots)"),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(x=df2['UTC Date & time'], y=df2['power(kw)'], name="power(kw)"),
        secondary_y=True,
    )
    fig.add_trace(
        go.Scatter(x=df8['UTC Date & time'], y=df8['Bollard Pull'], name="Bollard Pull"),
        secondary_y=True,
    )
    fig.add_trace(
        go.Scatter(x=df9['UTC Date & time'], y=df9['Fuel Oil Consumption (Litre)'], name="Fuel Oil Consumption (Litre)"),
        secondary_y=True,
    )

    fig.update_layout(

        autosize=False,
        width=1000,
        height=600,

    )

    fig.update_xaxes(title_text="UTC Date & time")
    fig.update_yaxes(title_text="Speed(knots) , Power , Bollard Pull , FO Consumption", )
    fig.update_yaxes(range=[0, 50])

    df3 = pd.read_csv("tug1.csv")
    st.write(df3)
    fig.update_yaxes(visible=True, showticklabels=True, title_font=dict(size=12))
    st.plotly_chart(fig, use_container_width=True)





    st.write("Tug Boat from vessel to Port ")

    df5 = pd.read_csv("graph3.csv")
    df6 = pd.read_csv("graph4.csv")

    fig1 = make_subplots(specs=[[{"secondary_y": True}]])

    fig1.add_trace(
        go.Scatter(x=df5['UTC Date & time'], y=df5['Speed (Knots)'], name="Speed (Knots)"),
        secondary_y=False,
    )
    fig1.add_trace(
        go.Scatter(x=df6['UTC Date & time'], y=df6['Fuel Oil Consumption (Litre)'], name="Fuel Oil Consumption (Litre)"),
        secondary_y=True,
    )

    fig1.update_layout(
        autosize=False,
        width=1000,
        height=600,

    )

    fig1.update_xaxes(title_text="UTC Date & Time")
    fig1.update_yaxes(title_text="Speed , FO Consumption", )
    fig1.update_yaxes(range=[0, 50])
    df7 = pd.read_csv("tug2.csv")
    st.write(df7)
    fig1.update_yaxes(visible=True, showticklabels=True, title_font=dict(size=12))
    st.plotly_chart(fig1, use_container_width=True)




if selected == "Total FO Con Monitoring":

    st.write("Total Fuel Oil Consumption")

    df5 = pd.read_csv("graph5.csv")
    df6 = pd.read_csv("graph6.csv")

    fig2 = make_subplots(specs=[[{"secondary_y": True}]])

    fig2.add_trace(
        go.Scatter(x=df5['UTC Date & time'], y=df5[' Total Speed'], name="speed (Knots)"),
        secondary_y=False,
    )
    fig2.add_trace(
        go.Scatter(x=df6['UTC Date & time'], y=df6['Total Fuel Oil Consumption (Litre)'], name="Fuel Oil Consumption (Litre)"),
        secondary_y=True,
    )

    fig2.update_layout(

        autosize=False,
        width=1000,
        height=600,

    )

    fig2.update_xaxes(title_text="UTC Date & Time")
    fig2.update_yaxes(title_text="Total Speed , Total FO Consumption", )
    fig2.update_yaxes(range=[0, 70])

    df8 = pd.read_csv("tug3.csv")
    st.write(df8)
    fig2.update_yaxes(visible=True, showticklabels=True, title_font=dict(size=12))
    st.plotly_chart(fig2, use_container_width=True)

if selected == "Fuel Oil Consumption Calculation":
    st.write("Fuel Oil Consumption Calculation")
    X = st.number_input("Ship Speed Knots")
    FOC = -609.4+85.84*X
    st.write(FOC)
