#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1
 
Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

def ej1():
    # Ejercicios de práctica con números

    '''
    Realice un programa que solicite por consola 2 números
    Calcule la diferencia entre ellos e informe por pantalla
    si el resultado es positivo, negativo o cero.
        
    '''
    numero_1 = int(input("Ingrese el primer número:\n"))

    numero_2 = int(input("Ingrese el segundo número:\n"))

    resta = numero_1 - numero_2

    if resta == 0:
      print("La diferencia es cero",resta)
    elif resta < 0:
      print("La diferencia es negativa",resta)
    elif resta > 0:
      print("La diferencia es positiva",resta)

def ej2():
# Ejercicios de práctica con números

  '''
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el resultado en pantalla.
    
  '''
  numero_1 = int(input("Ingrese el primer número:\n"))

  numero_2 = int(input("Ingrese el segundo número:\n"))

  numero_3 = int(input("Ingrese el tercer número:\n"))

  if (numero_1 % 2) == 0:
    print("El primer número ingresado es par:", numero_1)
  else:
    print("El primer número ingresado es impar:", numero_1)
  if (numero_2 % 2) == 0:
    print("El segundo número ingresado es par:", numero_2)
  else:
    print("El segundo número ingresado es impar:", numero_2)
  if (numero_3 % 2) == 0:
    print("El tercer número ingresado es par:", numero_3)
  else:
    print("El tercer número ingresado es impar:", numero_3)


def ej3():
    # Ejercicios de práctica con números

    '''
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se desea ejecutar
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)

    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    

    '''
    numero_1 = int(input("Ingrese el primer número:\n"))

    numero_2 = int(input("Ingrese el segundo número:\n"))

    operacion = str(input("Que operación matemática desea realizar: "))

    if operacion == "+" :
      suma = numero_1 + numero_2
      print("El resultado de la suma es:",suma)
    elif operacion == "-" :
      resta = numero_1 - numero_2
      print("El resultado de la resta es:",resta)
    elif operacion == "*" :
      multi = numero_1 * numero_2
      print("El resultado de la multiplicación es:",multi)
    elif operacion == "/" :
      division = numero_1 / numero_2
      print("El resultado de la división es:",division)
    elif operacion == "**" :
      expo = numero_1 ** numero_2
      print("El resultado del exponente es:",expo) 

def ej4():
    # Ejercicios de práctica con cadenas
    
    '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)

    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor

    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor

    '''

    palabra_1 = str(input("Ingrese la primer palabra: "))
    palabra_2 = str(input("Ingrese la segunda palabra: "))
    palabra_3 = str(input("Ingrese la tercer palabra: "))

    print("Como desea ordenar las palabras:")
    print("Opción 1, ordena alfabeticamente")
    print("Opción 2, ordena por longitud")
    
    opcion = int(input("Elegí una opción: "))
        
    if opcion == 1:
      if (palabra_1 > palabra_2) and (palabra_1 > palabra_3) and (palabra_2 > palabra_3):
        print("El orden es: " + palabra_1+" " + palabra_2 +" "+palabra_3)
      elif (palabra_1 > palabra_2) and (palabra_1 > palabra_3) and (palabra_3 > palabra_2):
        print("El orden es: " + palabra_1+" " + palabra_3 +" "+palabra_2)
      elif (palabra_2 > palabra_1) and (palabra_2 > palabra_3) and (palabra_1 > palabra_3):
        print("El orden es: " + palabra_2+" " + palabra_1 +" "+palabra_3)
      elif (palabra_2 > palabra_1) and (palabra_2 > palabra_3) and (palabra_3 > palabra_1):
        print("El orden es: " + palabra_2+" " + palabra_3 +" "+palabra_1)
      elif (palabra_3 > palabra_1) and (palabra_3 > palabra_2) and (palabra_1 > palabra_2):
        print("El orden es: " + palabra_3+" " + palabra_1 +" "+palabra_2)
      elif (palabra_3 > palabra_1) and (palabra_3 > palabra_2) and (palabra_2 > palabra_1):
        print("El orden es: " + palabra_3+" " + palabra_2 +" "+palabra_1)
    
    elif opcion == 2:

      letra_1 = int(len(palabra_1))
      letra_2 = int(len(palabra_2))
      letra_3 = int(len(palabra_3))

      #if len(palabra_1) > len(palabra_2) and len(palabra_1) > len(palabra_3) :
        #print("El orden es: " + palabra_1 + " " + palabra_2)
      if (letra_1 > letra_2) and (letra_1 > letra_3) and (letra_2 > letra_3):
        print("El orden es: " + palabra_1+" " + palabra_2 +" "+palabra_3)
      elif (letra_1 > letra_2) and (letra_1 > letra_3) and (letra_3 > letra_2):
        print("El orden es: " + palabra_1+" " + palabra_3 +" "+palabra_2)
      elif (letra_2 > letra_1) and (letra_2 > letra_3) and (letra_1 > letra_3):
        print("El orden es: " + palabra_2+" " + palabra_1 +" "+palabra_3)
      elif (letra_2 > letra_1) and (letra_2 > letra_3) and (letra_3 > letra_1):
        print("El orden es: " + palabra_2+" " + palabra_3 +" "+palabra_1)
      elif (letra_3 > letra_1) and (letra_3 > letra_2) and (letra_2 > letra_3):
        print("El orden es: " + palabra_3+" " + palabra_2 +" "+palabra_1)
      elif (letra_3 > letra_1) and (letra_3 > letra_2) and (letra_1 > letra_2):
        print("El orden es: " + palabra_3+" " + palabra_1 +" "+palabra_2)
      
      print(letra_1)
      print(letra_2)
      print(letra_3)

def ej5():
    # Ejercicios de práctica con números
       
    '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?

    En cada caso imprimir en pantalla el resultado  

    '''
    temp_1 = float(input("Ingrese la primer temperatura: "))
    temp_2 = float(input("Ingrese la segunda temperatura: "))
    temp_3 = float(input("Ingrese la tercer temperatura: "))

    promedio = (temp_1 + temp_2 + temp_3) / 3

    if temp_1 > temp_2 and temp_1 > temp_3 and temp_2 > temp_3:
      print("La temperatura mayor es: ",temp_1)
      print("La temperatura menor es: ",temp_3)
      print("El promedio de las temperaturas es: ",promedio)
    elif temp_1 > temp_2 and temp_1 > temp_3 and temp_3 > temp_2:
      print("La temperatura mayor es: ",temp_1)
      print("La temperatura menor es: ",temp_2)
      print("El promedio de las temperaturas es: ",promedio)
    elif temp_2 > temp_1 and temp_2 > temp_3 and temp_1 > temp_3:
      print("La temperatura mayor es: ",temp_2)
      print("La temperatura menor es: ",temp_3)
      print("El promedio de las temperaturas es: ",promedio)
    elif temp_2 > temp_1 and temp_2 > temp_3 and temp_3 > temp_1:
      print("La temperatura mayor es: ",temp_2)
      print("La temperatura menor es: ",temp_1)
      print("El promedio de las temperaturas es: ",promedio)
    elif temp_3 > temp_1 and temp_3 > temp_2 and temp_2 > temp_1:
      print("La temperatura mayor es: ",temp_3)
      print("La temperatura menor es: ",temp_1)
      print("El promedio de las temperaturas es: ",promedio)
    elif temp_3 > temp_1 and temp_3 > temp_2 and temp_1 > temp_2:
      print("La temperatura mayor es: ",temp_2)
      print("La temperatura menor es: ",temp_2)
      print("El promedio de las temperaturas es: ",promedio)

if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
