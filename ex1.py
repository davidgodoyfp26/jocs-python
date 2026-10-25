"""
Crea un aplicatiu en python que et mostri un menú que permeti escollir jugar a un dels següents diferents jocs:
Pedra - Paper - Tisores: Guanyador el primer que arriba a 3 punts. (2p)
El ‘Penjat’ - ‘Ahorcado’: (3p)
El programa partirà d’una llista de 20 paraules d’entre 3 i 7 lletres obtingudes d’una llista.
Aleatòriament es seleccionarà una de les 30 paraules.
L’usuari disposarà de número de lletres de la paraula * 2 intents per adivinar-la.
S’anirà mostrant abans de cada intent el tauler típic: R _ _ _ _

Tres en ratlla (2p)
BlackJack (3p)
"""

# Variables
import random
import os

# Activar colores ANSI también en consolas de Windows compatibles.
if os.name == "nt":
  import ctypes
  salida = ctypes.windll.kernel32.GetStdHandle(-11)
  modo = ctypes.c_uint32()
  if ctypes.windll.kernel32.GetConsoleMode(salida, ctypes.byref(modo)):
    ctypes.windll.kernel32.SetConsoleMode(salida, modo.value | 0x0004)

ROJO = "\033[91m"
VERDE = "\033[92m"
CIAN = "\033[96m"
RESET = "\033[0m"

def colorear_casilla(casilla):
  if casilla == "X":
    return ROJO + casilla + RESET
  if casilla == "O":
    return VERDE + casilla + RESET
  if casilla.isdigit():
    return CIAN + casilla + RESET
  return casilla


# Funciones
#------------------------------------------ MENU PRINCIPAL
def menu_principal():
  while True:
    print("---Menu---\n0 - Salir\n1 - Piedra/papel/tijeras\n2 - Ahorcado\n3 - Tres en ralla\n4 - blackjack\n----------")
    try:
      opcion=int(input("Opcion: "))
      if opcion not in (0, 1, 2, 3, 4):
        print("Error: selecciona un número de 0 a 4.")
        continue
      break
    except:
      print("Valor no reconocido.")
  return opcion
#------------------------------------------ MENU JUGADORES
def menu_jugadores():
  while True:
    print("---Menu---\n0 - Salir\n1 - Un jugador\n2 - Dos Jugadores\n----------")
    try:
      opcion_jugadores=int(input("Opcion: "))
      if opcion_jugadores not in (0, 1, 2):
        print("Error: selecciona 0, 1 o 2.")
        continue
      break
      if opcion_jugadores==0:
        break
    except:
      print("Valor no reconocido.")
  return opcion_jugadores
#------------------------------------------ PIEDRA PAPEL TIJERA
def juego1_1jugador(): # ------------------ OBLIGATORIO
  # VARIABLES
  turnos_ganados=0
  turnos_perdidos=0
  turnos_empate=0
  TURNOS=0
  # CODIGO
  while True and turnos_ganados < 3 and turnos_perdidos < 3:
    TURNOS+=1
    print("JUEGO --> PIEDRA PAPEL TIJERA\nEl primero en llegar a 3 gana.\n-----------\nOpciones\n-----------\n1 - Tijera\n2 - Papel\n3 - Piedra\n-----------")
    try:
      objeto=int(input("Opcion: "))
      if objeto not in (1, 2, 3):
        TURNOS-=1
        print("Opción no válida. Elige 1, 2 o 3.")
        continue
      objetos_lista={
          1:{"GANA":2,"PIERDE":3},
          2:{"GANA":3,"PIERDE":1},
          3:{"GANA":1,"PIERDE":2},
      }
      opcion_maquina=random.randint(1,3)
      if objetos_lista[objeto]["GANA"]==opcion_maquina:
        print(f"Resultado ronda {TURNOS}: GANAS")
        turnos_ganados+=1
      elif objetos_lista[objeto]["PIERDE"]==opcion_maquina:
        print(f"Resultado ronda {TURNOS}: PIERDES")
        turnos_perdidos+=1
      else:
        print(f"Resultado ronda {TURNOS}: EMPATE")
        turnos_empate+=1
    except:
      print("Error de la opcion selecionada")
      TURNOS-=1
  if turnos_ganados==3:
    print(f"RESULTADOS: GANASTE \nTURNOS: {TURNOS} \nGANASTE: {turnos_ganados}\nPERDISTE: {turnos_perdidos}\nEMPATES: {turnos_empate}")
  elif turnos_perdidos==3:
    print(f"RESULTADOS: PERDISTE \nTURNOS: {TURNOS} \nGANASTE: {turnos_ganados}\nPERDISTE: {turnos_perdidos}\nEMPATES: {turnos_empate}")

