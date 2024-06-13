from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Define the API URLs for both PNR numbers
    api_urls = [
        "https://pnr-status-for-railways-api.onrender.com/status?pnr=4822030912",
        "https://pnr-status-for-railways-api.onrender.com/status?pnr=2316268170"
    ]
    
    # Initialize an empty list to store data for both PNRs
    data_list = []
    
    # Loop through each API URL and fetch the data
    for api_url in api_urls:
        response = requests.get(api_url)
        if response.status_code == 200:
            data_list.append(response.json())
        else:
            print(f"Failed to retrieve data for {api_url}. Status code:", response.status_code)
            data_list.append({})
    
    # Render the template with the data list
    return render_template('index.html', data_list=data_list)    # Render the template with the data list
if __name__ == '__main__':
    app.run(debug=True)