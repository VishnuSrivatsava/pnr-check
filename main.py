import streamlit as st
import requests

def fetch_pnr_status(pnr):
    response = requests.get(f'https://pnr-status-for-railways-api.onrender.com/status?pnr={pnr}')
    return response.json()

st.title('PNR Status Fetcher')

pnr1 = '4822030912'
pnr2 = '2316268170'

status1 = fetch_pnr_status(pnr1)
status2 = fetch_pnr_status(pnr2)

st.write(f'PNR: {pnr1}, Status: {status1["status"]}')
st.write(f'PNR: {pnr2}, Status: {status2["status"]}')
