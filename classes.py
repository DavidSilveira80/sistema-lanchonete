
class Pedido:
    id = 0

    def __init__(self, nome_cliente, taxa_servico):
        Pedido.id += 1
        self.id = Pedido.id
        self.nome_cliente = nome_cliente
        self.taxa_servico = taxa_servico
        self.itens_consumidos = []

    def calcular_total(self):
        soma = 0
        for iten in self.itens_consumidos:
            soma += iten.calcular_preco()
        return soma + self.taxa_servico

    def mostrar_fatura(self):
        print(f'PEDIDO N°: {self.id}')
        print(f'Cliente: {self.nome_cliente}')
        print('ITENS:')
        for iten in self.itens_consumidos:
            if isinstance(iten, Pizza):
                print(f'Pizza: {iten.recheio}   Qtd: {iten.quantidade} X {iten.valor:.2f} = '
                      f'{iten.calcular_preco():.2f} ')
            if isinstance(iten, Salgadinho):
                print(f'Salgadinho: {iten.recheio} {iten.massa} Qtd: {iten.quantidade} X {iten.valor:.2f} = '
                      f'{iten.calcular_preco():.2f}')
            if isinstance(iten, Lanche):
                print(f'Lanche: {iten.recheio} {iten.quantidade} X {iten.valor:.2f} = {iten.calcular_preco():.2f}')
        print(f'Taxa de serviço: {self.taxa_servico:.2f}')
        print(f'Total a pagar: {self.calcular_total():.2f} R$')


class Prato:
    def __init__(self, quantidade):
        self.quantidade = quantidade

    def registrar_consumo(self, iten):
        pedido.itens_consumidos.append(iten)


class Pizza(Prato):
    def __init__(self, molho, recheio, borda, quantidade, valor):
        super().__init__(quantidade)
        self.molho = molho
        self.recheio = recheio
        self.borda = borda
        self.valor = valor

    def calcular_preco(self):
        return self.valor * self.quantidade


class Salgadinho(Prato):
    def __init__(self, recheio, massa, quantidate, valor):
        super().__init__(quantidate)
        self.recheio = recheio
        self.massa = massa
        self.valor = valor

    def calcular_preco(self):
        return self.valor * self.quantidade


class Lanche(Prato):
    def __init__(self, pao, recheio, molho, quantidade, valor):
        super().__init__(quantidade)
        self.pao = pao
        self.recheio = recheio
        self. molho = molho
        self.valor = valor

    def calcular_preco(self):
        return self.valor * self.quantidade


if __name__ == '__main__':
    pedidos = []
    pedido = Pedido('David', 10.0)

    pizza = Pizza('Catupiri', 'Portuguesa', 'Recheada', 2, 30)
    pizza.registrar_consumo(pizza)

    salgado = Salgadinho('Frango', 'Assado',  2, 15)
    salgado.registrar_consumo(salgado)

    lanche = Lanche('Salgado', 'Calabreza', 'Catupiry', 1, 25)
    lanche.registrar_consumo(lanche)
    lanche1 = Lanche('Cervejinha', 'Tudo', 'Chedar', 2, 25)
    lanche1.registrar_consumo(lanche1)
    pedidos.append(pedido)
    print()
    pedido.mostrar_fatura()
    print()
    print()
    pedido1 = Pedido('Daniel', 10)
    pedido1.mostrar_fatura()
    pedidos.append(pedido1)

    print(len(pedidos))


    def buscar_pedido(pedidos, id_pedido):
        for pedido in pedidos:
            if pedido.id == id_pedido:
                return pedido
    print()
    print()
    pedido_encontrado = buscar_pedido(pedidos, 1)

    pedido_encontrado.mostrar_fatura()

