url = "https://api.mvola.com/v1/payments"

data = {
    "amount": 1000,
    "description": "Paiement de test",
    "phone": "+26133770001",
}

data = json.dumps(data).encode("utf-8")

req = urllib.request.Request(url, data=data, method="POST")

with urllib.request.urlopen(req) as response:
    response_data = response.read().decode("utf-8")
    payment = json.loads(response_data)
    print(payment)
