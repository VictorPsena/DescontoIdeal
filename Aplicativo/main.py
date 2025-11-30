from kivy.app import App
from kivy.lang import Builder
from Funcoes.Ffuncoes import TaxaBandeira, calcular_precos, ldp
from kivy.properties import StringProperty
KV = """
BoxLayout:
    orientation: "vertical"
    padding: 10
    spacing: 10

    TextInput:
        id: entrada1
        hint_text: "Qual é a bandeira do cartão? (d/c)"
        size_hint_y: None
        height: 40

    TextInput:
        id: entrada2
        hint_text: "Débito ou Crétido? (e/v/m/h)"
        size_hint_y: None
        height: 40

    TextInput:
        id: entrada3
        hint_text: "Número de parcelas"
        size_hint_y: None
        height: 40

    TextInput:
        id: entrada4
        hint_text: "Valor da compra"
        size_hint_y: None
        height: 40

    Button:
        text: "Enviar"
        on_release: app.processar()
        size_hint_y: None
        size_hint_x: None
        height: 40
        width: 80
        pos_hint: {"center_x": 0.5}

    Label:
        id: resultado
        text: "Resultado aparecerá aqui"
        text_size: self.width, None
        halign: "center"
        valign: "middle"
        height: self.texture_size[1]
"""

class MeuApp(App):
    resultado = StringProperty("Resultado")
    def build(self):
        return Builder.load_string(KV)

    def processar(self):
        e1 = self.root.ids.entrada1.text
        e2 = self.root.ids.entrada2.text
        e3 = self.root.ids.entrada3.text
        e4 = self.root.ids.entrada4.text

        # Aqui você envia para sua função (model)
        lista = self.process_inputs(e1, e2, e3, e4)
        self.texto = f'Preço a vista no PIX: R${format(lista[6], ".2f").replace(".",",")} \n   Preço Ideal: R${format(lista[2], ".2f").replace(".",",")}\n Desconto Máximo: R${format(lista[3], ".2f").replace(".",",")} \n Lucro: R${format(lista[0], ".2f").replace(".",",")} \n  Lucro mínimo: R${format(lista[4], ".2f").replace(".",",")} \n Margem de lucro: {format(lista[1], ".2f").replace(".",",")}%  \n Tarifa da maquininha: R${format(lista[5], ".2f").replace(".",",")}'
        self.root.ids.resultado.text = self.texto

    def process_inputs(self, band, db, NumPar, ValComp):
        bandeira = band.lower().strip()[0]
        lista =  ['e', 'v', 'm', 'h']
        try:
            lista.index(band)
        except (ValueError, TypeError):
            print('ERRO')
        DebCred = db.lower().strip()[0]
        lista = ['d', 'c']
        try:
            lista.index(DebCred)
        except (ValueError, TypeError):
            print('ERRO')

        parcelas = int(NumPar)

        taxa = TaxaBandeira(str(bandeira), parcelas, DebCred)
        lista_ldp = ldp(float(ValComp), str(bandeira), float(taxa))
        for i in range(len(lista_ldp)):
            print(lista_ldp[i])
        return lista_ldp

MeuApp().run()