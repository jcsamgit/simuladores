
def introduccion(): 
    print("Bienvenidos al TA-TE-TI".center(44,"_"))
    print("\n>>>Reglas del juego<<<")
    print("Solo se admiten 2 jugadores; el jugador 1 elige que simbolo que desea usar, luego cada uno, en su turno, debe elegir su posicion ingresando un numero del 1 al 9")
    print("Para ganar se debe poder alinear en linea recta(ya sea una linea horizontal, vertical o diagonal) 3 simbolos iguales, si se llena el tablero sin poder cumplir el objetivo el juego termina en empate \n")

    p= [['7','8','9'], ['4','5','6'],['1','2','3']] 
    for fila in p:  #imprimir tabla con numeros posicionales
        for i in range(len(fila)):
            if i== len(fila)-1:
                print("|"+fila[i], end="|\n")
            else:
                print("|"+fila[i], end="")

    print("Para elegir las posiciones solo debe ingresar el numero correspondiente")
    print('(Las "X" empiezan primero) \n')
introduccion()

def tateti():
    m= [['_','_','_'], ['_','_','_'],['_','_','_']]
    simbolo= input('Elija que simbolo desea utilizar: X | O \n').lower().strip() #elegir simbolo
    jugador_1=True

    while simbolo not in ["x","o"]:
        print("el simbolo ingresado es invalido, por favor intente nuevamente".center(77,"-"))
        simbolo= input('Elija que simbolo desea utilizar: X | O \n').lower().strip()
    else:
        if simbolo in "o":
            print('\nEl jugador 2 ("X") empieza la partida')
            jugador_1= not jugador_1
        else:
            print('\nEl jugador 1 ("x") empieza la partida')


    def tabla():#imprimir tabla
        for fila in m:
            for i in range(len(fila)):
                if i== len(fila)-1:
                    print("|"+fila[i], end="|\n")
                else:
                    print("|"+fila[i], end="")
        print()
    tabla()

    x="X"
    o="O"

    def dibujar(s): #"s" de simbolo "X" o "O" para luego dibujar en la tabla
        turno= input("Elija una posicion: ").strip()
        num= str([x for x in range(10)])

        while turno not in num:
            print("La posicion es invalida, por favor intente nuevamente".center(70,"-"))
            turno= input("Elija una posicion: ").strip()
        else:
            if turno == "1" and m[2][0]=="_":
                m[2][0]= s
            elif turno == "2" and m[2][1]=="_":
                m[2][1]= s
            elif turno == "3" and m[2][2]=="_":
                m[2][2]= s
            elif turno == "4" and m[1][0]=="_":
                m[1][0]= s
            elif turno == "5" and m[1][1]=="_":
                m[1][1]= s
            elif turno == "6" and m[1][2]=="_":
                m[1][2]= s
            elif turno == "7" and m[0][0]=="_":
                m[0][0]= s
            elif turno == "8" and m[0][1]=="_":
                m[0][1]= s
            elif turno == "9" and m[0][2]=="_":
                m[0][2]= s
            else:
                print("Posicion ocupada o invalida")
                if contador %2==0:
                    dibujar(o)
                else:
                    dibujar(x)

    contador=1
    while contador < 11:
        x1=[x,x,x]                              #variables que indican los casos en que se pueden ganar la partida
        x2= m[0][0] +m[1][0] +m[2][0] ==x*3
        x3= m[0][1] +m[1][1] +m[2][1] ==x*3  
        x4= m[0][2] +m[1][2] +m[2][2] ==x*3  
        x5= m[0][0] +m[1][1] +m[2][2] ==x*3  
        x6= m[0][2] +m[1][1] +m[2][0] ==x*3  

        o1=[o,o,o]
        o2= m[0][0] +m[1][0] +m[2][0] ==o*3
        o3= m[0][1] +m[1][1] +m[2][1] ==o*3  
        o4= m[0][2] +m[1][2] +m[2][2] ==o*3  
        o5= m[0][0] +m[1][1] +m[2][2] ==o*3  
        o6= m[0][2] +m[1][1] +m[2][0] ==o*3  
        
        if o1 in m or True in [o2,o3,o4,o5,o6]:# verifica si las "o" estan alineadas
            if simbolo == "o":
                print('El jugador 1 ("O") gana la partida'.center(50,"-"))
            else:
                print('El jugador 2 ("O") gana la partida'.center(50,"-"))
            print("\nGracias por jugar, vuelva pronto!")
            break
        elif x1 in m or True in [x2,x3,x4,x5,x6]: #verifica si las "x" estan alineadas
            if simbolo == "o":
                print('El jugador 2 "(X)" gana la partida'.center(50,"-"))
            else:
                print('El jugador 1 "(X)" gana la partida'.center(50,"-"))
            print("\nGracias por jugar, vuelva pronto!")
            break
        else: #verifica si el tablero esta lleno para declarar el empate
            if contador==10:
                print("JUEGO EMPATADO".center(33,"-"))
                print("Gracias por jugar, vuelva pronto!")
                break
            if jugador_1==True: #intercambia los turnos
                print("***Turno del jugador 1***")
                jugador_1= not jugador_1
            else:
                print("***Turno del jugador 2***")
                jugador_1= not jugador_1

        if contador % 2 ==0:
            dibujar(o)
            tabla()
            
        else:
            dibujar(x)
            tabla()
            
        contador+=1

tateti()

# agregar opcion de continuar jugando y de matar al programa con control c



