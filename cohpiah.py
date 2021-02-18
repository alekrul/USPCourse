import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    relacao = 0
    for v in range(len(as_a)):
        relacao += abs(as_a[v] - as_b[v])
    relacao = relacao/6
    return relacao

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    wal = 0
    sentencas = separa_sentencas(texto)
    frases = []
    car_sentencas = 0
    for s in sentencas:
        frases = frases + separa_frases(s)
        car_sentencas += len(s)
    palavras = []
    car_frases = 0
    for f in frases:
        palavras = palavras + separa_palavras(f)
        car_frases += len(f)
    wal = 0
    total = 0
    for pal in palavras:
        total = total + len(pal)

    wal = total/len(palavras) 

    ttr = n_palavras_diferentes(palavras)/len(palavras)

    hlr = n_palavras_unicas(palavras)/len(palavras)

    sal = car_sentencas/len(sentencas) #

    sac = len(frases)/len(sentencas)

    pal = car_frases/len(frases) #
    
    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    relacoes = []
    for t in textos:
        ass_a = calcula_assinatura(t)
        s = compara_assinatura(ass_a, ass_cp)
        relacoes.append(s)
    menor = 10000
    infectado = 0
    for i in range(len(relacoes)):
        if relacoes[i]<menor:
            menor = relacoes[i]
            infectado = i+1
            
    return infectado

def main():
    ass_cp = le_assinatura()
    textos = le_textos()
    infectado = avalia_textos(textos, ass_cp)
    print("O autor do texto",infectado,"está infectado com COH-PIAH")

main()
