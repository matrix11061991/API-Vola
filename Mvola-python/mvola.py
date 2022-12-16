import mvola

# Initialiser un client MVola
mvola_client = mvola.Client(username="votre_nom_d'utilisateur", password="votre_mot_de_passe")

# Transférer de l'argent
response = mvola_client.transfer(amount=1000, recipient="+2572222222", message="Paiement de facture")

if response.status_code == 200:
  print("Le transfert a été effectué avec succès")
else:
  print("Le transfert a échoué")
