#Universidade Mogi das Cruzes
#Alunos: Ivens Richard(RGM:11252100378) - Caue Sena Santos(RGM:11252100698)
#Projeto para máteria de Software Básico - Sistema para oficinia, para criação e edição de ordens de serviços
import os
from tabulate import tabulate

resetar = "\033[0m"
branco_negrito = "\033[1;37m"
azul_negrito = "\033[1;34m"
ciano_negrito = "\033[1;36m"
vermelho_negrito = "\033[1;31m"
verde_negrito = "\033[1;32m"

vermelho = "\033[0;31m"
azul = "\033[0;34m"
ciano = "\033[0;36m"
verde = "\033[0;32m"

print(f'''{azul_negrito}   ____  ______ _____ _____ _____ _   _          
  / __ \|  ____|_   _/ ____|_   _| \ | |   /\    
 | |  | | |__    | || |      | | |  \| |  /  \   
 | |  | |  __|   | || |      | | | . ` | / /\ \  
 | |__| | |     _| || |____ _| |_| |\  |/ ____ \ 
  \____/|_|    |_____\_____|_____|_| \_/_/    \_\
                                                 
                                                 {resetar}''')
print(f"{branco_negrito}Local dedicado para criação/edição de Ordem de Serviço(SO)")

def Menu():
    while True:
        menu_os =[
            [f"{azul_negrito}1{resetar}",f"{branco_negrito}Adicionar OS"],
            [f"{azul_negrito}2{resetar}",f"{branco_negrito}Editar OS"],
            [f"{azul_negrito}3{resetar}",f"{branco_negrito}Excluir OS"],
            [f"{azul_negrito}4{resetar}",f"{branco_negrito}Listar Ordem de serviço"],
            [f"{azul_negrito}5{resetar}",f"{branco_negrito}Sair"]
        ]
        print(f"{tabulate(menu_os, headers=[f"{ciano_negrito}Opção{resetar}", f"{ciano_negrito}Descrição{resetar}"], tablefmt="rounded_grid")}")

        opcao = input(f"{azul}Digite a opção:{resetar} ")
        if opcao == "1":
            adicionar_os()
            
        elif opcao == "2":
            editar_os()
            
        elif opcao == "3":
            excluir_os()
            
        elif opcao == "4":
            listar_os()
        
        elif opcao == "5":
            print(f"\n {ciano}Encerrando o programa...até mais!{resetar} \n")
            break
        else:
            os.system("cls")
            print(f"{vermelho}  Opção invalida! {resetar}")

lista_os = [{"OS":"1","Cliente":"Pedro","Veiculo":"Corsa","Serviço":"Troca de oleo","Entrada":"15/11/2025"}]#Exemplo de lista
def carregar_do_arquivo():
    global lista_os
    lista_os = []
    try:
        with open("arquivo.txt", "r") as arq:
            for linha in arq:
                partes = linha.strip().split(";")
                if len(partes) == 5:
                    lista_os.append({
                        "OS": partes[0],
                        "Cliente": partes[1],
                        "Veiculo": partes[2],
                        "Serviço": partes[3],
                        "Entrada": partes[4]
                    })
    except FileNotFoundError:
        pass

