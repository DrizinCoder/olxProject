class PersistenciaAnuncios:

  instancia = None

  @classmethod
  def get_instancia(cls):
    if not cls.instancia:
        cls.instancia = cls()
    return cls.instancia

  def __init__(self):
    self.listaAnuncios = []

  def SalvarProduto(self, produto):
    self.listaAnuncios.append(produto)

  def get_Anuncios(self):
    return self.listaAnuncios

  def info(self, Anuncio):
    
      print('-'*25)
      print(f'Anunciante: {Anuncio["Anunciante"]}')
      print('-'*25)
      print(f'ID do anuncio - {Anuncio["ID"]}')
      print('-'*25)
      print(f'Nome: {Anuncio["Nome"]}')
      print(f'Tipo: {Anuncio["tipo"]}')
      print(f'Estado de uso: {Anuncio["EstadoUso"]}')
      print(f'Descrição: {Anuncio["descricao"]}')
      print(f'Preço: {Anuncio["preco"]}')
      print(f'Quantidade: {Anuncio["quantidade"]}')
      print(f'Localizaçao: {Anuncio["local"]}')
      if Anuncio['comentários'] != []:
        print('-'*25)
        print('Comentários:')
        for comentario in Anuncio['comentários']:
          print(comentario)


  def notificaçoes(self):
    Cont_Notificações = 0
    print('-'*25)
    print(f'Voce tem {len(self.listaAnuncios)} notificações')
    print('-'*25)