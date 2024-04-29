import json

def main():
    menu()


def menu():
    print('\nBEM VINDO A STORIES')
    print('1 - Usuário'
          '\n2 - Funcionário'
          '\n3 - Sair')
    opc = int(input('Digite a opção que deseja: '))
    match opc:
        case 1:
            subMenuUsuario()
        case 2:
            subMenuFuncionario()
        case 3:
            finalizarAplicacao()

listaUsu = {}
listaFunc = {}


def subMenuUsuario():
    print('\nUSUÁRIO')
    print('1 - Cadastrar usuario: '
          '\n2 - Exibir usuários cadastrados: '
          '\n3 - Atualizar usuário cadastrado: '
          '\n4 - Deletar usuário cadastrado: '
          '\n5 - Voltar ao menu principal: '
          '\n6 - Buscar Usuário: ')
    opcUsu = int(input('Digite a opção que deseja: '))
    match opcUsu:
        case 1:
            try:
                print('\nCadastrando Usuário...')
                id = int(input('Digite o id: '))
                while True:
                    nome_novo = input('Digite o nome: ')
                    if nome_novo.isalpha():
                        break
                    else:
                        print('\nCaractere inválido! Digite apenas letras\n')
                idade_nova = int(input('Digite a idade: '))
                usuario = {f'ID': id, 'Nome': nome_novo, 'Idade': idade_nova}
                listaUsu[id] = usuario
                print('Usuário cadastrado com sucesso')
            except Exception as e:
                print(f'Erro ao cadastrar usuário. {e}')
            voltarSubMenuUsuario()
        case 2:
            print('\nUsuários cadastrados')

            if len(listaUsu) == 0:
                print('Não há usuários cadastrados')
            else:
                for id, valores in listaUsu.items():
                    print(f'{id} - {valores}')
            voltarSubMenuUsuario()

        case 3:
            print('Atualizando Usuário...')
            ID = int(input('Digite o Id do usuário que deseja atualizar: '))
            if ID in listaUsu:
                nome_novo = input('Digite o novo nome do usuário: ')
                idade_nova = int(input('Digite a nova idade do usuário: '))
                listaUsu[ID]['Nome'] = nome_novo
                listaUsu[ID]['Idade'] = idade_nova
                print('Usuário atualizado com sucesso!')
            else:
                print('Usuário não cadastrado')
            voltarSubMenuUsuario()
        case 4:
            print('Deletando Usuário...')
            ID = int(input('Digite o Id do usuário: '))
            if ID in listaUsu:
                listaUsu.pop(ID)
                print('Usuário deletado com sucesso')
            else:
                print('Usuário não existe')
            voltarSubMenuUsuario()
        case 5:
            menu()
        case 6:
            print('Buscando usuário...')
            id = int(input('Digite o ID do usuário que deseja encontrar: '))
            if id in listaUsu:
                print(listaUsu[id])

def voltarSubMenuUsuario():
    opc = int(input('\nDeseja continuar?(1/SIM) (2/NÃO): '))
    if opc == 1:
        subMenuUsuario()
    else:
        finalizarAplicacao()

def voltarSubMenuFuncionario():
    opc = int(input('\nDeseja continuar?(1/SIM) (2/NÃO): '))
    if opc == 1:
        subMenuFuncionario()
    else:
        finalizarAplicacao()

def subMenuFuncionario():
    print('\nFuncionário')
    print('1 - Cadastrar Funcionário: '
          '\n2 - Exibir funcionários cadastrados: '
          '\n3 - Atualizar funcionários: '
          '\n4 - Deletar funcionários: '
          '\n5 - Voltar ao menu principal: ')
    opc = int(input('Digite a opção que deseja: '))
    match opc:
        case 1:
            print('\nCadastrando funcionário...')
            try:
                id = int(input('Digite o Id do funcionário: '))
                while True:
                    nome = input('Digite o nome do funcionário: ')
                    if nome.isalpha():
                        break
                    else:
                        print('Caractere inválido! Coloque apenas letras')
                idade = int(input('Digite a idade do funcionário: '))
                salario = float(input('Digite o salário do funcionário: '))
                funcionario = {f'ID': id, 'Nome': nome, 'Idade': idade, 'Salário': salario}
                listaFunc[id] = funcionario

            except Exception as e:
                print(f'Erro ao cadastrar funcionário. ERRO:{e}')
            voltarSubMenuFuncionario()
        case 2:
            print('\nExibir funcionários cadastrados')
            if len(listaFunc) == 0:
                print('Nenhum funcionário cadastrado')
            else:
                for id, funcionario in listaFunc.items():
                    print(f'{id} - {funcionario}')
            voltarSubMenuFuncionario()
        case 3:
            print('\nAtualizando funcionário...')
            id = int(input('Digite o ID funcionário que deseja atualizar: '))
            try:
                if id in listaFunc:
                    nome_novo = input('Digite o novo nome do funcionário: ')
                    idade_nova = int(input('Digite a idade nova do funcionário: '))
                    salario_novo = float(input('Digite o novo salário do funcionário: '))
                    listaFunc[id]['Nome'] = nome_novo
                    listaFunc[id]['Idade'] = idade_nova
                    listaFunc[id]['Salário'] = salario_novo
                    print('Funcionário atualizado')
            except Exception as e:
                print(f'Erro ao atualizar funcionário. ERRO: {e}')
            voltarSubMenuFuncionario()
        case 4:
            print('\nDeletando funcionário...')
            id = int(input('Digite o id do funcionário que deseja deletar: '))
            if id in listaFunc:
                listaFunc.pop(id)
                print('Funcionário deletado do sistema!')
            else:
                print('Funcionário não está cadastrado ou não existe')
            voltarSubMenuFuncionario()
        case 5:
            menu()


def finalizarAplicacao():
    print('Finalizando aplicação')


if __name__ == '__main__':
    main()