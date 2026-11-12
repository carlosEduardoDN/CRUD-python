import subprocess

from estado import Estado

def estado():

    while True:
        subprocess.run("cls", shell=True)
        print("## MENU ##")
        print("1. Cadastrar Estado")
        print("2. Listar Estados")
        print("3. Atualizar Estado")
        print("4. Excluir Estado")
        print("0. Sair")
        opcao = int(input("=> "))
        subprocess.run("cls", shell=True)

        if opcao == 0:
            break

        elif opcao == 1:
            print("## Cadastro de Estado ##")

            estado = Estado()
            estado.nome = input("Nome: ")
            estado.sigla = input("Sigla: ")

            estado.salvar()

        elif opcao == 2:
            print("## Estados cadastrados ##")

            estado = Estado()

            for e in estado.listar():
                print(f"ID: {e['id']}, Nome: {e['nome']}, Sigla: {e['sigla']}")

        elif opcao == 3:
            print("## Atualizar Estado ##")

            estado = Estado()
            estado.id = int(input("ID do estado: "))
            estado.nome = input("Novo nome: ")
            estado.sigla = input("Nova sigla: ")

            estado.atualizar()

        elif opcao == 4:
            print("## Excluir Estado ##")

            estado = Estado()
            estado.id = int(input("ID do estado: "))

            estado.excluir()

        else:
            print("Opção inválida.")

        subprocess.run("pause > nul", shell=True)
