import requests
url = "https://echo.getpostman.com/post"
user_data = {
    'login': "je_inc",
    'password': 1232,
}
respons_data = requests.post(url, user_data)
incoming_data = respons_data.json().get("form")
print(incoming_data)