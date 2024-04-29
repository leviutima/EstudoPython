def main():
    menu()

listUsu = {}
def menu():
    print('Menu Principal')
    print('1 - Usuário: '
          '\n2 - Funcionário: ')
    opc = int(input('Digite a opção que deseja: '))
    match opc:
        case 1:
            subMenuUsu()

def subMenuUsu():
    print('\nUsuário...')
    print('1 - Cadastrar Usuário: '
          '\n2 - Exibir Usuário: '
          '\n3 - Atualizar Usuário: '
          '\n4 - Deletar Usuário: '
          '\n5 - Buscar um Usuário: '
          '\n6 - Importar para Json: '
          '\n7 - Exportar para Json: ')
    opc = int(input('Digite a opção que deseja: '))
    match opc:
        case 1:
            print('\nCadastrando Usuário...')
            id = int(input('Digite o ID do usuário: '))
            while True:
                nome = input('Digite o nome do usuário: ')
                if nome.isalpha():
                    break
                else:
                    print('\nCaracteres inválidos! Escreva apenas letras!\n')
            idade = int(input('Digite a idade do usuário: '))
            usuario = {f'ID': id, 'Nome': nome, 'Idade': idade}
            listUsu[id] = usuario
            print('Usuário cadastrado com sucesso!')
            voltarSubMenu()

        case 2:
            print('Usuários cadastrados:')
            if len(listUsu) == 0:
                print('Nenhum usuário cadastrado!')
            else:
                for id, valores in listUsu.items():
                    print(f'{id} - {valores}')
            voltarSubMenu()
        case 3:
            print('\nAtualizando usuário...')
            id = int(input('Digite o ID do usuário que deseja alterar: '))
            if id in listUsu:
                nome_novo = input('Digite o novo nome do usuário: ')
                idade_nova = int(input('Digite a nova idade do usuário: '))
                listUsu[id]['Nome'] = nome_novo
                listUsu[id]['Idade'] = idade_nova
                print('Usuário atualizado com sucesso!')
            else:
                print('Nenhum usuário cadastrado!')
            voltarSubMenu()
        case 4:
            print('Deletando usuário...')
            id = int(input('Digite o ID do usuário que deseja deletar: '))
            if id in listUsu:
                listUsu.pop(id)
                print('Usuário deletado com sucesso!')
            else:
                print('Nenhum usuário encontrado')
            voltarSubMenu()
        case 5:
            print('\nBuscando usuário...')
            id = int(input('Digite o ID do usuário para encontra-lo: '))
            if id in listUsu:
                buscar = listUsu[id]
                print(buscar)
            else:
                print('Nenhum')
            voltarSubMenu()
        case 6:
            print('Importar para Json:')





def voltarSubMenu():
    opc = int(input('\nDeseja continuar a aplicação? (1/SIM) (2/NÃO): '))
    if opc == 1:
        subMenuUsu()
    else:
        print('Finalizando a aplicação...')



if __name__ == '__main__':
    main()