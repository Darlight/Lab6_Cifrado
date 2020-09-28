import rsa

m = input("Ingrese el mensaje a encriptar: ")

# Se generan las llaves de bob
(bob_public_key, bob_private_key) = rsa.newkeys(256)
print("Llave publica de Bob: ", bob_public_key.n)
print("Llave privada de Bob: ", bob_private_key.n)

# El modulo de RSA solo opera con bytes, no con strings
message = m.encode('utf8')
print("Mensaje: ", message)

# Alice encripta el mensaje usando la llave publica de Bob
crypto = rsa.encrypt(message, bob_public_key)
print("Mensaje encriptado: ", crypto)

#Bob recibe el mensaje y lo decripta con su llave privada
message = rsa.decrypt(crypto, bob_private_key)
print("Mensaje descifrado: ", message)
