# TODOS OS LIVROS
livros = [
    {"cont": 1, "titulo": "Sonho de uma noite de verão", "genero": "Romance", "disponivel": True},
    {"cont": 2, "titulo": "O fantasma da meia-noite", "genero": "Romance", "disponivel": True},
    {"cont": 3, "titulo": "O fantasma da meia-noite", "genero": "Romance", "disponivel": True},
    {"cont": 4, "titulo": "Duas vidas, dois destinos", "genero": "Romance", "disponivel": True},
    {"cont": 5, "titulo": "Extraordinário", "genero": "Romance", "disponivel": True},
    
    {"cont": 6, "titulo": "AutoCad 2000 utilizando totalmente 2D, 3D e avançado", "genero": "Informática", "disponivel": True},
    {"cont": 7, "titulo": "Programação em MATLAB para engenheiros", "genero": "Informática", "disponivel": True},
    {"cont": 8, "titulo": "Montagem, manutenção e configuração de computadores pessoais", "genero": "Informática", "disponivel": True},
    {"cont": 9, "titulo": "Programação usando arquivos de dados", "genero": "Informática", "disponivel": True},
    {"cont": 10, "titulo": "Projeto de banco de dados", "genero": "Informática", "disponivel": True},

    {"cont": 11, "titulo": "Terapia das caricias", "genero": "Psicologia", "disponivel": True},
    {"cont": 12, "titulo": "Assumindo a sua personalidade", "genero": "Psicologia", "disponivel": True},
    {"cont": 13, "titulo": "Fundamentos de psicologia educacional", "genero": "Psicologia", "disponivel": True},
    {"cont": 14, "titulo": "Vivendo, amando & aprendendo", "genero": "Psicologia", "disponivel": True},
    {"cont": 15, "titulo": "Filhos brilhantes, alunos fascinantes", "genero": "Psicologia", "disponivel": True},

    {"cont": 16, "titulo": "A grande sociedade", "genero": "Sociologia", "disponivel": True},
    {"cont": 17, "titulo": "Aprendendo a perguntar", "genero": "Sociologia", "disponivel": True},
    {"cont": 18, "titulo": "Direitos do cidadão especial", "genero": "Sociologia", "disponivel": True},
    {"cont": 19, "titulo": "Relatório terceira conferencia nacional das cidades", "genero": "Sociologia", "disponivel": True},
    {"cont": 20, "titulo": "Violência e cultura no Brasil", "genero": "Sociologia", "disponivel": True}
]

# CORES
red = "\033[31m"
green = "\033[32m"
bold = "\033[1m"
underline = "\033[4m"
back = "\033[m"

def listar_livros(livros):
    print("")
    print(bold, "**** Esses são os livros disponíveis da Biblioteca Virtual ****", back)
    for livro in livros:
        if livro["disponivel"]:
            print(f"{green}{livro['cont']}. Livro: {livro['titulo']}{back}")
        else:
            print(f"{red}{livro['cont']}. Livro: {livro['titulo']}{back}")
        print(f"   Gênero: {livro['genero']}")
        print(f"   Status: {'Disponível' if livro['disponivel'] else 'Indisponível'}")
        print("")
        time.sleep(0.2)

def total_de_livros(livros):
    return len(livros)

def adicionar_livro(livros):
    print("") 
    print(bold, "**** Para acrescentar um novo livro, preencha as informações abaixo ****", back)
    titulo = input("Digite o título do livro: ")
    genero = input("Digite o gênero do livro: ")
        
    novo_livro = {"cont": total_de_livros(livros) + 1, "titulo": titulo, "genero": genero, "disponivel": True, "nome_aluno": "", "sala_aluno": ""}
        
    livros.append(novo_livro)

    print("") 
    print(green, f"** O livro {novo_livro['titulo']} foi adicionado com sucesso! **", back)

def agendar_emprestimo(livros):
    print("") 
    print(bold, "**** Agendar um empréstimo de livro ****", back)
    listar_livros(livros)
    num_livro = int(input("Digite o número do livro que deseja: "))
        
    if num_livro in range(1, total_de_livros(livros) + 1):
        if livros[num_livro - 1]["disponivel"]:
            nome_aluno = input("Digite o seu nome: ")
            sala_aluno = input("Digite a sua sala: ")
            livros[num_livro - 1]["disponivel"] = False
            livros[num_livro - 1]["nome_aluno"] = nome_aluno
            livros[num_livro - 1]["sala_aluno"] = sala_aluno
            print("")
            print(green, f"** O livro {livros[num_livro - 1]['titulo']} foi emprestado para {nome_aluno} da sala {sala_aluno} com sucesso! **", back)
        else:
            print("")
            print(red, "** Este livro não está disponível para empréstimo no momento! **", back)
    else:
        print("")
        print(red, "** Número de livro inválido! **", back)

