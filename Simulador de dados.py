def dados():
    """ Simulador de dados
    Arroja 2 numero aleatorios entre el 1 y el 6
    Devuelve la suma de ambos numeros"""    

    #importar random para obtener los numeros aleatorios
    import random
    dado1= int (random.random()*6)+1
    dado2= int (random.random()*6)+1
    print ("\n________Bienvenidos al simulador de dados!________\n")
    print ("Dado1:", dado1)
    print ("Dado2:", dado2)

    #sumar ambos numeros
    print ("La suma de ambos dados es:", dado1 + dado2)
    
    #interactuar con el usuario para saber si desea volver a tirar los "dados"
    retry= input ("Desea volver a tirar los dados? SI/NO: ").lower().strip()
    
    while retry not in ["si", "s", "no", "n"]:

        retry= input ("Desea volver a tirar los dados? SI/NO: ").lower().strip()
        
    else:
        if retry in ["si", "s"]:
            dados()
            
            
        elif retry in ["no", "n"]:
            print("\nMuchas gracias y vuelva pronto!")

dados()

#version mejorada