#------------------------------------------ AHORCADO
def juego2_1jugador(): # ------------------ OBLIGATORIO
  import random
  # VARIABLES
  paraules = [
    "sol", "mar", "cel", "gat", "casa",
    "lluna", "arbre", "flor", "porta", "taula",
    "cadira", "llibre", "paper", "escola", "cami",
    "jardi", "nuvol", "pedra", "bosc", "ocell"
  ]
  abc = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i",
    "j", "k", "l", "m", "n", "ñ", "o", "p", "q",
    "r", "s", "t", "u", "v", "w", "x", "y", "z"
  ]
  palabra=paraules[random.randint(0,19)]
  turnos=0
  aciertos=0
  letras_usadas=[]
  # CODIGO
  while True:
    print(letras_usadas)
    for caracteres in palabra:
      if caracteres in letras_usadas:
          print(caracteres, end=" ")
      else:
          print("_", end=" ")

    print()
    print(f"Turno: {turnos}")
    letra_jugador=input("Imprime una letra: ").lower()
    if letra_jugador not in abc:
      print("Introduce una sola letra válida.")
      continue
    if letra_jugador in letras_usadas:
      print("Esta letra ya la usaste.")
      continue
    if letra_jugador in letras_usadas:
      None
    else:
      for caracteres in palabra:
        if caracteres == letra_jugador:
          aciertos+=1
          print("Has acertado")
          print(f"Palabra={len(palabra)}, ACIERTOS: {aciertos}")
    if letra_jugador in abc:
      if not letra_jugador in letras_usadas:
        letras_usadas.append(letra_jugador)
      else:
        print("Esta letra ya la usaste.")
    else:
      print("Esto no es una letra.")
    if int(len(palabra))==aciertos or turnos==len(palabra)*2:
      break
    turnos+=1


    if turnos >= len(palabra)*2:
      break

  # RESULTADO DEL AHORCADO
  print("\nLa palabra era:", palabra)
  if aciertos == len(palabra):
    print("¡Has ganado! Intentos utilizados:", turnos + 1)
  else:
    print("Has perdido. Se han agotado los", len(palabra)*2, "intentos.")

#------------------------------------------ TRES EN RALLA
def juego3_2jugador(): # ------------------ OBLIGATORIO
  print("Juego2 Jugadores3")

  tablero = [" "] * 9
  combinaciones = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
  ]
  jugador_actual = "X"
  turnos = 0

  while True:
    # Enseñar los números de las casillas que siguen libres.
    visible = [str(i + 1) if tablero[i] == " " else tablero[i] for i in range(9)]
    visible = [colorear_casilla(casilla) for casilla in visible]
    print("Casillas libres en cian | X en rojo | O en verde")
    print("\n--- TRES EN RAYA ---")
    print(f" {visible[0]} | {visible[1]} | {visible[2]} ")
    print("---+---+---")
    print(f" {visible[3]} | {visible[4]} | {visible[5]} ")
    print("---+---+---")
    print(f" {visible[6]} | {visible[7]} | {visible[8]} ")

    try:
      posicion = int(input(f"Jugador {jugador_actual}, elige casilla (1-9): "))
    except ValueError:
      print("Debes introducir un número del 1 al 9.")
      continue

    if posicion < 1 or posicion > 9:
      print("La casilla debe estar entre 1 y 9.")
      continue
    if tablero[posicion - 1] != " ":
      print("La casilla ya está ocupada.")
      continue

    tablero[posicion - 1] = jugador_actual
    turnos += 1

    if any(all(tablero[i] == jugador_actual for i in linea) for linea in combinaciones):
      print(f"\n¡Ha ganado el jugador {jugador_actual}!")
      break
    if turnos == 9:
      print("\n¡Empate! No quedan casillas libres.")
      break

    jugador_actual = "O" if jugador_actual == "X" else "X"

  # Aplicamos los colores también al tablero final.
  tablero = [colorear_casilla(casilla) for casilla in tablero]
  # Mostrar el tablero también después del último movimiento.
  print(f" {tablero[0]} | {tablero[1]} | {tablero[2]} ")
  print("---+---+---")
  print(f" {tablero[3]} | {tablero[4]} | {tablero[5]} ")
  print("---+---+---")
  print(f" {tablero[6]} | {tablero[7]} | {tablero[8]} ")
