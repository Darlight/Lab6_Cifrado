"""
Universidad del Valle de Guatemala
nolib_RSA.py
Seccion 10
Proposito: RSA sin dependencia de libreria
"""
#https://juncotic.com/rsa-como-funciona-este-algoritmo/
from decimal import Decimal 
#Esta funciona retorna el gcd de a y b  
def gcd(a,b): 
    if b==0: 
        return a 
    else: 
        return gcd(b,a%b) 
#P y Q son son dos random numeros primos
p = int(input('Enter the value of p = ')) # 53
q = int(input('Enter the value of q = '))  # 59
#el mensaje debe ser en numeros
no = int(input('Enter the value of text = ')) 
#ejemplo "hi" => H = 8 e I = 9
n = p*q #valor de la llave publica

t = (p-1)*(q-1)  #phi - esto genera la llave privada

# e tiene que ser un numero entero, y no puede ser un factor de  n
for e in range(2,t): 
    if gcd(e,t)== 1: 
        break
# la llave publica es creada usando n y e
  
for i in range(1,10): 
    x = 1 + i*t  
    if x % e == 0: 
        d = int(x/e) #llave privada
        break

#Encriptacion
# ct = 89^e mod n, si HI fuera el mensaje. 
# Es decir, ct = (mensaje^e) % n. En el algoritomo, seria (no^e)%n
ctt = Decimal(0) 
ctt = pow(no,e) 
ct = ctt % n 
  
#Desencriptacion
# dt = = c^d mod n, si HI fuera el mensaje. 
# Es decir, dt = (ct^ d) % n
dtt = Decimal(0) 
dtt = pow(ct,d) 
dt = dtt % n 
# Se imrpime los resultados de cada dato.
print('n = '+str(n)+' e = '+str(e)+' t = '+str(t)+' d = '+str(d)+' cipher text = '+str(ct)+' decrypted text = '+str(dt)) 
