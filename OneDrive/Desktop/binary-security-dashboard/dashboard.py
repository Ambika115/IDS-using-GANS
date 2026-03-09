import streamlit as st
import pandas as pd
from packet_capture import start_capture
from binary_analyzer import convert_to_binary

st.title("Binary Network Monitoring Dashboard")

if st.button("Start Packet Capture"):

    data = start_capture()

    binary_data = convert_to_binary(data)

    df = pd.DataFrame(binary_data)

    st.subheader("Packet Data")
    st.write(df)

    st.subheader("Statistics")

    st.metric("Total Packets", len(df))
    st.metric("Average Bytes", int(df["bytes"].mean()))

    st.bar_chart(df["bytes"])