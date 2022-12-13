import urllib.request
import json

# Définissez l'URL de l'API MVola
mvola_url = 'https://mvola.com/api/'

# Définissez les paramètres de la requête
params = {
    'phone': '+26100000000',
    'amount': 1000,
    'reference': 'MyTransaction'
}

# Encodez les paramètres de la requête en tant que chaîne de caractères
data = urllib.parse.urlencode(params)

# Envoyez la requête en utilisant urllib
with urllib.request.urlopen(mvola_url, data) as response:
    # Récupérez la réponse en tant que chaîne de caractères JSON
    response_data = response.read().decode('utf-8')

    # Décodez la réponse JSON en tant qu'objet Python
    response_obj = json.loads(response_data)

    # Affichez les détails de la transaction
    print(response_obj['status'])
    print(response_obj['amount'])
    print(response_obj['reference'])
