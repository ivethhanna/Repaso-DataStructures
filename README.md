# Sistema de Administración de Inventario

Aplicación de terminal desarrollada en Python que implementa cinco estructuras de datos fundamentales: arreglos, listas enlazadas, pilas, colas y árboles binarios de búsqueda.

---

## Estructura del proyecto

| Archivo | Responsabilidad |
|---|---|
| `main.py` | Punto de entrada y menú principal |
| `structures.py` | Implementación de las 5 estructuras de datos |
| `state.py` | Estado global: instancias y datos iniciales |
| `ui.py` | Colores ANSI, tablas y entradas de usuario |
| `menu_inventario.py` | Agregar, eliminar, editar, ordenar y buscar productos |
| `menu_pila.py` | Historial de operaciones y función deshacer |
| `menu_cola.py` | Gestión de pedidos de clientes |
| `menu_bst.py` | Búsqueda, recorrido inorden y visualización del árbol |

---

## Estructuras de datos

### 1. Arreglos

Se usa una lista de diccionarios en Python para almacenar los productos iniciales del inventario.

```python
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
```

El ordenamiento se implementa con `sorted()` y un comparador `lambda`. El usuario puede ordenar por nombre, precio o cantidad en dirección ascendente o descendente.

```python
products.sort(key=lambda p: p["name"])
products.sort(key=lambda p: p["price"], reverse=True)
```

---

### 2. Lista Enlazada

Es la estructura principal del inventario. Cada producto se almacena en un nodo con un puntero al siguiente. Permite agregar y eliminar productos de forma dinámica.

```
[P001] -> [P002] -> [P003] -> ... -> [P008] -> None
```

**Métodos implementados:**

| Método | Descripción | Complejidad |
|---|---|---|
| `add(product)` | Inserta un nodo al final | O(n) |
| `remove(code)` | Elimina el nodo con ese código | O(n) |
| `find(code)` | Busca un producto por código | O(n) |
| `update(code, fields)` | Actualiza campos de un nodo | O(n) |
| `to_list()` | Convierte la lista a un array de Python | O(n) |

La búsqueda es secuencial: recorre los nodos desde el inicio hasta encontrar el código buscado.

---

### 3. Pila (Stack)

Lleva el historial de las últimas 10 operaciones. Sigue el principio **LIFO**: la última operación registrada es la primera en deshacerse.

```
TOPE --> [ EDITAR  | P003 | 10:45 ]
         [ AGREGAR | P009 | 10:32 ]
         [ ELIMINAR| P005 | 10:21 ]
         [ AGREGAR | P008 | 10:10 ]
BASE --> [ ...                    ]
```

Cada entrada guarda el tipo de operación, los datos afectados y la hora. Si la pila supera 10 entradas, se descarta la más antigua.

**Función deshacer (`pop()`):**

| Operación | Acción al deshacer |
|---|---|
| `AGREGAR` | Elimina el producto de la lista enlazada y del BST |
| `ELIMINAR` | Vuelve a insertar el producto en ambas estructuras |
| `EDITAR` | Restaura los valores anteriores del producto |

---

### 4. Cola (Queue)

Simula una fila de pedidos de clientes. Sigue el principio **FIFO**: el primer cliente en llegar es el primero en ser atendido.

```
FRENTE --> [ Cliente A | P001 x2 | 09:00 ]
           [ Cliente B | P003 x1 | 09:15 ]
FINAL  --> [ Cliente C | P007 x3 | 09:30 ]
```

**Métodos implementados:**

| Método | Descripción |
|---|---|
| `enqueue(item)` | Agrega un pedido al final de la cola |
| `dequeue()` | Extrae y retorna el pedido del frente |

Al atender un pedido, el sistema muestra los datos del cliente, la hora de ingreso y la hora de atención, e indica quién es el siguiente en la fila.

---

### 5. Árbol Binario de Búsqueda (BST)

Permite encontrar productos de forma eficiente. Los nodos se insertan ordenados por código: los menores van al subárbol izquierdo y los mayores al derecho.


**Operaciones disponibles:**

| Operación | Descripción | Complejidad |
|---|---|---|
| `insert(product)` | Inserta un nodo respetando el orden | O(log n) promedio |
| `search(code)` | Busca un producto comparando en cada nivel | O(log n) promedio |
| `inorder()` | Recorrido izquierda → raíz → derecha | O(n) |
| `remove(code)` | Elimina un nodo manteniendo la propiedad del BST | O(log n) promedio |

El recorrido inorden produce automáticamente los productos ordenados por código de forma ascendente, sin necesidad de un algoritmo de ordenamiento adicional.

El BST se mantiene sincronizado con la lista enlazada: toda operación de agregar, editar o eliminar actualiza ambas estructuras.

---

## Conclusiones

- Los **arreglos** son útiles para datos iniciales y ordenamiento visual, pero no permiten inserciones y eliminaciones dinámicas eficientes.
- La **lista enlazada** gestiona el inventario de forma dinámica a costo de búsqueda secuencial O(n).
- La **pila** implementa de forma natural la funcionalidad de deshacer, ya que el último cambio siempre es el primero en revertirse.
- La **cola** garantiza equidad en la atención de pedidos respetando el orden de llegada.
- El **BST** ofrece búsqueda eficiente O(log n) y produce los productos ordenados a través del recorrido inorden sin costo adicional.
