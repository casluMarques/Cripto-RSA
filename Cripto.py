import random

fator = random.SystemRandom()

#dicionário a serem usados na descriptação:
códigos_para_símbolos = {111: '0', 112: '1', 113: '2', 114: '3', 115: '4',
116: '5', 117: '6', 118: '7', 119: '8', 121: '9', 122: '=', 123: '+',
124: '-', 125: '/', 126: '*', 127: 'a', 128: 'b', 129: 'c', 131: 'd',
132: 'e', 133: 'f', 134: 'g', 135: 'h', 136: 'i', 137: 'j', 138: 'k',
139: 'l', 141: 'm', 142: 'n', 143: 'o', 144: 'p', 145: 'q', 146: 'r',
147: 's', 148: 't', 149: 'u', 151: 'v', 152: 'w', 153: 'x', 154: 'y',
155: 'z', 156: 'á', 157: 'à', 158: 'â', 159: 'ã', 161: 'é', 162: 'ê',
163: 'í', 164: 'ó', 165: 'ô', 166: 'õ', 167: 'ú', 168: 'ç', 169: 'A',
171: 'B', 172: 'C', 173: 'D', 174: 'E', 175: 'F', 176: 'G', 177: 'H',
178: 'I', 179: 'J', 181: 'K', 182: 'L', 183: 'M', 184: 'N', 185: 'O',
186: 'P', 187: 'Q', 188: 'R', 189: 'S', 191: 'T', 192: 'U', 193: 'V',
194: 'W', 195: 'X', 196: 'Y', 197: 'Z', 198: 'Á', 199: 'À', 211: 'Â',
212: 'Ã', 213: 'É', 214: 'Ê', 215: 'Í', 216: 'Ó', 217: 'Ô', 218: 'Õ',
219: 'Ú', 221: 'Ç', 222: ',', 223: '.', 224: '!', 225: '?', 226: ';',
227: ':', 228: '_', 229: '(', 231: ')', 232: '"', 233: '#', 234: '$',
235: '%', 236: '@', 237: ' ', 238: '\n'}

#dicionários a serem usados na encriptação:
símbolos_para_códigos = {'0': 111, '1': 112, '2': 113, '3': 114, '4': 115,
'5': 116, '6': 117, '7': 118, '8': 119, '9': 121, '=': 122, '+': 123,
'-': 124, '/': 125, '*': 126, 'a': 127, 'b': 128, 'c': 129, 'd': 131,
'e': 132, 'f': 133, 'g': 134, 'h': 135, 'i': 136, 'j': 137, 'k': 138,
'l': 139, 'm': 141, 'n': 142, 'o': 143, 'p': 144, 'q': 145, 'r': 146,
's': 147, 't': 148, 'u': 149, 'v': 151, 'w': 152, 'x': 153, 'y': 154,
'z': 155, 'á': 156, 'à': 157, 'â': 158, 'ã': 159, 'é': 161, 'ê': 162,
'í': 163, 'ó': 164, 'ô': 165, 'õ': 166, 'ú': 167, 'ç': 168, 'A': 169,
'B': 171, 'C': 172, 'D': 173, 'E': 174, 'F': 175, 'G': 176, 'H': 177,
'I': 178, 'J': 179, 'K': 181, 'L': 182, 'M': 183, 'N': 184, 'O': 185,
'P': 186, 'Q': 187, 'R': 188, 'S': 189, 'T': 191, 'U': 192, 'V': 193,
'W': 194, 'X': 195, 'Y': 196, 'Z': 197, 'Á': 198, 'À': 199, 'Â': 211,
'Ã': 212, 'É': 213, 'Ê': 214, 'Í': 215, 'Ó': 216, 'Ô': 217, 'Õ': 218,
'Ú': 219, 'Ç': 221, ',': 222, '.': 223, '!': 224, '?': 225, ';': 226,
':': 227, '_': 228, '(': 229, ')': 231, '"': 232, '#': 233, '$': 234,
'%': 235, '@': 236, ' ': 237, '\n': 238}

def euclidianoExtendido (a,b):
    #principal
    resto = a%b
    quociente = a//b
    if resto == 0:
        return (b,0,1)
    else:
        mdc,x,y = euclidianoExtendido(b,resto)
        return (mdc,y,x-quociente*y)

def mdc_simples(val1, val2):
    if val2 > val1:
        t = val1
        val1 = val2
        val2 = t
    v = 1
    while v != 0:
        v = val1 % val2
        val1 = val2
        val2 = v
    return val1
#Gerando p e q:
def teste_unitario(n, a):
    exp = n - 1
    while not exp & 1: #fazendo expoente ser ímpar
        exp >>= 1      #dividindo exp por 2

    if pow(a, exp, n) == 1:
        return True

    while exp < n - 1:
        if pow(a, exp, n) == n - 1:
            return True

        exp <<= 1     #multiplicando exp por 2

    return False


def miller_rabin(p, k=10):
    for i in range(k):
        a = fator.randrange(2, p - 1)
        if not teste_unitario(p, a):
            return False

    return True


def gerador_primos(tamanho):

    while True:
        a = (fator.randrange(10**(tamanho), 10**(tamanho+2)) *2) + 1
        if miller_rabin(a):
            return a

#gerando n e phi de n a apartir de p e q:
n1 = int(input("Digite o expoente n desejado: "))
p = gerador_primos(n1)
q = gerador_primos(n1)
n = p*q
phi_de_n = (p - 1) * (q - 1)

def gerador_de_chaves(phi_de_n):
#Gerando a chave 'e':
    while True:
        e = fator.randrange(2, phi_de_n)
        if mdc_simples(e,phi_de_n) == 1:
            break
    #Gerando a chave 'd':
    mdc, x ,y = euclidianoExtendido(phi_de_n, e)
    d = y%phi_de_n
    return e,d

#Gerando de fato as chaves
e, d = gerador_de_chaves(phi_de_n)

print(e, d, phi_de_n)
print(pow((símbolos_para_códigos.get('t')), e , phi_de_n))

def encriptar (string, e ,n):
    tam = len(string.title())
    print(string)
    lista = []
    for c in range (0,tam):
        lista.append(pow((símbolos_para_códigos.get(string[c])), e , n))
    return lista

lista_encriptada = encriptar("teste", e, n)
print(lista_encriptada)

def descriptar (lista_encriptada, d, n):
    mensagem = []
    for c in range (0, len(lista_encriptada)):
        mensagem.append(códigos_para_símbolos.get(pow(lista_encriptada[c], d , n)))
    return mensagem
mensagem = descriptar(lista_encriptada, d, n)
print(mensagem)
for i in range (len(mensagem)):
    print(""+ mensagem[i])
    i=+1