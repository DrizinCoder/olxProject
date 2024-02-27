import os
from MainPage import PaginaPrincipal



def Login(Usuários):

  if len(Usuários) > 0:

    print('Para cancelar o login, digite 0')

    while True:
      
      RequerirID = input('Digite o e-mail:\n')

      contador = 0
      
      for Usuário in Usuários:
        
        if RequerirID == Usuário['Email']:

          while True:
            
            RequerirSenha = input('Digite a senha:\n')
      
            if Usuário['senha'] == RequerirSenha:

              os.system('cls' if os.name == 'nt' else 'clear')
              
              PaginaPrincipal(Usuário)
              
              contador += 1
            elif RequerirSenha == '0':
              print('Login cancelado')
              import main
              main.main()
            
            else:
              print('Senha incorreta')
              
        elif RequerirID == '0':
          print('Login cancelado')
          import main
          main.main()
          
              
      if contador == 0:
        print('E-mail não encontrado, tente novamente.')
        
  else:

    print('Erro - Não há usuários cadastrados')

  