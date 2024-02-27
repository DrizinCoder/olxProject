from CadastroUsuario import Cadastro_Usuário
from PersistenciaUsuários import PersistenciaUsuarios
from Login import Login
import os



def main():
  
  salvar_usuarios = PersistenciaUsuarios.get_instancia()

  Usuarios = salvar_usuarios.get_usuarios()

  while True:

    try:
      
      prompt_login = int(input('Digite 1 para fazer login ou 2 para cadastrar-se ou 3 para sair:\n'))
      
    except:
      
      os.system('cls' if os.name == 'nt' else 'clear')
    
      print('\033[0;31mErro - Opção inválida\033[0;37m')
      continue

    if prompt_login != 1 and prompt_login != 2 and prompt_login != 3:
      os.system('cls' if os.name == 'nt' else 'clear')
      print('\033[0;31mErro - Opção inválida\033[0;37m')

    match prompt_login:
  
      case 1:
        
          Login(Usuarios)
        
      case  2:
        
          usuario_cadastro = Cadastro_Usuário()
        
          for Ver_Usuário in Usuarios:
            if Ver_Usuário['Email'] == usuario_cadastro['Email']:
              os.system('cls' if os.name == 'nt' else 'clear')
              print('E-mail já cadastrado')
              main()
              
          salvar_usuarios.listaUsuarios.append(usuario_cadastro)
          os.system('cls' if os.name == 'nt' else 'clear')
          print('\033[32mUsuário cadastrado com sucesso!\033[37m')
        
      case 3:
        
          print('Saindo do Portal OLX..')
          quit()
      

if __name__ == "__main__":
  main()