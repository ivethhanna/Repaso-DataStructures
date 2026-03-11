import copy
from datetime import datetime
from ui import header, hr, ok, err, info, ask, ask_int, ask_float, pause, print_table, clr, YELLOW, BOLD, GRAY, CYAN, WHITE
from state import ll, stk, bst


def ts():
    return datetime.now().strftime("%H:%M:%S")


def ver_inventario():
    header("INVENTARIO COMPLETO", "Lista Enlazada + Array")
    print_table(ll.to_list())
    info(f"Nodos en lista enlazada: {ll.size}")
    pause()


def agregar_producto():
    header("AGREGAR PRODUCTO", "Lista Enlazada -- insercion al final")
    code = ask("Codigo (ej: P009)").upper()
    if not code:
        err("El codigo no puede estar vacio")
        pause()
        return
    if ll.find(code):
        err(f"Ya existe un producto con codigo {code}")
        pause()
        return
    name  = ask("Nombre")
    if not name:
        err("El nombre no puede estar vacio")
        pause()
        return
    qty   = ask_int("Cantidad", lo=0)
    price = ask_float("Precio")
    product = {"code": code, "name": name, "qty": qty, "price": price}
    ll.add(product)
    bst.insert(dict(product))
    stk.push({"op": "AGREGAR", "data": dict(product), "time": ts()})
    ok(f"Producto {code} agregado correctamente")
    pause()


def eliminar_producto():
    header("ELIMINAR PRODUCTO", "Lista Enlazada -- eliminacion por codigo")
    code = ask("Codigo del producto a eliminar").upper()
    product = ll.find(code)
    if not product:
        err(f"No se encontro el producto con codigo {code}")
        pause()
        return
    print()
    print_table([product])
    confirm = ask("Confirmar eliminacion? (s/n)").lower()
    if confirm != "s":
        info("Operacion cancelada")
        pause()
        return
    snapshot = dict(product)
    ll.remove(code)
    bst.remove(code)
    stk.push({"op": "ELIMINAR", "data": snapshot, "time": ts()})
    ok(f"Producto {code} eliminado")
    pause()


def editar_producto():
    header("EDITAR PRODUCTO", "Lista Enlazada -- actualizacion de nodo")
    code = ask("Codigo del producto a editar").upper()
    product = ll.find(code)
    if not product:
        err(f"No se encontro el producto con codigo {code}")
        pause()
        return
    print()
    print_table([product])
    old_snapshot = dict(product)
    print(clr("\n  Ingresa los nuevos valores (ENTER para conservar el actual):", GRAY))
    name_in = ask(f"Nombre [{product['name']}]")
    qty_str = ask(f"Cantidad [{product['qty']}]")
    price_str = ask(f"Precio [{product['price']}]")
    updates = {}
    if name_in:
        updates["name"] = name_in
    if qty_str:
        try:
            updates["qty"] = int(qty_str)
        except ValueError:
            err("Cantidad invalida, se conserva el valor anterior")
    if price_str:
        try:
            updates["price"] = float(price_str)
        except ValueError:
            err("Precio invalido, se conserva el valor anterior")
    if not updates:
        info("Sin cambios")
        pause()
        return
    ll.update(code, updates)
    updated = ll.find(code)
    bst.remove(code)
    bst.insert(dict(updated))
    stk.push({"op": "EDITAR", "data": {"old": old_snapshot, "new": dict(updated)}, "time": ts()})
    ok(f"Producto {code} actualizado")
    pause()


def ordenar_productos():
    header("ORDENAR INVENTARIO", "Array -- sort con comparador")
    print(clr("  [1]", YELLOW, BOLD) + "  Nombre (A-Z)")
    print(clr("  [2]", YELLOW, BOLD) + "  Nombre (Z-A)")
    print(clr("  [3]", YELLOW, BOLD) + "  Precio (menor a mayor)")
    print(clr("  [4]", YELLOW, BOLD) + "  Precio (mayor a menor)")
    print(clr("  [5]", YELLOW, BOLD) + "  Cantidad (menor a mayor)")
    print(clr("  [6]", YELLOW, BOLD) + "  Cantidad (mayor a menor)")
    op = ask_int("Opcion", lo=1, hi=6)
    products = ll.to_list()
    if op == 1: products.sort(key=lambda p: p["name"])
    if op == 2: products.sort(key=lambda p: p["name"], reverse=True)
    if op == 3: products.sort(key=lambda p: p["price"])
    if op == 4: products.sort(key=lambda p: p["price"], reverse=True)
    if op == 5: products.sort(key=lambda p: p["qty"])
    if op == 6: products.sort(key=lambda p: p["qty"], reverse=True)
    header("RESULTADO DEL ORDENAMIENTO")
    print_table(products)
    pause()


def buscar_por_codigo():
    header("BUSCAR POR CODIGO", "Lista Enlazada -- recorrido secuencial O(n)")
    code = ask("Codigo a buscar").upper()
    product = ll.find(code)
    if product:
        ok(f"Producto encontrado:")
        print_table([product])
    else:
        err(f"No se encontro ningun producto con codigo {code}")
    pause()


def menu_inventario():
    while True:
        header("MODULO: INVENTARIO", "Array + Lista Enlazada")
        print(clr("  [1]", YELLOW, BOLD) + "  Ver inventario completo")
        print(clr("  [2]", YELLOW, BOLD) + "  Agregar producto")
        print(clr("  [3]", YELLOW, BOLD) + "  Eliminar producto")
        print(clr("  [4]", YELLOW, BOLD) + "  Editar producto")
        print(clr("  [5]", YELLOW, BOLD) + "  Ordenar productos")
        print(clr("  [6]", YELLOW, BOLD) + "  Buscar por codigo")
        print(clr("  [0]", GRAY)         + "  Volver")
        print()
        op = ask("Opcion")
        if op == "1": ver_inventario()
        elif op == "2": agregar_producto()
        elif op == "3": eliminar_producto()
        elif op == "4": editar_producto()
        elif op == "5": ordenar_productos()
        elif op == "6": buscar_por_codigo()
        elif op == "0": break
        else: err("Opcion invalida")
