from categoriasProduto import *
class FabricaOlx(FabricaProduto):
  def criarProduto(self, tipoProduto, nome, tipo, descricao, preco, quantidade):
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
          11: ComercioeEscritório,
          12: MusicaHobbies,
          13: ArtigosInfantis,
          14: AgroeIndustria,
          15: ModaEbeleza,
          16: AnimaldeaEstimação,
          17: MaterialdeConstrução,
          18: CameraeDrones,
          19: TveVideo,
          20: CelulareseTelefonia,
          21: Informatica
      }

      constructor = construtores.get(tipoProduto)
      if constructor:
          return constructor(nome, tipo, descricao, preco, quantidade)
      else:
          raise ValueError("Tipo de produto não suportado: " + str(tipoProduto))



Tipo = int(input('Digite o número referente ao tipo do produto: '))

