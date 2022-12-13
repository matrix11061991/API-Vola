# Voici un exemple de code pour envoyer une requête de vérification de solde à l'API Airtel Money en utilisant la bibliothèque requests
# Ce code utilise la bibliothèque requests pour envoyer une requête
import requests

# votre clé d'API Airtel Money
api_key = "xxxxxxxxxx"

# votre numéro de téléphone Airtel Money
phone_number = "xxxxxxxxxx"

# l'URL de l'API Airtel Money pour la vérification de solde
url = "https://api.airtel.com/balance-check/v1/accounts/{phone_number}/balance"

# en-têtes de la requête, incluant la clé d'API
headers = {
    "apiKey": api_key
}

# envoi de la requête HTTP
response = requests.get(url, headers=headers)

# traitement de la réponse
if response.status_code == 200:
    # la réponse a réussi, afficher le solde
    balance = response.json()["data"]["balance"]
    print(f"Votre solde est de {balance}")
else:
    # la réponse a échoué, afficher le code d'erreur
    print(f"Erreur : {response.status_code}")
Ce code utilise la bibliothèque requests pour envoyer une requête




Try againimport requests

# votre clé d'API Airtel Money

api_key = "xxxxxxxxxx"

# votre numéro de téléphone Airtel Money

phone_number = "xxxxxxxxxx"

# l'URL de l'API Airtel Money pour la vérification de solde

url = "https://api.airtel.com/balance-check/v1/accounts/{phone_number}/balance"

# en-têtes de la requête, incluant la clé d'API

headers = {

    "apiKey": api_key

}

# envoi de la requête HTTP

response = requests.get(url, headers=headers)

# traitement de la réponse

if response.status_code == 200:

    # la réponse a réussi, afficher le solde

    balance = response.json()["data"]["balance"]

    print(f"Votre solde est de {balance}")

else:

    # la réponse a échoué, afficher le code d'erreur

    print(f"Erreur : {response.status_code}")



