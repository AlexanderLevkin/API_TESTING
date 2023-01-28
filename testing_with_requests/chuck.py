import requests

url = "https://api.chucknorris.io/jokes/random"
print(url)
result = requests.get(url)
print(f"status code: {result.status_code}")
assert 200 == result.status_code
if result.status_code == 200:
    print(f"Successful!!! We get the new joke")
else:
    print("Failed!!! Request is wrong")
result.encoding = 'utf-8'
print(result.text)

