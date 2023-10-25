class Dog:

    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name ## class attribute called name
        self.age = age ## class attribute called age

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
    def coat_color(self, coat):
        return f"{self.name}'s coat is {coat}"

    
    ## self é a variável que faz referência à instancia da classe (ou seja, ao objeto criado pela classe)
    ## name e age são atributos da instancia
    ## instancia é o ato de criar um objeto, mas um objeto só permanece objeto se for instanciado, ou há algum método pra manter um objeto da classe mesmo sem sua instancia(criação)?

buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)

