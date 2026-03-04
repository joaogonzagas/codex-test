print("=== SEN.AI Fase 1 ===")
print("Digite: oi, ajuda, python ou sair\n")

while True:
    mensagem = input("Você: ").lower()

    if "sair" in mensagem:
        print("SEN.AI: Encerrando conversa...")
        break
    elif "ajuda" in mensagem:
        print("SEN.AI: Você pode digitar: oi, python ou sair")
    elif "python" in mensagem or "pyhton" in mensagem:
        print("SEN.AI: Python é uma linguagem de programação.")
    elif "oi" in mensagem:
        print("SEN.AI: Olá!")
    else:
        print("SEN.AI: Não entendi.")
