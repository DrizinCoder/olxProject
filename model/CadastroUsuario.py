def Cadastro_Usuário():

  try:
    
    from Usuário import User
  
    print('Cadastro de Usuário')
    print('-'*25)
    Nome = input('Nome: ')
    Email = input('E-mail: ')
    Idade = input('Idade: ')
    CPF = input('CPF: ')
    local = input('local: ')
    senha = input('senha: ')
    confirmar = int(input('Confirmar o cadastro? 1 - sim | 2 - não:\n'))
    print('-'*25)
  
    while True:
      if confirmar == 1:
        cadastroUsuarios = {}
        
        object = User(Nome, Email, Idade, CPF, local, senha)
      
        cadastroUsuarios['Nome'] = object.nome
        cadastroUsuarios['Email'] = object.email
        cadastroUsuarios['Idade'] = object.idade
        cadastroUsuarios['CPF'] = object.cpf
        cadastroUsuarios['local'] = object.local
        cadastroUsuarios['senha'] = object.senha
        cadastroUsuarios['ListaCompras'] = object.Lista_compras
        cadastroUsuarios['ListaVendas'] = object.Lista_Vendas
        cadastroUsuarios['Notificações'] = object.Notificaçoes
      
        CadData = cadastroUsuarios.copy()
    
        return CadData
        
      elif confirmar == 2:
        print('Cadastro cancelado')
        import main
        main.main()
    
      else:
        print('Erro - Opção inválida')
        confirmar = int(input('Confirmar o cadastro? 1 - sim, 2 - não:\n'))
      
  except:
    print('\033[0;31mOcorreu um erro inesperado, tente novamente\033[0;37m')
    import main
    main.main()
    