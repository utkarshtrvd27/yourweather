from flask import Flask
from flask_cors import CORS
import requests
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import os

app = Flask("My api")
CORS(app)

# Set your Key Vault name
key_vault_name = "finance-invoices-secrets"  # <-- updated with your actual Key Vault name
key_vault_uri = f"https://{key_vault_name}.vault.azure.net"

# Authenticate and create a client
credential = DefaultAzureCredential()
client = SecretClient(vault_url=key_vault_uri, credential=credential)

# Fetch secrets from Azure Key Vault
API_KEY = client.get_secret("TOMORROW-API-KEY").value
api_key = client.get_secret("OPENWEATHER-API-KEY").value

@app.route('/')
def greet():
    return {"message": "Welcome to our Home Page"}, 200

@app.route('/env')
def show_env():
    return {
        "FLASK_APP": os.environ.get("FLASK_APP"),
        "FLASK_DEBUG": os.environ.get("FLASK_DEBUG")
    }

@app.route("/city/<city_name>")
def get_by_city(city_name):
    # print("Your city:",city_name)

    flag = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}")
    flag_code = int("".join(x for x in str(flag) if x.isdigit()))
    # print("RES=",RES)

    if flag_code == 200:
        # tomorrow.io API does not check for valid city names, we are using openweathermap API to check for valid city names
        res = requests.get(f"https://api.tomorrow.io/v4/weather/realtime?location={city_name}&apikey={API_KEY}")

        # Extracting the response code from the API
        res_code = int("".join(x for x in str(res) if x.isdigit()))
        # print("res_code=", res_code)

        if res_code == 200:
            res = res.json()

            temperature = res["data"]["values"]["temperature"]
            feels_like = res["data"]["values"]["temperatureApparent"]
            humidity = res["data"]["values"]["humidity"]
            dew_point = res["data"]["values"]["dewPoint"]
            wind_gust = round(res["data"]["values"]["windGust"]*(18/5), 2)
            wind_speed = round(res["data"]["values"]["windSpeed"]*(18/5), 2)
            visibility = round(res["data"]["values"]["visibility"], 3)
            cloud_cover = res["data"]["values"]["cloudCover"]
            name = res["location"]["name"]

            return {"temperature": temperature,
                    "feels_like": feels_like,
                    "humidity": humidity,
                    "dew_point": dew_point,
                    "wind_gust": wind_gust,
                    "wind_speed": wind_speed,
                    "visibility": visibility,
                    "cloud_cover": cloud_cover,
                    "name": name}, 200

    elif flag_code == 404:
        return {"message": "Something went wrong!"}, 404

    else:
        return {"message": "Server error!"}, 500

if __name__ == "__main__":
    app.run()
