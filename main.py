import streamlit as st
import requests
import re
import json

# Assuming this function is part of your larger application
def get_pnr_status(pnr):
    url = f"https://api.example.com/pnr_status/{pnr}"
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        pattern = r'data\s*=\s*({.*?;)'  # Regular expression to match the desired data structure
        match = re.search(pattern, html_content, re.DOTALL)
        if match:
            json_data = match.group(1).replace(';', '')
            try:
                parsed_data = json.loads(json_data)
                return parsed_data
            except json.JSONDecodeError as e:
                st.error(f"JSON decoding error: {e}")
                return None
        else:
            st.error("No JSON data found on the webpage.")
            return None
    else:
        st.error(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

# Streamlit UI
def main():
    st.title("PNR Status Checker")

    pnr1, pnr2 = "2316268170", "4822030912"  # Example PNRs
    if st.button("Fetch PNR Statuses"):
        with st.spinner("Fetching..."):
            status1 = get_pnr_status(pnr1)
            status2 = get_pnr_status(pnr2)
            st.write(f"PNR {pnr1}: ", status1)
            st.write(f"PNR {pnr2}: ", status2)

if __name__ == "__main__":
    main()