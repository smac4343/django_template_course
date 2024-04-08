import jwt

# Secret key used for encoding and decoding JWT tokens
SECRET_KEY = "very_strong_password"

# # Example payload data
# payload = {"user_id": 123, "username": "example_user", "role": "admin"}

# # Encoding JWT token
# encoded_token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
# print("Encoded Token:", encoded_token)
encoded_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMjMsInJvbGUiOiJhZG1pbiJ9.GXYSZJtgu2Ab3UfFJwiBATxvP2pYcJsSx3WvxFKS6QM"
# Decoding JWT token
try:
    decoded_payload = jwt.decode(encoded_token, SECRET_KEY, algorithms=["HS256"])
    print("Decoded Payload:", decoded_payload)
except jwt.ExpiredSignatureError:
    print("Token has expired.")
except jwt.InvalidTokenError:
    print("Invalid token.")
