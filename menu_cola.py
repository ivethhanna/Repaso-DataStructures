from datetime import datetime
from ui import header, hr, ok, err, info, ask, pause, clr, YELLOW, BOLD, GRAY, CYAN, GREEN, WHITE
from state import q


def ts():
    return datetime.now().strftime("%H:%M:%S")


def _print_queue():
    orders = q.to_list()
    if not orders:
        info("La cola de pedidos esta vacia")
        return
    col = [6, 20, 32, 10]
    print(
        f"  {clr('POS'.ljust(col[0]),     YELLOW, BOLD)}"
        f"{clr('CLIENTE'.ljust(col[1]),   YELLOW, BOLD)}"
        f"{clr('PRODUCTOS'.ljust(col[2]), YELLOW, BOLD)}"
        f"{clr('HORA'.ljust(col[3]),      YELLOW, BOLD)}"
    )
    hr()
    for i, order in enumerate(orders):
        marker = clr(" <-- FRENTE", GREEN) if i == 0 else ""
        print(
            f"  {clr(str(i+1).ljust(col[0]), GRAY)}"
            f"{order['client'].ljust(col[1])}"
            f"{order['items'].ljust(col[2])}"
            f"{clr(order['time'].ljust(col[3]), GRAY)}"
            f"{marker}"
        )
    hr()
    info(f"Pedidos en cola: {q.size()}")


def ver_cola():
    header("COLA DE PEDIDOS", "Queue -- FIFO")
    _print_queue()
    pause()


def encolar_pedido():
    header("NUEVO PEDIDO", "Queue -- enqueue() al final")
    client = ask("Nombre del cliente")
    if not client:
        err("El nombre no puede estar vacio")
        pause()
        return
    items = ask("Productos solicitados (ej: P001 x2, P003 x1)")
    if not items:
        err("Debe ingresar al menos un producto")
        pause()
        return
    order = {"client": client, "items": items, "time": ts()}
    q.enqueue(order)
    ok(f"Pedido de {client} agregado a la cola (posicion {q.size()})")
    pause()


def atender_pedido():
    header("ATENDER SIGUIENTE PEDIDO", "Queue -- dequeue() del frente")
    if q.is_empty():
        err("No hay pedidos en cola")
        pause()
        return
    order = q.dequeue()
    print(clr("\n  Atendiendo pedido:", GREEN, BOLD))
    print(clr(f"  Cliente  : {order['client']}", WHITE))
    print(clr(f"  Productos: {order['items']}", WHITE))
    print(clr(f"  Ingresado: {order['time']}", GRAY))
    print(clr(f"  Atendido : {ts()}", GRAY))
    if not q.is_empty():
        next_order = q.to_list()[0]
        info(f"Siguiente en cola: {next_order['client']}")
    else:
        info("La cola quedo vacia")
    pause()


def menu_cola():
    while True:
        header("MODULO: COLA DE PEDIDOS", "Queue -- FIFO")
        print(clr("  [1]", YELLOW, BOLD) + "  Ver cola de pedidos")
        print(clr("  [2]", YELLOW, BOLD) + "  Agregar nuevo pedido")
        print(clr("  [3]", YELLOW, BOLD) + "  Atender siguiente pedido")
        print(clr("  [0]", GRAY)         + "  Volver")
        print()
        op = input(clr("  --> Opcion: ", CYAN)).strip()
        if op == "1": ver_cola()
        elif op == "2": encolar_pedido()
        elif op == "3": atender_pedido()
        elif op == "0": break
        else: err("Opcion invalida")
