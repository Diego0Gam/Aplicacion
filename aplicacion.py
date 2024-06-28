import random #Importamos el elemento "Random" de un modulo

opciones = ["Piedra", "Papel", "Tijeras"] #Definimos la lista de opciones

for i in opciones: #Mostramos la lista  
    print(i)

print("Presiona Enter para ingresar") #La linea 8 y 9 son meramente esteticas
input()

def piedra(): #Definimos todas las posibilidades en caso de que el usuario elija "Piedra"
    if maquina == seleccion_cap:
       print("Es un empate")
    elif maquina == "Tijeras":
       print("Ganaste, Piedra rompe Tijeras")
    elif maquina == "Papel":
       print("Perdiste, Papel envuelve Piedra")

def papel(): #Definimos todas las posibilidades en caso de que el usuario elija "Papel"
    if maquina == seleccion_cap:
        print("Es un empate")
    elif maquina == "Piedra":
        print("Ganaste, Papel envuelve Piedra")
    elif maquina == "Tijeras":
        print("Perdiste, Tijeras cortan Papel")

def tijeras(): #Definimos todas las posibilidades en caso de que el usuario elija "Tijeras"
    if maquina == seleccion_cap:
        print("Es un empate")
    elif maquina == "Papel":
        print("Ganaste, Tijeras cortan Papel")
    elif maquina == "Piedra":
        print("Perdiste, Piedra rompe Tijeras")

while True: #Iniciamos un ciclo "While"

    print("1. Jugar | 2.Salir") #Le mostramos al usuario el menu
    menu = str(input()) #Guardamos la seleccion de el usuario en una variable, esta ubicado de esta forma debido a razones esteticas

    if menu == "1": #Si el usuario selecciona "1" se le muestran las dificultades a elegir
        print("1.Facil | 2.Normal | 3.Dificil")
        dificultad = str(input()) #Guardamos la seleccion de el usuario en una variable, esta ubicado de esta forma debido a razones esteticas
        if dificultad == "1":
            print("Piedra | Papel | Tijeras") #Se le muestran las opciones a elegir al usuario
            seleccion = str(input()) #Guardamos la seleccion de el usuario en una variable, esta ubicado de esta forma debido a razones esteticas
            seleccion_cap = seleccion.capitalize() #Hacemos que la seleccion del usuario pase a tener solo la primera letra en mayusculas
            if seleccion_cap == "Piedra":
                prioridad = [1, 1, 5] #Creamos una lista con valores numericos
                maquina = random.choices(opciones, weights=prioridad)[0] #Vinculamos la lista "Opciones" con la lista "Prioridad" y pasamos la lista "Prioridad" como el "peso" de la lista "Opciones", a continuacion el programa selecciona uno de los elementos de la lista "Opciones" dependiendo de la dificultad
                print(f"La maquina eligio: {maquina}") #Se muestra en pantalla lo que elegio la maquina
                piedra() #Se llama a la funcion "Piedra()"
            elif seleccion_cap == "Papel": 
                prioridad = [5, 1, 1]
                maquina = random.choices(opciones, weights=prioridad)[0]
                print(f"La maquina eligio: {maquina}")
                papel()
            elif seleccion_cap == "Tijeras":
                prioridad = [1, 5, 1]
                maquina = random.choices(opciones, weights=prioridad)[0]
                print(f"La maquina eligio: {maquina}")
                tijeras()
            else: #En caso de que el usuario ingrese un valor incorrecto se enviara un mensaje de error
                print("Opcion no valida")
        elif dificultad == "2": #La misma estructura que la dificultad facil, solo cambian los valores numericos de la lista "prioridad"
            print("Piedra | Papel | Tijeras")
            seleccion = str(input())
            seleccion_cap = seleccion.capitalize()
            if seleccion_cap == "Piedra":
                prioridad = [1, 1, 1]
                maquina = random.choices(opciones, weights=prioridad)[0]
                print(f"La maquina eligio: {maquina}")
                piedra()
            elif seleccion_cap == "Papel":
                prioridad = [1, 1, 1]
                maquina = random.choices(opciones, weights=prioridad)[0]
                print(f"La maquina eligio: {maquina}")
                papel()
            elif seleccion_cap == "Tijeras":
                prioridad = [1, 1, 1]
                maquina = random.choices(opciones, weights=prioridad)[0]
                print(f"La maquina eligio: {maquina}")
                tijeras()
            else:
                print("Opcion no valida")
        elif dificultad == "3": #La misma estructura que la dificultad facil, solo cambian los valores numericos de la lista "prioridad"
            print("Piedra | Papel | Tijeras")
            seleccion = str(input())
            seleccion_cap = seleccion.capitalize()
            if seleccion_cap == "Piedra":
                prioridad = [1, 5, 1]
                maquina = random.choices(opciones, weights=prioridad)[0]
                print(f"La maquina eligio: {maquina}")
                piedra()
            elif seleccion_cap == "Papel":
                prioridad = [1, 1, 5]
                maquina = random.choices(opciones, weights=prioridad)[0]
                print(f"La maquina eligio: {maquina}")
                papel()
            elif seleccion_cap == "Tijeras":
                prioridad = [5, 1, 1]
                maquina = random.choices(opciones, weights=prioridad)[0]
                print(f"La maquina eligio: {maquina}")
                tijeras()
            else:
                print("Opcion no valida")
        else:
            print("Opcion no valida")
    elif menu == "2": #En caso de que el usuario seleccione "2" en el menu, se enviara un mensaje y se dara por terminado el programa
        print("Ten un buen dia")
        break
    else: #En caso de que el usuario ingrese un valor incorrecto se enviara un mensaje de error
        print("Opcion no valida")

#Explicacion de las dificultades:
#Se crea y se vincula la lista "prioridad" para usarla como porcentaje para los distintos elementos de la lista "opciones"
#Mientras mas alto sea el valor en la lista "prioridad" mas probabilidades tiene de salir su elemento correspondiente
#Ejemplo
#[Piedra, Papel, Tijeras]
#[1, 1, 2] en este caso el elemento "Tijeras" tendria mas probabilidad de salir, debido a que su valor asignado es mas grande
#Los elementos se vinculan dependiendo de su orden

#Todo esto funciona dependiendo de la dificultad y la eleccion del usuario
#Facil: Hay mas posibilidades de que salga el elemento que sea Inferior al que eligio el usuario
#Normal: Todos los elementos tiene la misma probabilidad de salir
#Dificil:  Hay mas posibilidades de que salga el elemento que sea Superior al que eligio el usuario