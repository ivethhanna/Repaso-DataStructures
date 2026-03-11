from structures import LinkedList, Stack, Queue, BST

INITIAL_PRODUCTS = [
    {"code": "P001", "name": "Laptop Dell XPS",      "qty": 15, "price": 1299.99},
    {"code": "P002", "name": "Monitor Samsung 27in", "qty": 30, "price":  349.99},
    {"code": "P003", "name": "Teclado Mecanico",     "qty": 50, "price":   89.99},
    {"code": "P004", "name": "Mouse Inalambrico",    "qty": 75, "price":   45.99},
    {"code": "P005", "name": "Auriculares Sony",     "qty": 20, "price":  199.99},
    {"code": "P006", "name": "Webcam Logitech",      "qty": 35, "price":   79.99},
    {"code": "P007", "name": "SSD 1TB Samsung",      "qty": 60, "price":  109.99},
    {"code": "P008", "name": "RAM DDR5 32GB",        "qty": 25, "price":  139.99},
]

ll  = LinkedList()
stk = Stack(max_size=10)
q   = Queue()
bst = BST()

for p in INITIAL_PRODUCTS:
    product = dict(p)
    ll.add(product)
    bst.insert(dict(p))
