from assento import Assento

fileiraA = [Assento('A1'),Assento("A2"),Assento('A3'),Assento('A4'),Assento('A5'),Assento('A6'),Assento('A7'),Assento('A8')]
def reserva_assento():
    for assento in fileiraA:
        print(f'Assento: {assento.nome} status da reserva: {assento.reservado} nome da reserva: {assento.nome_reservado}')
    escolha = input("escolha um assento disponível: ").upper()
    match escolha:
        case 'A1':
            if fileiraA[0].reservado:
                print("Este lugar está reservado.\n")
                reserva_assento()
                return 
            else:
                print('Este lugar está disponível.')
                #criar uma funcao que faça ele escolher novamente, ou seja voltar ao fluxo do match anterior reserva_assento()            
            nome = input("Digite o nome do cliente: ")
            fileiraA[0].reserva(nome)
            
            print("Lugar Reservado com sucesso!")
            continuar = int(input("deseja continuar? [1]. sim [2]. não: "))
            if continuar == 1:
                return reserva_assento()
            else:
                print("Escolha dos assentos finalizada.")

        case 'A2':
            if fileiraA[1].reservado:
                print("Este lugar está reservado.\n")
                reserva_assento()
                return
            else:
                print('Este lugar está disponível.')
                #criar uma funcao que faça ele escolher novamente, ou seja voltar ao fluxo do match anterior reserva_assento()            
            nome = input("Digite o nome do cliente: ")
            fileiraA[1].reserva(nome)
            print("Lugar Reservado com sucesso!")
            continuar = int(input("deseja continuar? [1]. sim [2]. não: "))
            if continuar == 1:
                return reserva_assento()
            else:
                print("Escolha dos assentos finalizada.")

        case 'A3':
            if fileiraA[2].reservado:
                print("Este lugar está reservado.\n")
                reserva_assento()
                return 
            else:
                print('Este lugar está disponível.')
                #criar uma funcao que faça ele escolher novamente, ou seja voltar ao fluxo do match anterior reserva_assento()            
            nome = input("Digite o nome do cliente: ")
            fileiraA[2].reserva(nome)
            print("Lugar Reservado com sucesso!")
            continuar = int(input("deseja continuar? [1]. sim [2]. não: "))
            if continuar == 1:
                return reserva_assento()
            else:
                print("Escolha dos assentos finalizada.")

        case 'A4':
            if fileiraA[3].reservado:
                print("Este lugar está reservado.\n")
                reserva_assento()
                return
            else:
                print('Este lugar está disponível.')
                #criar uma funcao que faça ele escolher novamente, ou seja voltar ao fluxo do match anterior reserva_assento()            
            nome = input("Digite o nome do cliente: ")
            fileiraA[3].reserva(nome)
            print("Lugar Reservado com sucesso!")
            continuar = int(input("deseja continuar? [1]. sim [2]. não: "))
            if continuar == 1:
                return reserva_assento()
            else:
                print("Escolha dos assentos finalizada.")

        case  'A5':
            if fileiraA[4].reservado:
                print("Este lugar está reservado.\n")
                reserva_assento()
                return
            else:
                print('Este lugar está disponível.')
                #criar uma funcao que faça ele escolher novamente, ou seja voltar ao fluxo do match anterior reserva_assento()            
            nome = input("Digite o nome do cliente: ")
            fileiraA[4].reserva(nome)
            print("Lugar Reservado com sucesso!")
            continuar = int(input("deseja continuar? [1]. sim [2]. não: "))
            if continuar == 1:
                return reserva_assento()
            else:
                print("Escolha dos assentos finalizada.")

        case 'A6':
            if fileiraA[5].reservado:
                print("Este lugar está reservado.\n")
                reserva_assento()
                return
            else:
                print('Este lugar está disponível.')
                #criar uma funcao que faça ele escolher novamente, ou seja voltar ao fluxo do match anterior reserva_assento()            
            nome = input("Digite o nome do cliente: ")
            fileiraA[5].reserva(nome)
            print("Lugar Reservado com sucesso!")
            continuar = int(input("deseja continuar? [1]. sim [2]. não: "))
            if continuar == 1:
                return reserva_assento()
            else:
                print("Escolha dos assentos finalizada.")

        case 'A7':
            if fileiraA[6].reservado:
                print("Este lugar está reservado.\n")
                reserva_assento()
                return
            else:
                print('Este lugar está disponível.')
                
                #criar uma funcao que faça ele escolher novamente, ou seja voltar ao fluxo do match anterior reserva_assento()            
            nome = input("Digite o nome do cliente: ")
            fileiraA[6].reserva(nome)
            print("Lugar Reservado com sucesso!")
            continuar = int(input("deseja continuar? [1]. sim [2]. não: "))
            if continuar == 1:
                return reserva_assento()
            else:
                print("Escolha dos assentos finalizada.")

        case 'A8':
            if fileiraA[7].reservado:
                print("Este lugar está reservado.\n")
                reserva_assento()
                return
            else:
                print('Este lugar está disponível.')
                #criar uma funcao que faça ele escolher novamente, ou seja voltar ao fluxo do match anterior reserva_assento()            
            nome = input("Digite o nome do cliente: ")
            fileiraA[7].reserva(nome)
            print("Lugar Reservado com sucesso!")
            continuar = int(input("deseja continuar? [1]. sim [2]. não: "))
            if continuar == 1:
                return reserva_assento()
            else:
                print("Escolha dos assentos finalizada.")

reserva_assento()
        


    


