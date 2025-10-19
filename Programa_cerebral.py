# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 16:20:25 2025

@author: Carlos Gil
"""

estructuras_cerebrales ={

'cuerpo calloso': 'El cuerpo calloso une los dos hemisferios cerebrales',
'sustancia nigra':'Cuerpos de dopamina mesolímbica que regulan la motricidad corporal',
'corteza prefrontal': 'Estructura encargada de la función ejecutiva',
'ganglio basal': 'Estructuras relacionadas a control motriz y aprendizaje motor',
'nucleo accumbens':'Centro de apego y relaciones que expresa OTR y VPR'
}


def mostrar_menu():
    print("Seleccione una estructura cerebral para más información:\n")
    for i, estructura in enumerate(estructuras_cerebrales.keys(), 1):
        print(f"{i}. {estructura}")
    print("\n")

def buscar_informacion(opcion):
    estructuras = list(estructuras_cerebrales.keys())
    estructura_seleccionada = estructuras[opcion - 1]
    return estructuras_cerebrales[estructura_seleccionada]

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Ingrese el número de la estructura de su interes: "))
            if 1 <= opcion <= 5:
                informacion = buscar_informacion(opcion)
                print(f"\nInformación sobre {list(estructuras_cerebrales.keys())[opcion - 1]}: \n{informacion}\n")
            else:
                print("Por favor, ingrese un número entre 1 y 5.\n")
        except ValueError:
            print("Ingrese un número entre 1 y 5.\n")

        continuar = input("¿Desea seleccionar otra estructura? (si/no): ").lower()
        if continuar != 'si':
            print("¡Gracias por usar el programa!, ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()