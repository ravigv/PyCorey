import requests

r = requests.get("https://www.google.co.in/")
print(r.status_code)
print(r.ok)