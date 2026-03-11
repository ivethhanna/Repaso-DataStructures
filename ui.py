import os

RESET  = "\033[0m"
BOLD   = "\033[1m"
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
WHITE  = "\033[97m"
GRAY   = "\033[90m"

def clr(text, *codes):
    return "".join(codes) + str(text) + RESET

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input(clr("\n  Presiona ENTER para continuar...", GRAY))

def hr(char="─", width=68, color=GRAY):
    print(clr(char * width, color))

def header(title, subtitle=""):
    clear()
    hr("=", 68, CYAN)
    print(clr(f"  {title}", BOLD, WHITE))
    if subtitle:
        print(clr(f"  {subtitle}", GRAY))
    hr("=", 68, CYAN)
    print()

def ok(msg):
    print(clr(f"\n  [OK]    {msg}", GREEN, BOLD))

def err(msg):
    print(clr(f"\n  [ERROR] {msg}", RED, BOLD))

def info(msg):
    print(clr(f"\n  [INFO]  {msg}", CYAN))

def ask(prompt):
    return input(clr(f"  --> {prompt}: ", CYAN)).strip()

def ask_int(prompt, lo=None, hi=None):
    while True:
        raw = ask(prompt)
        try:
            val = int(raw)
            if (lo is None or val >= lo) and (hi is None or val <= hi):
                return val
            err(f"Ingresa un numero entre {lo} y {hi}")
        except ValueError:
            err("Valor invalido, ingresa un entero")

def ask_float(prompt):
    while True:
        raw = ask(prompt)
        try:
            val = float(raw)
            if val >= 0:
                return val
            err("El valor debe ser mayor o igual a 0")
        except ValueError:
            err("Valor invalido, ingresa un decimal")

def print_table(products):
    if not products:
        print(clr("  (sin productos)", GRAY))
        return
    col = [10, 26, 10, 12, 12]
    print(
        f"  {clr('CODIGO'.ljust(col[0]), YELLOW, BOLD)}"
        f"{clr('NOMBRE'.ljust(col[1]), YELLOW, BOLD)}"
        f"{clr('CANTIDAD'.ljust(col[2]), YELLOW, BOLD)}"
        f"{clr('PRECIO'.ljust(col[3]), YELLOW, BOLD)}"
        f"{clr('TOTAL'.ljust(col[4]), YELLOW, BOLD)}"
    )
    hr()
    for p in products:
        total = p["qty"] * p["price"]
        price_str = "$" + f"{p['price']:.2f}"
        total_str = "$" + f"{total:.2f}"
        print(
            f"  {clr(p['code'].ljust(col[0]), CYAN)}"
            f"{p['name'].ljust(col[1])}"
            f"{clr(str(p['qty']).ljust(col[2]), GREEN)}"
            f"{clr(price_str.ljust(col[3]), WHITE)}"
            f"{clr(total_str.ljust(col[4]), GRAY)}"
        )
    hr()
    print(clr(f"  Total de productos: {len(products)}", GRAY))
