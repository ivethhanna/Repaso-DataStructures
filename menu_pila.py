from ui import header, hr, ok, err, info, ask, pause, print_table, clr, YELLOW, BOLD, GRAY, CYAN, GREEN, RED, WHITE
from state import ll, stk, bst


def ver_historial():
    header("HISTORIAL DE OPERACIONES", "Pila (Stack) -- LIFO, maximo 10 entradas")
    ops = stk.to_list()
    if not ops:
        info("La pila esta vacia")
        pause()
        return
    col = [4, 10, 38, 10]
    print(
        f"  {clr('#'.ljust(col[0]),       YELLOW, BOLD)}"
        f"{clr('OPERACION'.ljust(col[1]), YELLOW, BOLD)}"
        f"{clr('DETALLE'.ljust(col[2]),   YELLOW, BOLD)}"
        f"{clr('HORA'.ljust(col[3]),      YELLOW, BOLD)}"
    )
    hr()
    for i, op in enumerate(ops):
        tag   = op["op"]
        tcolor = GREEN if tag == "AGREGAR" else RED if tag == "ELIMINAR" else CYAN
        if tag == "EDITAR":
            detail = f"{op['data']['old']['name']} -> {op['data']['new']['name']}"
        else:
            detail = f"{op['data']['code']} {op['data']['name']}"
        marker = clr("<-- TOPE", YELLOW) if i == 0 else ""
        print(
            f"  {clr(str(i+1).ljust(col[0]), GRAY)}"
            f"{clr(tag.ljust(col[1]), tcolor, BOLD)}"
            f"{detail.ljust(col[2])}"
            f"{clr(op['time'].ljust(col[3]), GRAY)}"
            f"  {marker}"
        )
    hr()
    info(f"Operaciones en pila: {stk.size()} / 10")
    pause()


def deshacer():
    header("DESHACER ULTIMA OPERACION", "Pila -- pop() extrae el tope")
    op = stk.peek()
    if not op:
        err("La pila esta vacia, no hay operaciones que deshacer")
        pause()
        return
    tag = op["op"]
    print(clr(f"\n  Ultima operacion: {tag}", CYAN, BOLD))
    if tag == "EDITAR":
        print(clr(f"  Producto: {op['data']['old']['name']}", WHITE))
    else:
        print(clr(f"  Producto: {op['data']['name']}", WHITE))
    confirm = input(clr("  Deshacer esta operacion? (s/n): ", CYAN)).strip().lower()
    if confirm != "s":
        info("Operacion cancelada")
        pause()
        return
    stk.pop()
    if tag == "AGREGAR":
        code = op["data"]["code"]
        ll.remove(code)
        bst.remove(code)
        ok(f"Se revirtio el AGREGAR: producto {code} eliminado")
    elif tag == "ELIMINAR":
        product = dict(op["data"])
        ll.add(product)
        bst.insert(dict(product))
        ok(f"Se revirtio el ELIMINAR: producto {product['code']} restaurado")
    elif tag == "EDITAR":
        old = op["data"]["old"]
        new_code = op["data"]["new"]["code"]
        ll.update(new_code, old)
        bst.remove(new_code)
        bst.insert(dict(old))
        ok(f"Se revirtio el EDITAR: producto {new_code} restaurado a valores anteriores")
    pause()


def menu_pila():
    while True:
        header("MODULO: PILA (HISTORIAL)", "Stack -- LIFO")
        print(clr("  [1]", YELLOW, BOLD) + "  Ver historial de operaciones")
        print(clr("  [2]", YELLOW, BOLD) + "  Deshacer ultima operacion")
        print(clr("  [0]", GRAY)         + "  Volver")
        print()
        op = input(clr("  --> Opcion: ", CYAN)).strip()
        if op == "1": ver_historial()
        elif op == "2": deshacer()
        elif op == "0": break
        else: err("Opcion invalida")