def ver_emprestimos(livros):
    print("") 
    print(bold, "**** Livros Emprestados ****", back)
    emprestados = [livro for livro in livros if not livro["disponivel"]]
    
    if emprestados:
        for livro in emprestados:
            print(f"{red}{livro['cont']}. Livro: {livro['titulo']}{back}")
            print(f"   Gênero: {livro['genero']}")
            print(f"   Status: Emprestado")
            print(f"   Emprestado para: {livro['nome_aluno']} (Sala: {livro['sala_aluno']})")
            print("")
            time.sleep(0.5)
    else:
        print("")
        print(green, "** Não há livros emprestados no momento! **", back)

def romance(livros):
    print("")
    for livro in livros:
        if livro["genero"] == "Romance": 
            if livro["disponivel"]:
                print(f"{green}{livro['cont']}. Livro: {livro['titulo']}{back}")
            else:
                print(f"{red}{livro['cont']}. Livro: {livro['titulo']}{back}")
            print(f"   Gênero: {livro['genero']}")
            print(f"   Status: {'Disponível' if livro['disponivel'] else 'Indisponível'}")
            print("")
            time.sleep(0.5)

def informatica(livros):
    print("")
    for livro in livros:
        if livro["genero"] == "Informática": 
            if livro["disponivel"]:
                print(f"{green}{livro['cont']}. Livro: {livro['titulo']}{back}")
            else:
                print(f"{red}{livro['cont']}. Livro: {livro['titulo']}{back}")
            print(f"   Gênero: {livro['genero']}")
            print(f"   Status: {'Disponível' if livro['disponivel'] else 'Indisponível'}")
            print("")
            time.sleep(0.5)

def psicologia(livros):
    print("")
    for livro in livros:
        if livro["genero"] == "Psicologia":  
            if livro["disponivel"]:
                print(f"{green}{livro['cont']}. Livro: {livro['titulo']}{back}")
            else:
                print(f"{red}{livro['cont']}. Livro: {livro['titulo']}{back}")
            print(f"   Gênero: {livro['genero']}")
            print(f"   Status: {'Disponível' if livro['disponivel'] else 'Indisponível'}")
            print("")
            time.sleep(0.5)

def sociologia(livros):
    print("")
    for livro in livros:
        if livro["genero"] == "Sociologia":  
            if livro["disponivel"]:
                print(f"{green}{livro['cont']}. Livro: {livro['titulo']}{back}")
            else:
                print(f"{red}{livro['cont']}. Livro: {livro['titulo']}{back}")
            print(f"   Gênero: {livro['genero']}")
            print(f"   Status: {'Disponível' if livro['disponivel'] else 'Indisponível'}")
            print("")
            time.sleep(0.5)

def mostrar_livros_por_genero(livros):
    while True:
        print("")
        print("******* Escolha um gênero: *******")
        print("* 1. Romance                     *")
        print("* 2. Informática                 *")
        print("* 3. Psicologia                  *")
        print("* 4. Sociologia                  *")
        print("* 5. Voltar ao menu principal    *")
        print("**********************************")

        escolha = int(input("Escolha o número desejado: "))
        
        if escolha == 1:
            romance(livros)
        elif escolha == 2:
            informatica(livros)
        elif escolha == 3:
            psicologia(livros)
        elif escolha == 4:
            sociologia(livros)
        elif escolha == 5:
            break
        else:
            print(red + "** Opção inválida! Tente novamente. **" + back)
 

# PROGRAMA EM SI MESMO
print("")
print("Seja bem-vindo(a) ao Clube do Livro Senai")
print("")
import time
time.sleep(0.5)

nome = str(input("Digite seu nome de usuário: "))
import getpass
senha = getpass.getpass("Digite sua senha: ")

if (nome == "bibliotecaria") and (senha == "4321"):
    user = "bibliotecaria"
else:
    user = "usuario"

while True:
    print("")
    print("***************** MENU *****************")
    print("* 1. Livros Disponíveis                *")
    print("* 2. Livros por Gêneros                *")
    print("* 3. Realizar um Empréstimo            *")
    if user == "bibliotecaria":
        print("* 4. Acrescentar Novos Livros          *")
        print("* 5. Ver Empréstimos                   *")
    print("* 6. Sair do Sistema                   *")
    print("****************************************")
    print("")

    escolha = int(input("Escolha o número desejado: "))

    if 1 <= escolha <= 5:
        if escolha == 1:
            listar_livros(livros)

        elif escolha == 2:
            mostrar_livros_por_genero(livros)

        elif escolha == 3:
            agendar_emprestimo(livros)

        elif escolha == 4 and user == "bibliotecaria":
            adicionar_livro(livros)

        elif escolha == 5 and user == "bibliotecaria":
            ver_emprestimos(livros)

    elif escolha == 6:
        print("")
        print(bold,"**** Muito obrigado(a) por usar o Sistema da Biblioteca Virtual do Senai! Esperamos que tenha gostado ;) ****",back)
        print("")
        import time
        time.sleep(1)
        break
    else:
        print(red, "** Opção inválida! **", back)