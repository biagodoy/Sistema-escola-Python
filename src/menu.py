def MostrarMenu():
    print("menu pricipal")
    print("1. cadastrar aluno")
    print("2. listar alunos")
    # colocar terceira opcao cadastrar notas
    
    # Criar lógica que pegar valor do terminal
    # e toma uma decisão atráves do valor inserido.

    entradaUsuario = input()

    nomeDoAluno = ""

    if entradaUsuario == "1": 
        print('Cadastrando Aluno..')
        print("Insira o nome do aluno")
        nomeDoAluno = input()
        
    if entradaUsuario == "2":
        print('Listando Alunos...')
        print(nomeDoAluno)