#------------------------------------------ BLACKJACK
def juego4_1jugador(): # ------------------ OBLIGATORIO
  # VARIABLES
  Dinero = 1000

  palos = ["Corazones", "Diamantes", "Tréboles", "Picas"]
  valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

  # FUNCIONES
  def calcular_puntos(cartas):
      puntos = 0
      ases = 0

      for carta in cartas:
          valor = carta[0]

          if valor == "A":
              puntos += 11
              ases += 1
          elif valor in ["J", "Q", "K"]:
              puntos += 10
          else:
              puntos += int(valor)

      while puntos > 21 and ases > 0:
          puntos -= 10
          ases -= 1

      return puntos

  # BUCLE PRINCIPAL
  while True:

      # MENÚ DE LA MESA
      if Dinero <= 0:
          print("Te has quedado sin dinero. Fin de la partida.")
          break

      print("\nDinero que traigo:", Dinero)

      while True:
          opcion_mesa = input("\nMESA\n----------\n0 - Retirarme\n1 - Apostar\nOpción: ")

          if opcion_mesa == "0":
              break

          elif opcion_mesa == "1":
              try:
                  apuesta = int(input("¿Cuánto dinero quieres meter?: "))

                  if apuesta > 0 and apuesta <= Dinero:
                      Dinero -= apuesta
                      break
                  else:
                      print("Cantidad no válida.")

              except ValueError:
                  print("Introduce un número válido.")

          else:
              print("Error: escribe 0 para retirarte o 1 para apostar.")

      if opcion_mesa == "0":
          print("Te retiras con", Dinero)
          break

      # REINICIAR BARAJA Y CARTAS
      baraja = []
      cartas_jugador = []
      cartas_crupier = []

      for palo in palos:
          for valor in valores:
              baraja.append((valor, palo))

      # Repartir 2 cartas al jugador y al crupier
      for i in range(2):
          carta = random.choice(baraja)
          cartas_jugador.append(carta)
          baraja.remove(carta)

          carta = random.choice(baraja)
          cartas_crupier.append(carta)
          baraja.remove(carta)

      # TURNO DEL JUGADOR
      while True:
          print("\nCARTAS DEL CRUPIER:")
          print(cartas_crupier[0], "???")

          print("CARTAS DEL JUGADOR:")
          print(*cartas_jugador)
          print("Puntos:", calcular_puntos(cartas_jugador))

          opcion = input("MENU\n----------\n0 - Salir\n1 - Pedir carta\n2 - Doblar\n3 - Plantarme\nOpción: ")

          if opcion == "0":
              Dinero += apuesta
              break

          elif opcion == "1":
              carta = random.choice(baraja)
              cartas_jugador.append(carta)
              baraja.remove(carta)

              if calcular_puntos(cartas_jugador) > 21:
                  print("\nHas superado los 21 puntos. ¡Has perdido!")
                  break

          elif opcion == "2":
              if Dinero < apuesta:
                  print("No tienes suficiente dinero para doblar.")
                  continue

              Dinero -= apuesta
              apuesta *= 2

              carta = random.choice(baraja)
              cartas_jugador.append(carta)
              baraja.remove(carta)
              break

          elif opcion == "3":
              break

          else:
              print("Error: elige una opción de 0 a 3.")

      # SALIR DEL PROGRAMA
      if opcion == "0":
          print("Te retiras con", Dinero)
          break

      # TURNO DEL CRUPIER
      if calcular_puntos(cartas_jugador) <= 21:
          while calcular_puntos(cartas_crupier) < 17:
              carta = random.choice(baraja)
              cartas_crupier.append(carta)
              baraja.remove(carta)

      # RESULTADO FINAL
      puntos_jugador = calcular_puntos(cartas_jugador)
      puntos_crupier = calcular_puntos(cartas_crupier)

      print("\n---------- RESULTADO FINAL ----------")
      print("CARTAS DEL CRUPIER:", *cartas_crupier)
      print("Puntos:", puntos_crupier)

      print("CARTAS DEL JUGADOR:", *cartas_jugador)
      print("Puntos:", puntos_jugador)

      if puntos_jugador > 21:
          print("HA GANADO EL CRUPIER. El jugador supera 21 puntos.")

      elif puntos_crupier > 21:
          print("HA GANADO EL JUGADOR. El crupier supera 21 puntos.")
          Dinero += apuesta * 2

      elif puntos_jugador > puntos_crupier:
          print("HA GANADO EL JUGADOR por", puntos_jugador - puntos_crupier, "puntos.")
          Dinero += apuesta * 2

      elif puntos_crupier > puntos_jugador:
          print("HA GANADO EL CRUPIER por", puntos_crupier - puntos_jugador, "puntos.")

      else:
          print("EMPATE.")
          Dinero += apuesta

      print("\nDinero actual:", Dinero)
#------------------------------------------
# Codigo

# Menu
while True:
  opcion=menu_principal()
  if opcion==0:
    break
  elif opcion==1: # ------------------------ PIEDRA PAPEL TIJERA
    juego1_1jugador()
  elif opcion==2: # ------------------------ AHORCADO
    juego2_1jugador()
  elif opcion==3: # ------------------------ TRES EN RALLA
    juego3_2jugador()
  elif opcion==4: # ------------------------ BACKJACK
    juego4_1jugador()