import funcoes as funcoes

def menu():
    print("\n=== Menu ===")
    print("1. Cadastrar jogador")
    print("2. Listar todos os jogadores")
    print("3. Consultar jogador")
    print("4. Apagar jogador")
    print("5. Atualizar jogador")
    print("6. Cadastrar time")
    print("7. Listar todos os times")
    print("8. Consultar time")
    print("9. Apagar time")
    print("10. Atualizar time")
    print("0. Sair")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do jogador: ")
            idade = int(input("Idade do jogador: "))
            posicao = input("Posição do jogador: ")
            time = input("Time do jogador: ")
            funcoes.cadastrar_jogador(nome, idade, posicao, time)

        elif opcao == "2":
            print("\n=== Lista de Jogadores ===")
            funcoes.listar_jogadores()

        elif opcao == "3":
            nome = input("Nome do jogador: ")
            jogador = funcoes.consultar_jogador(nome)
            if jogador:
                print(f"Nome: {jogador.nome}, Idade: {jogador.idade}, Posição: {jogador.posicao}, Time: {jogador.time}")
            else:
                print("Jogador não encontrado.")

        elif opcao == "4":
            nome = input("Nome do jogador a ser apagado: ")
            funcoes.apagar_jogador(nome)

        elif opcao == "5":
            nome = input("Nome do jogador a ser atualizado: ")
            idade = int(input("Nova idade do jogador: "))
            posicao = input("Nova posição do jogador: ")
            time = input("Novo time do jogador: ")
            funcoes.atualizar_jogador(nome, idade, posicao, time)

        elif opcao == "6":
            nome = input("Nome do time: ")
            cidade = input("Cidade do time: ")
            funcoes.cadastrar_time(nome, cidade)

        elif opcao == "7":
            print("\n=== Lista de Times ===")
            funcoes.listar_times()

        elif opcao == "8":
            nome = input("Nome do time: ")
            time = funcoes.consultar_time(nome)
            if time:
                print(f"Nome: {time.nome}, Cidade: {time.cidade}")
            else:
                print("Time não encontrado.")

        elif opcao == "9":
            nome = input("Nome do time a ser apagado: ")
            funcoes.apagar_time(nome)

        elif opcao == "10":
            nome = input("Nome do time a ser atualizado: ")
            cidade = input("Nova cidade do time: ")
            funcoes.atualizar_time(nome, cidade)

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()