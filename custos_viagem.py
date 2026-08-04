from abc import ABC, abstractmethod

# Classe base
class Veiculo(ABC):
    @abstractmethod
    def custo_viagem(self, distancia):
        pass


class Carro(Veiculo):
    def __init__(self, consumo_km_l, preco_combustivel):
        self.consumo_km_l = consumo_km_l
        self.preco_combustivel = preco_combustivel

    def custo_viagem(self, distancia):
        litros = distancia / self.consumo_km_l
        return litros * self.preco_combustivel


class Moto(Veiculo):
    def __init__(self, consumo_km_l, preco_combustivel):
        self.consumo_km_l = consumo_km_l
        self.preco_combustivel = preco_combustivel

    def custo_viagem(self, distancia):
        litros = distancia / self.consumo_km_l
        return litros * self.preco_combustivel


class Caminhao(Veiculo):
    def __init__(self, consumo_km_l, preco_diesel):
        self.consumo_km_l = consumo_km_l
        self.preco_diesel = preco_diesel

    def custo_viagem(self, distancia):
        litros = distancia / self.consumo_km_l
        return litros * self.preco_diesel


def custo_total_viagem(veiculos):
    """
    Recebe uma lista de objetos do tipo Veiculo
    e calcula o custo total de uma viagem de 200 km.
    """
    DISTANCIA = 200
    return sum(veiculo.custo_viagem(DISTANCIA) for veiculo in veiculos)


# Exemplo de uso
veiculos = [
    Carro(consumo_km_l=12, preco_combustivel=6.00),
    Moto(consumo_km_l=30, preco_combustivel=6.00),
    Caminhao(consumo_km_l=4, preco_diesel=5.80)
]

total = custo_total_viagem(veiculos)
print(f"Custo total da viagem: R$ {total:.2f}")