def adicionar_os(): #Adiciona ordem de serviço
    carregar_do_arquivo()
    print(
        f'''{azul}
   ____  _____  _____  ______ __  __   _____  ______ 
  / __ \|  __ \|  __ \|  ____|  \/  | |  __ \|  ____|
 | |  | | |__) | |  | | |__  | \  / | | |  | | |__   
 | |  | |  _  /| |  | |  __| | |\/| | | |  | |  __|  
 | |__| | | \ \| |__| | |____| |  | | | |__| | |____ 
  \____/|_|  \_\_____/|______|_|  |_| |_____/|______|
                                                     
   _____ ______ _______      _______ _____ ____  
  / ____|  ____|  __ \ \    / /_   _/ ____/ __ \ 
 | (___ | |__  | |__) \ \  / /  | || |   | |  | |
  \___ \|  __| |  _  / \ \/ /   | || |   | |  | |
  ____) | |____| | \ \  \  /   _| || |___| |__| |
 |_____/|______|_|  \_\  \/   |_____\_____\____/ 
                                      )_)        
                                                 {resetar}'''
    )
    print(f"\n    {ciano_negrito}Defina um número para Ordem de Serviço (OS){resetar}")
    print(f"{vermelho_negrito}Observação:{resetar} {vermelho}Todos os campos devem ser preenchidos!{resetar}\n")
    while True:
        try:
            num_os = int(input(f"{azul}Número da OS:{branco_negrito} ")) #Chave primaria
        except ValueError:
            print(f"\n{vermelho_negrito}Digite apenas números!{resetar}\n")
            continue
        repetida = False
        for os_item in lista_os: #Verificação de chave
            try:
                if int(os_item["OS"]) == num_os:
                    print(f"\n{vermelho_negrito}Ordem de serviço já existe!{resetar}\n")
                    repetida = True
                    break
            except KeyError:
                pass
        if not repetida:
            break 

    while True:
        nome_cliente = input(f"{azul}Nome do cliente:{branco_negrito} ")
        if all(c.isalnum() or c.isspace() for c in nome_cliente):
            break
        else:
            print(f"\n{vermelho_negrito}Nome deve conter apenas letras!{resetar}\n")

    while True:
        modelo_veiculo = input(f"{azul}Modelo do veiculo:{branco_negrito} ")
        if all(c.isalnum() or c.isspace() for c in modelo_veiculo):
            break
        else:
            print(f"\n{vermelho_negrito}Nome do modelo deve conter apenas letras!{resetar}\n")

    while True:
        servico = input(f"{azul}Serviço a ser realizado:{branco_negrito} ")
        if all(c.isalnum() or c.isspace() for c in servico): 
            break
        else:
            print(f"\n{vermelho_negrito}Digite apenas letras e números para o serviço.{resetar}\n")

    while True:
        try:
            data_entrada = input(f"{azul}Data de entrada (DD/MM/AAAA):{branco_negrito} ")
            break
        except ValueError:
            print(f"\n{vermelho_negrito}Digite apenas numeros{resetar}\n")

    nova_os = {
        "OS": num_os,
        "Cliente": nome_cliente,
        "Veiculo": modelo_veiculo,
        "Serviço": servico,
        "Entrada": data_entrada
    }

    lista_os.append(nova_os)

    with open("arquivo.txt", "a") as arq: #Salvando em arquivo
        arq.write(f"{num_os};{nome_cliente};{modelo_veiculo};{servico};{data_entrada}\n")
        os.system("cls")
    print(f"\n{verde_negrito}Ordem de serviço adicionada!{resetar}")

def editar_os(): #Edita ordem de serviço existente
    os.system("cls")
    carregar_do_arquivo()
    print(
            f'''{azul}  ______ _____ _____ _______       _____  
 |  ____|  __ \_   _|__   __|/\   |  __ \ 
 | |__  | |  | || |    | |  /  \  | |__) |
 |  __| | |  | || |    | | / /\ \ |  _  / 
 | |____| |__| || |_   | |/ ____ \| | \ \ 
 |______|_____/_____|  |_/_/    \_\_|  \_\
                                          
                                          {resetar}
'''
    )

    os_procurada = input(f"{ciano_negrito}Digite o número da OS que deseja editar:{resetar}")
    os.system("cls")

    encontrada = None
    for os_item in lista_os:
        if os_item["OS"] == os_procurada:
            encontrada = os_item
            break

    if encontrada is None:
        print(f"\n{vermelho_negrito}Ordem de Serviço não encontrada!{resetar}\n")
        return
    
    dados_atuais = [
        [f"{branco_negrito}Cliente:{encontrada['Cliente']}"],
        [f"{branco_negrito}Veiculo:{encontrada['Veiculo']}"],
        [f"{branco_negrito}Serviço:{encontrada['Serviço']}"],
        [f"{branco_negrito}Entrada:{encontrada['Entrada']}"]
    ]
    print(f"{tabulate(dados_atuais, headers=[f"{ciano_negrito}DADOS ATUAIS{resetar}"], tablefmt="rounded_grid")}")

    print(f"\n{ciano_negrito}Digite os novos dados (ou deixe vazio para manter o atual):{resetar}\n")

    novo_cliente = input(f"{branco_negrito}Cliente{azul_negrito}[{encontrada['Cliente']}]:{branco_negrito} ")
    novo_veiculo = input(f"Veiculo {azul_negrito}[{encontrada['Veiculo']}]:{branco_negrito} ")
    novo_servico = input(f"Serviço {azul_negrito}[{encontrada['Serviço']}]:{branco_negrito} ")
    nova_data = input(f"Entrada {azul_negrito}[{encontrada['Entrada']}]:{branco_negrito}")

    if novo_cliente.strip() != "":
        encontrada["Cliente"] = novo_cliente

    if novo_veiculo.strip() != "":
        encontrada["Veiculo"] = novo_veiculo

    if novo_servico.strip() != "":
        encontrada["Serviço"] = novo_servico

    if nova_data.strip() != "":
        encontrada["Entrada"] = nova_data

    # Reescrever tudo no arquivo (sobrescreve com a lista atualizada)
    with open("arquivo.txt", "w") as arq:
        for os_item in lista_os:
            linha = f"{os_item['OS']};{os_item['Cliente']};{os_item['Veiculo']};{os_item['Serviço']};{os_item['Entrada']}\n"
            arq.write(linha)
    os.system("cls")

    print(f"\n {verde_negrito}Ordem de Serviço atualizada com sucesso!{resetar}\n")

