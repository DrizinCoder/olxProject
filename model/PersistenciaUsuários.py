class PersistenciaUsuarios:
  
  instancia = None

  @classmethod
  def get_instancia(cls):
    if not cls.instancia:
        cls.instancia = cls()
    return cls.instancia

  def __init__(self):
    self.listaUsuarios = []

  def SalvarUsuario(self, usuario):
    self.listaUsuarios.append(usuario)
    
  def get_usuarios(self):
    return self.listaUsuarios
  
  