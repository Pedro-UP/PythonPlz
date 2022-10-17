import random

def password_genert():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    simbolos = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', 
    ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    caracteres = mayusculas + minusculas + simbolos + numeros

    password = []

    for i in range(15):
        contrasena_aleatoria = random.choice(caracteres)
        password.append(contrasena_aleatoria)

    password = "".join(password)
    return password

def run():
    password = password_genert()
    print("Esta es tu nueva contraseña papu: "+ password)


if __name__ == "__main__":
    run()