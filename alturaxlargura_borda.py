largura = int(input("digite a largura :"))
altura = int(input("digite a altura :"))
a=altura
l=largura
while a >0:
    while l>0:
        if (a == altura or a == 1) or (l== 1 or l==largura):
            print("#",end="")
        else:
            print(" ",end="")
        l -= 1
    a -= 1
    l = largura
    print()