def excluir_os(): #Exclui ordem de serviço
    os.system("cls")
    carregar_do_arquivo() 
    print(
        f'''{azul}  ________   _______ _     _    _ _____ _____  
 |  ____\ \ / / ____| |   | |  | |_   _|  __ \ 
 | |__   \ V / |    | |   | |  | | | | | |__) |
 |  __|   > <| |    | |   | |  | | | | |  _  / 
 | |____ / . \ |____| |___| |__| |_| |_| | \ \ 
 |______/_/ \_\_____|______\____/|_____|_|  \_\
                                               
                                               {resetar}'''
    )

    os_procurada = input(f"{ciano_negrito}Digite o número da OS que deseja excluir: {resetar}")

    encontrada = None
    for os_item in lista_os:
        if os_item["OS"] == os_procurada:
            encontrada = os_item
            break

    if encontrada is None:
        os.system("cls")
        print(f"\n {verde_negrito}Ordem de Serviço não encontrada!{resetar}\n")
        return
    os.system("cls")

    dados_excluir = [
        [f"{branco_negrito}Cliente:{encontrada['Cliente']}"],
        [f"{branco_negrito}Veiculo:{encontrada['Veiculo']}"],
        [f"{branco_negrito}Serviço:{encontrada['Serviço']}"],
        [f"{branco_negrito}Entrada:{encontrada['Entrada']}"]
    ]
    print(f"{tabulate(dados_excluir, headers=[f"{ciano_negrito}DADOS P/ EXCLUIR{resetar}"], tablefmt="rounded_grid")}")

    confirmar = input(f"\n{vermelho_negrito}Tem certeza que deseja excluir?{resetar} ({verde}s{resetar}/{vermelho}n{resetar}):").lower()

    if confirmar != "s":
        os.system("cls")
        print(f"\n{vermelho_negrito}Operação cancelada.{resetar}")
        return

    lista_os.remove(encontrada)

    # regrava o arquivo inteiro
    with open("arquivo.txt", "w") as arq:
        for os_item in lista_os:
            arq.write(
                f"{os_item['OS']};{os_item['Cliente']};{os_item['Veiculo']};{os_item['Serviço']};{os_item['Entrada']}\n"
            )
    os.system("cls")
    print(f"\n{verde_negrito}Ordem de Serviço excluída com sucesso!{resetar}")

def listar_os(): #Cria uma lista
    carregar_do_arquivo()
    os.system("cls")

    if not lista_os:
        print(f"\n{ciano_negrito}Nenhuma ordem de serviço cadastrada!{resetar}\n")
        return

    tabela = []
    for os_item in lista_os:
        tabela.append([
            os_item['OS'],
            os_item['Cliente'],
            os_item['Veiculo'],
            os_item['Serviço'],
            os_item['Entrada']
        ])

    cabecalho = [f"{branco_negrito}OS", "Cliente", "Veículo", "Serviço", "Entrada"]

    print(
    f'''{azul}
  _      _____  _____ _______       
 | |    |_   _|/ ____|__   __|/\    
 | |      | | | (___    | |  /  \   
 | |      | |  \___ \   | | / /\ \  
 | |____ _| |_ ____) |  | |/ ____ \ 
 |______|_____|_____/   |_/_/    \_\
                                    
                                    {resetar}'''
    )
    print(tabulate(tabela, headers=cabecalho, tablefmt="rounded_grid"))
    
Menu()