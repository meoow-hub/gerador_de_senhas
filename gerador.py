import secrets 
import string

def gerar_senha(tamanho=16):
    #definindo os grupos de caracteres
    alfabeto = string.ascii_letters 
    numeros = string.digits
    simbolos = string.punctuation

    #combinar os caracteres
    todos_caracteres = alfabeto + numeros + simbolos 

    senha = ''.join(secrets.choice(todos_caracteres) for i in range(tamanho))

    return senha 

nova_senha = gerar_senha(20)
print(f"Sua senha é: {nova_senha}")