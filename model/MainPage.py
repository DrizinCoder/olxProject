import os
from PersistenciaAnuncios import PersistenciaAnuncios
from PersistenciaUsuários import PersistenciaUsuarios
from factory_produtos import Cadastro_Produto
from categoriasProduto import *



def PaginaPrincipal(Usuario):
  os.system('cls' if os.name == 'nt' else 'clear')
  
  Usuarios = PersistenciaUsuarios.get_instancia()
  Produtos = PersistenciaAnuncios.get_instancia()
  

  print('Bem-vindo ao Portal OLX,',Usuario['Nome'],'!')
  print('='*150)
  print(f'Voce tem \033[0;33m{len(Usuario["Notificações"])}\033[0;37m notificações!') if len(Usuario["Notificações"]) > 0 else print('Voce não tem notificações!')

  
  while True:
    
    ListaUsuarios = Usuarios.get_usuarios()
    ListaAnuncios = Produtos.get_Anuncios()
    
    try:
      
      operacao = int(input('Digite 1 para ver os produtos, 2 para anunciar ou editar um produto, 3 para comprar ou comentar um anuncio, 4 para ver compras, vendas e notificações ou 5 para sair da conta:\n'))
      match operacao:
      
        case 1:
  
          if len(ListaAnuncios) > 0:
            
            Listar = int(input('Digite 1 para ver todos os produtos ou 2 para filtrar:\n'))
  
            if Listar == 1:
        
              for Anuncio in ListaAnuncios:
      
               Produtos.info(Anuncio)
               print('-'*25)
  
            elif Listar == 2:
        
              TipoFiltro = int(input('Digite 1 para filtrar por tipo ou 2 para filtrar por região:\n'))
        
              if TipoFiltro == 1:
    
                tipos = {
                  1: AutosePecas,
                  2: Imóveis,
                  3: Eletrodomésticos,  
                  4: Servicos,
                  5: Moveis,
                  6: EsporteseLazer,
                  7: Games,
                  8: CasaDecor,
                  9: VagasEmprego,
                  10: Audio,
                  11: ComercioEscritorio,
                  12: MusicaHobbies,
                  13: ArtigoInfantil,
                  14: AgroIndustria,
                  15: ModaEbeleza,
                  16: AnimalEstimacao,
                  17: MaterialConstrucao,
                  18: CamerasDrones,
                  19: TvsVideos,
                  20: CelularTelefonia,
                  21: Informatica
                  }
    
                for MostrarTipos in tipos:
                  print(f'Tipo {MostrarTipos} - {tipos[MostrarTipos].__name__}')
      
                tipo = int(input('Digite o número referente ao tipo do produto:\n'))
        
                for Anuncio in ListaAnuncios:
                  if Anuncio['tipo'] == tipos[tipo].__name__:
                    
                     Produtos.info(Anuncio)
                     print('-'*25)
                      
              elif TipoFiltro == 2:
        
                for Anuncio in ListaAnuncios:
                  if Anuncio['local'] == Usuario['local']:
        
                     Produtos.info(Anuncio)
                     print('-'*25)
                    
            if Listar != 1 and Listar != 2:
              os.system('cls' if os.name == 'nt' else 'clear')
              print('\033[0;31mErro - Opção inválida\033[0;37m')
                
  
          else:
            print('Não há produtos disponíveis')
      
  
        case 2:
  
          VendaEdicao = int(input('Digite 1 para anunciar um produto ou 2 para editar um produto:\n'))
  
          match VendaEdicao:
    
            case 1:
      
              p = Cadastro_Produto(Usuario['Email'])
              Produtos.SalvarProduto(p)
              os.system('cls' if os.name == 'nt' else 'clear')
              print('\033[32mProduto anunciado com sucesso!\033[37m')
        
              for Notificar in ListaUsuarios:
        
                if Usuario['Email'] != Notificar['Email']:
        
                  Notificar['Notificações'].append(f'Novo produto anunciado por {Usuario["Nome"]} -> {p["Nome"]} | ID do anuncio: {p["ID"]}')
                  
            case 2:
          
              Id = int(input('Digite o ID do produto que deseja editar:\n'))
  
              contador = 0
              for anuncio in ListaAnuncios:
      
                if anuncio['ID'] == Id and anuncio['EmailAnunciante'] == Usuario['Email']:
                  contador += 1
      
                  item = int(input('Digite 1 para editar o nome, 2 descrição ou 3 para editar o valor'))
      
                  match item:
      
                    case 1:
                      anuncio['Nome'] = input('Digite o novo nome:\n')
                      print('Produto editado com sucesso!')
                    case 2:
                      anuncio['descricao'] = input('Digite a nova descrição:\n')
                      print('Produto editado com sucesso!')
                    case 3:
                      anuncio['preco'] = input('Digite o novo preço:\n')
                      print('Produto editado com sucesso!')
                      
                  if item != 1 and item != 2 and item != 3:
                    print('\033[0;31mErro - Opção inválida\033[0;37m')
                  
                  os.system('cls' if os.name == 'nt' else 'clear')
              if contador == 0:
                print('Produto não encontrado ou não vendido por você.')
                  
          if VendaEdicao != 1 and VendaEdicao != 2:
            print('\033[0;31mErro - Opção inválida\033[0;37m')
                
        
        case 3:
      
          Selecionado = int(input('Digite o ID do produto que deseja comprar ou comentar:\n'))
    
          CompraComent = int(input('Digite 1 para comprar ou 2 para comentar:\n'))
    
          match CompraComent:
  
            case 1:  
    
              contador = 0
              
              for Ver_Anuncio in ListaAnuncios:
          
                if Ver_Anuncio['ID'] == Selecionado:
  
                  if Ver_Anuncio['EmailAnunciante'] == Usuario['Email']:
                    print('Voce não pode comprar um produto que você anunciou!')
  
                  else:
        
                    contador += 1
                    Usuario['ListaCompras'].append(Ver_Anuncio)
                    
                    print('\033[32mProduto comprado com sucesso!\033[37m')
                    
                    Ver_Anuncio['quantidade'] -= 1
            
                    if Ver_Anuncio['quantidade'] == 0:
          
                      ListaAnuncios.remove(Ver_Anuncio)
        
                    for Vendedor in ListaUsuarios:
                      
                      if Vendedor['Email'] == Ver_Anuncio['Anunciante']:
        
                        Vendedor['ListaVendas'].append(Ver_Anuncio)
                      
      
                    if contador == 0:
                      
                      print('ID não encontrado. Tente novamente.')
              
            case 2:
    
              Comentario = input('Digite o comentário:\n')
              
              contador = 0
              for Ver_Anuncio in ListaAnuncios:
  
                if Ver_Anuncio['ID'] == Selecionado:
          
                  contador += 1
      
                  Ver_Anuncio['comentários'].append(Usuario['Nome'] + ' - ' + Comentario)
  
                  print('Comentário adicionado com sucesso!')
                  
              if contador == 0:
                print('ID não encontrado. Tente novamente.')
          if CompraComent != 1 and CompraComent != 2:
            print('\033[0;31mErro - Opção inválida\033[0;37m')
  
    
      
            
        case 4:
  
          VerListas = int(input('Digite 1 para ver suas compras, 2 para ver suas vendas ou 3 para ver as notificações:\n'))
  
          match VerListas:
    
            case 1:
  
              if len(Usuario['ListaCompras']) > 0:
    
                print('Lista de compras:')
        
                for compras in Usuario['ListaCompras']:
                  print('-'*25)
                  print(f'Nome : {compras["Nome"]}\nTipo : {compras["tipo"]}\nPreco : {compras["preco"]}\nLocal : {compras["local"]}')
                  print('-'*25)
                  
              else:
                print('Você ainda não comprou nenhum produto.')
                
            case 2:
  
              if len(Usuario['ListaVendas']) > 0:
    
                print('Lista de vendas')
        
                for vendas in Usuario['ListaVendas']:
                  print('-'*25)
                  print(f'Nome : {vendas["Nome"]}\nTipo : {vendas["tipo"]}\nPreco : {vendas["preco"]}\nLocal : {vendas["local"]}')
                  print('-'*25)
                  
              else:
                print('Você ainda não vendeu nenhum produto.')
      
            case 3:
            
              if Usuario['Notificações'] != []:
      
                print('Notificações')
                  
                for Notificacoes in Usuario['Notificações']:                
                  print('-'*40)
                  print(Notificacoes)
                  print('-'*40)
      
                Apagar = int(input('Digite 1 para apagar as notificações ou 2 para não apagar:\n'))
      
                if Apagar == 1:
      
                  Usuario['Notificações'].clear()
                  print('Notificações apagadas com sucesso!')
                  
                elif Apagar == 2:
                  continue    
                
              else:
                print('Não há notificações')
  
          if VerListas != 1 and VerListas != 2 and VerListas != 3:
            print('\033[0;31mErro - Opção inválida\033[0;37m')
              
              
        case 5:
          import main
          main.main()  
        
      if operacao != 1 and operacao != 2 and operacao != 3 and operacao != 4 and operacao != 5:
          print('Opção inválida')
  
    except:
      print('\033[0;31mErro - Opção inválida\033[0;37m')