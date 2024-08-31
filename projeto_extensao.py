from empreendedores import Empreendedor
from produtos import Produto

def menu():
    print("1. Adicionar Empreendedor")
    print("2. Adicionar Produto")
    print("3. Listar Empreendedores")
    print("4. Listar Produtos")
    print("5. Sair")
    return input("Escolha uma opção: ")

def main():
    empreendedores = []
    produtos = []

    while True:
        opcao = menu()

        if opcao == '1':
            nome = input("Nome do Empreendedor: ")
            email = input("Email do Empreendedor: ")
            empreendedor = Empreendedor(nome, email)
            empreendedores.append(empreendedor)
            print(f"Empreendedor {nome} adicionado com sucesso!")

        elif opcao == '2':
            nome_empreendedor = input("Nome do Empreendedor: ")
            empreendedor = next((e for e in empreendedores if e.nome == nome_empreendedor), None)
            if empreendedor:
                nome_produto = input("Nome do Produto: ")
                descricao = input("Descrição: ")
                preco = float(input("Preço: "))
                quantidade = int(input("Quantidade em Estoque: "))
                produto = Produto(nome_produto, descricao, preco, quantidade)
                empreendedor.adicionar_produto(produto)
                print(f"Produto {nome_produto} adicionado com sucesso!")
            else:
                print("Empreendedor não encontrado.")

        elif opcao == '3':
            for e in empreendedores:
                print(e)

        elif opcao == '4':
            for e in empreendedores:
                print(f"Empreendedor: {e.nome}")
                for p in e.produtos:
                    print(p)

        elif opcao == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
