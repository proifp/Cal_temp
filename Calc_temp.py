Kelvin = 273.15
Fahrenheit = 32
division = 9/5
division2 = 5/9

def Celsius_Kelvin(Kelvin):
    b = int(input('¿cuantos ªC tienes?: '))
    c = b + Kelvin
    Celsius = d

def Celsius_Fahrenheit(Fahrenheit,division):
    b = int(input('¿cuantos ªC tienes?: '))
    c = b*division
    d = c + Fahrenheit 
    Celsius = d

def Kelvin_Celsius(Kelvin):
    b = int(input('¿cuantos K tienes?: '))
    c = Kelvin - b
    Kelvin = c

def Fahrenheit_Celsius(Fahrenheit,division2,Kelvin):
    b = int(input('¿cuantos ªF tienes?: '))
    c = b - Fahrenheit
    d = c * division2
    Fahrenheit = d

def Fahrenheit_Kelvin(Fahrenheit,division2,Kelvin):
    b = int(input('¿cuantos ªF tienes?: '))
    c = b - Fahrenheit
    d = c * division2
    e = d + Kelvin
    Fahrenheit = e

def Kelvin_Fahrenheit(division,Kelvin,Fahrenheit):
    b = int(input('¿cuantos K tienes?: '))
    c = b - Kelvin
    d = c * division
    e = d + Fahrenheit
    Kelvin = e


while True:
    pregunta = input('¿Que quieres convertir? ªC a K / ªC a ªF / K a ªC / ªF a ªC / K a ªF / ªF a K : ')
    if(pregunta == 'ªC a K'):
        Celsius_Kelvin(Kelvin)
        print(str(Kelvin) + 'K')
        
    if(pregunta == 'ªC a ªF'):
        Celsius_Fahrenheit(Fahrenheit, division)
        print(str(Fahrenheit) + 'ªF')
    if(pregunta == 'ªF a K'):
        Fahrenheit_Kelvin(Fahrenheit, division2, Kelvin)
        print(str(Kelvin) + 'K')

    if(pregunta == 'ªF a ªC'):
        Fahrenheit_Celsius(Fahrenheit, division2, Kelvin)
        print(str(Celsius) + 'ªC')

    if(pregunta == 'K a ªC'):
        Kelvin_Celsius(Kelvin)
        print(str(Celsius) + 'ªC')

    if(pregunta == 'K a ªF'):
        Kelvin_Fahrenheit(division,Kelvin, Fahrenheit)
        print(str(Fahrenheit) + 'ªF')