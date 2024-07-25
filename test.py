senha = 4805
print(
"""
+================================+
| Quer acessar meu sistema?      |
| Digite a senha correta         |
| Você terá 3 tentativas         |
| Ou sera banido da vida         |
+================================+
""")
senhachute = int(input())
for i in range(1,3):
    if senhachute!=senha:
        print("acesso negado capiroto")
        senhachute = int(input("qual a senha?"))
    else:
        break
if senhachute==senha:
    print("seja muito bem-vindo bebê")
else:
    print("voce foi banido! tente ano que vem!")