import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from ui import header, hr, ok, err, pause, clr, YELLOW, BOLD, GRAY, CYAN, WHITE, clear
from menu_inventario import menu_inventario
from menu_pila import menu_pila
from menu_cola import menu_cola
from menu_bst import menu_bst
from state import ll, stk, q


def main_menu():
    while True:
        header(
            "SISTEMA DE ADMINISTRACION DE INVENTARIO",
            "Estructuras de Datos -- Array | Lista Enlazada | Pila | Cola | BST"
        )
        print(clr("  [1]", YELLOW, BOLD) + "  Inventario          " + clr("(Array + Lista Enlazada)", GRAY))
        print(clr("  [2]", YELLOW, BOLD) + "  Historial           " + clr("(Pila / Stack)", GRAY))
        print(clr("  [3]", YELLOW, BOLD) + "  Pedidos de clientes " + clr("(Cola / Queue)", GRAY))
        print(clr("  [4]", YELLOW, BOLD) + "  Arbol BST           " + clr("(Arbol Binario de Busqueda)", GRAY))
        print()
        hr()
        print(
            clr("  Productos: ", GRAY) + clr(str(ll.size), YELLOW, BOLD) +
            clr("   |  Operaciones en pila: ", GRAY) + clr(str(stk.size()), YELLOW, BOLD) +
            clr("   |  Pedidos en cola: ", GRAY) + clr(str(q.size()), YELLOW, BOLD)
        )
        hr()
        print(clr("  [0]", GRAY) + "  Salir")
        print()
        op = input(clr("  --> Opcion: ", CYAN)).strip()
        if op == "1": menu_inventario()
        elif op == "2": menu_pila()
        elif op == "3": menu_cola()
        elif op == "4": menu_bst()
        elif op == "0":
            clear()
            print(clr("\n  Hasta luego.\n", YELLOW, BOLD))
            break
        else:
            err("Opcion invalida")


if __name__ == "__main__":
    main_menu()
