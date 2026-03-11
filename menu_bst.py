from ui import header, hr, ok, err, info, ask, pause, print_table, clr, YELLOW, BOLD, GRAY, CYAN, WHITE
from state import bst


def buscar_bst():
    header("BUSCAR EN ARBOL BST", "Busqueda eficiente O(log n) promedio")
    code = ask("Codigo del producto").upper()
    product = bst.search(code)
    if product:
        ok("Producto encontrado:")
        print_table([product])
    else:
        err(f"No se encontro el codigo {code} en el arbol")
    pause()


def recorrido_inorden():
    header("RECORRIDO INORDEN", "Arbol BST -- izquierda, raiz, derecha")
    products = bst.inorder()
    if not products:
        info("El arbol esta vacio")
        pause()
        return
    info("Productos ordenados por codigo (inorden):")
    print()
    print_table(products)
    pause()


def _print_bst_level(node, prefix="", is_left=True):
    if not node:
        return
    connector = "|-- " if is_left else "\\-- "
    print(clr(f"  {prefix}{connector}", GRAY) + clr(node.product["code"], YELLOW, BOLD) + " " + node.product["name"])
    new_prefix = prefix + ("|   " if is_left else "    ")
    if node.left or node.right:
        if node.left:
            _print_bst_level(node.left,  new_prefix, True)
        if node.right:
            _print_bst_level(node.right, new_prefix, False)


def ver_arbol():
    header("ESTRUCTURA DEL ARBOL BST", "Representacion visual en terminal")
    if not bst.root:
        info("El arbol esta vacio")
        pause()
        return
    print(clr(f"  RAIZ --> ", CYAN, BOLD) + clr(bst.root.product["code"], YELLOW, BOLD) + " " + bst.root.product["name"])
    if bst.root.left:
        _print_bst_level(bst.root.left,  "", True)
    if bst.root.right:
        _print_bst_level(bst.root.right, "", False)
    hr()
    info(f"Total de nodos: {len(bst.inorder())}")
    pause()


def menu_bst():
    while True:
        header("MODULO: ARBOL BINARIO DE BUSQUEDA", "BST ordenado por codigo")
        print(clr("  [1]", YELLOW, BOLD) + "  Buscar producto por codigo")
        print(clr("  [2]", YELLOW, BOLD) + "  Recorrido inorden (productos ordenados)")
        print(clr("  [3]", YELLOW, BOLD) + "  Ver estructura del arbol")
        print(clr("  [0]", GRAY)         + "  Volver")
        print()
        op = input(clr("  --> Opcion: ", CYAN)).strip()
        if op == "1": buscar_bst()
        elif op == "2": recorrido_inorden()
        elif op == "3": ver_arbol()
        elif op == "0": break
        else: err("Opcion invalida")
