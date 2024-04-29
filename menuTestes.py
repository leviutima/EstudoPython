import json


def main():
    menu()


def menu():
    print('Menu principal')
    print('1 - Cadastrar Produto: '
        '\n2 - Produtos Cadastrados: '
        '\n3 - Atualizar Produto: '
        '\n4 - Deletar Produto: '
        '\n3 - Sair do Programa: ')
    opcDesejada()
    voltarMenu()

def opcDesejada():
    opc = int(input('\nDigite a opção que deseja ver: '))
    match opc:
        case 1:
            cadastrarProd()
        case 2:
            prodCadastrados()
        case 3:
            atualizarProd()
        case 4:
            deletarProd()


listaProd = []

def prodCadastrados():
    if len(listaProd) == 0:
        print('Nenhum produto cadastrado')
    else:
        print('\nProduto cadastrado')
        for produto in listaProd:
            print(produto)

def cadastrarProd():
    print('Cadastrando produto...')
    id = int(input('Digite o ID do produto: '))
    nomeProd = input('Digite o nome do produto: ')
    precoProd = float(input('Digite o preço do produto: '))
    listaProd.append([id, nomeProd, precoProd])

def atualizarProd():
    print('Atualizar Produto')
    Id = int(input('Digite o ID do produto: '))
    if (Id == False):
        print('Produto não existe')
    else:
        for produto in listaProd:
            if produto[0] == Id:
                novo_nome = input('Digite o novo nome do produto: ')
                novo_preco = float(input('Digite o novo preço do produto: '))
                produto[1] = novo_nome
                produto[2] = novo_preco

def deletarProd():
    print('Deletando produto...')
    deleteId = int(input('Digite o ID do produto que deseja deletar: '))
    if (deleteId == False):
        print('Produto não existe')
    else:
        for produto in listaProd:
            if produto[0] == deleteId:
                listaProd.remove(produto)
                print('Produto Deletado com sucesso')


def importJson():
    path = input("Insira o caminho do arquivo json (com o formato .json no final): ")
    with open(path, "r", encoding="utf-8") as arq:
        arqJson = arq.read()
        lista = json.loads(arqJson)
        for i in range(len(lista)):
            listaProd.append(lista[i])
    print(f"{lista} importado com sucesso!")

def exportJson():
    path = input("Insira o nome do arquivo (sem o formato): ")
    with open(f"{path}.json", "w", encoding="utf-8") as arq:
        json.dump(listaProd, arq, indent=4, ensure_ascii=False)
    print(f"{listaProd} exportado com sucesso!")

def voltarMenu():
    comando = int(input('\nDigite (1/CONTINUAR) (2/PARAR APLICAÇÃO): '))
    if comando == 1:
        menu()
    if comando == 2:
        finalizandoAplicacao()

def finalizandoAplicacao():
    print('Aplicação finalizada!')

if __name__ == "__main__":
    main()