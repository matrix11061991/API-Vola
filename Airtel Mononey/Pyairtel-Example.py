from pyairtel import Airtel

# Créez une instance de la classe Airtel en spécifiant vos identifiants de compte

airtel = Airtel(api_key="YOUR_API_KEY", username="YOUR_USERNAME", password="YOUR_PASSWORD")

# Appelez la méthode make_payment() pour effectuer un paiement

response = airtel.make_payment(amount=100, phone_number="0700000000", description="Paiement de test")
