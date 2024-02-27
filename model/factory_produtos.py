from categoriasProduto import *
from PersistenciaAnuncios import PersistenciaAnuncios
from PersistenciaUsuários import PersistenciaUsuarios

#import 

#tipagem do produto

class FabricaOlX:
  
  def criarProduto(self, construtores, nome, Tipo_requerido, descricao, preco, quantidade, EstadoUso):

      constructor = construtores.get(Tipo_requerido)
      if constructor:
          return constructor(nome,Tipo_requerido,descricao, preco, quantidade,EstadoUso)
      else:
          print("Tipo de produto não suportado: " + str(Tipo_requerido))
      
  
def Cadastro_Produto(EmailUsuario):

  try:
  
    print('Cadastro de Produtos')
    print('-------------------')
    Nome = input('Nome: ')

    construtores = {
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

    for MostrarTipos in construtores:
      print(f'Tipo {MostrarTipos} - {construtores[MostrarTipos].__name__}')
    Tipo = int(input('\033[0;33mDigite o número referente ao tipo do produto\033[0;37m: '))
  
    EstadoUso = input('Estado de uso: ')
  
    descricao = input('descricao: ')
    
    preco = input('preço: ')
    
    quantidade = input('quantidade: ')
    
    print('-------------------')
    cadastroProdutos = {}

  # python is trash
    t = FabricaOlX()
    object = t.criarProduto(construtores, Nome, Tipo, descricao, preco, quantidade, EstadoUso)
    Anuncios = PersistenciaAnuncios.get_instancia()
    Anuncios.get_Anuncios()
  
    if len(Anuncios.get_Anuncios()) == 0:
      Id = 1
  
    else:
      Id = Anuncios.get_Anuncios()[-1]['ID'] + 1
  
    Usuarios = PersistenciaUsuarios.get_instancia()
    ListaUsuarios = Usuarios.get_usuarios()
  
    for GetAnunciante in ListaUsuarios:
      if GetAnunciante['Email'] == EmailUsuario:
        Anunciante = GetAnunciante['Nome']
        LocalAnunciante = GetAnunciante['local']
  
    cadastroProdutos['ID'] = Id
    cadastroProdutos['EmailAnunciante'] = EmailUsuario
    cadastroProdutos['Anunciante'] = Anunciante
    cadastroProdutos['Nome'] = object.nome
    cadastroProdutos['tipo'] = construtores[Tipo].__name__
    cadastroProdutos['EstadoUso'] = object.estadoUso
    cadastroProdutos['descricao'] = object.descricao
    cadastroProdutos['preco'] = object.preco
    cadastroProdutos['quantidade'] = int(object.quantidade)
    cadastroProdutos['local'] = LocalAnunciante
    cadastroProdutos['comentários'] = []
    
    cadProd = cadastroProdutos.copy()
  
    return cadProd
  except:
    print('\033[31mErro - Ocorreu um erro inesperado, tente novamente\033[37m')
    Cadastro_Produto(EmailUsuario)