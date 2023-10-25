class Bolo:

    def __init__(self, sabor, textura):
        self.sabor = sabor
        self.textura = textura

    def fatiar(self, fatias):
        print(f'Bolo de {self.sabor} fatiado em {fatias} fatias')

meu_bolo1 = Bolo('chocolate', 'fofa')
meu_bolo2 = Bolo("morango", "molenga")

print(meu_bolo1.sabor)
print(meu_bolo2.sabor)
meu_bolo1.fatiar(8)
