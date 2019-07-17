import requests

r = requests.post("https://maker.ifttt.com/trigger/HTU/with/key/mGh-lQN4x9c62thYIg_mkh0Z27glI7okoIl6ilVcWat")
print(r.status_code)
