import requests

response = requests.get("http://127.0.0.1:5000/board")
print(response.json())

#time to post a new quark


new_one = {"name":"giga","charge":"+1/7"}
r2 = requests.post("http://127.0.0.1:5000/board", json=new_one)

print(r2.json())