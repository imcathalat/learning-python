class Dog:

    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name ## class attribute called name
        self.age = age ## class attribute called age

    ## self é a variável que faz referência à instancia da classe (ou seja, ao objeto criado pela classe)
    ## name e age são atributos da instancia
    ## instancia é o ato de criar um objeto, mas um objeto só permanece objeto se for instanciado, ou há algum método pra manter um objeto da classe mesmo sem sua instancia(criação)?