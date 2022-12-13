import mvola
# Initialisation l'objet mVola avec votre clé d'API et votre secret
mvola_client = mvola.MVolaClient(api_key="votre_clé_api", api_secret="votre_secret")

# Définition des détails du transfert d'argent, tels que le montant, le numéro de téléphone du destinataire, etc.
amount = 100 # le montant à transférer, en Ariary
phone = "034xxxxxxx" # le numéro de téléphone du destinataire
description = "Paiement pour les courses" # une description du transfert

# Effectuez le transfert d'argent
response = mvola_client.transfer_money(amount, phone, description)
# Affichez la réponse du serveur
print(response)
