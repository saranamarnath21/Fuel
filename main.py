import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots
from streamlit_option_menu import option_menu


st.set_page_config(page_title='Tug Boat',layout="wide",page_icon='🚢')

st.header("FUEL OIL CONSUMPTION MONITORING SYSTEM")
hide_st_style = """
         <style>
         footer {visibility : hidden;}
         header {visibility : hidden;}
         </style>
         """

st.markdown(hide_st_style,unsafe_allow_html=True)

selected = option_menu(
    menu_title = None,
    options=["Vessel FO Con Monitoring", "Total FO Con Monitoring"],

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
    url = r'C:\Users\asus\PycharmProjects\fuel\data.xlsx'
    s = pd.read_excel(url, sheet_name='Graph')
    print(s)
    url = r'C:\Users\asus\PycharmProjects\fuel\data.xlsx'
    s1 = pd.read_excel(url, sheet_name='Graph1')
    print(s1)
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Scatter(x=s['UTC Date & time'], y=s['Speed (Knots)'], name="Speed (Knots)"),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(x=s1['UTC Date & time'], y=s1['Fuel Oil Consumption (Litre)'], name="Fuel Oil Consumption (Litre)"),
        secondary_y=True,
    )

    fig.update_layout(

        autosize=False,
        width=1000,
        height=600,

    )

    fig.update_xaxes(title_text="UTC Date & Time")
    fig.update_yaxes(title_text="Speed , FO Consumption", )
    fig.update_yaxes(range=[0, 50])

    url = r'C:\Users\asus\PycharmProjects\fuel\data.xlsx'
    s = pd.read_excel(url, sheet_name='Tug 1')
    st.write(s)
    fig.update_yaxes(visible=True, showticklabels=True, title_font=dict(size=12))
    st.plotly_chart(fig, use_container_width=True)





    st.write("Tug Boat from vessel to Port ")
    url = r'C:\Users\asus\PycharmProjects\fuel\data.xlsx'
    s2 = pd.read_excel(url, sheet_name='Graph2')
    print(s2)
    url = r'C:\Users\asus\PycharmProjects\fuel\data.xlsx'
    s3 = pd.read_excel(url, sheet_name='Graph3')
    print(s3)
    fig1 = make_subplots(specs=[[{"secondary_y": True}]])

    fig1.add_trace(
        go.Scatter(x=s2['UTC Date & time'], y=s2['Speed (Knots)'], name="Speed (Knots)"),
        secondary_y=False,
    )
    fig1.add_trace(
        go.Scatter(x=s3['UTC Date & time'], y=s3['Fuel Oil Consumption (Litre)'], name="Fuel Oil Consumption (Litre)"),
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

    url = r'C:\Users\asus\PycharmProjects\fuel\data.xlsx'
    s = pd.read_excel(url, sheet_name='Tug 2')
    st.write(s)
    fig1.update_yaxes(visible=True, showticklabels=True, title_font=dict(size=12))
    st.plotly_chart(fig1, use_container_width=True)




if selected == "Total FO Con Monitoring":

    st.write("Tug Boat from vessel to Port ")
    url = r'C:\Users\asus\PycharmProjects\fuel\data.xlsx'
    s4 = pd.read_excel(url, sheet_name='Graph4')
    print(s4)
    url = r'C:\Users\asus\PycharmProjects\fuel\data.xlsx'
    s5 = pd.read_excel(url, sheet_name='Graph5')
    print(s5)

    fig2 = make_subplots(specs=[[{"secondary_y": True}]])

    fig2.add_trace(
        go.Scatter(x=s4['UTC Date & time'], y=s4[' Total Speed'], name="Speed (Knots)"),
        secondary_y=False,
    )
    fig2.add_trace(
        go.Scatter(x=s5['UTC Date & time'], y=s5['Total Fuel Oil Consumption (Litre)'], name="Fuel Oil Consumption (Litre)"),
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


    url = r'C:\Users\asus\PycharmProjects\fuel\data.xlsx'
    s = pd.read_excel(url, sheet_name='Tug 3')
    st.write(s)
    fig2.update_yaxes(visible=True, showticklabels=True, title_font=dict(size=12))
    st.plotly_chart(fig2, use_container_width=True)






