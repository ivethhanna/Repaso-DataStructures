class LLNode:
    def __init__(self, product):
        self.product = product
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, product):
        node = LLNode(product)
        if not self.head:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
        self.size += 1

    def remove(self, code):
        if not self.head:
            return False
        if self.head.product["code"] == code:
            self.head = self.head.next
            self.size -= 1
            return True
        cur = self.head
        while cur.next:
            if cur.next.product["code"] == code:
                cur.next = cur.next.next
                self.size -= 1
                return True
            cur = cur.next
        return False

    def find(self, code):
        cur = self.head
        while cur:
            if cur.product["code"] == code:
                return cur.product
            cur = cur.next
        return None

    def update(self, code, fields):
        cur = self.head
        while cur:
            if cur.product["code"] == code:
                cur.product.update(fields)
                return True
            cur = cur.next
        return False

    def to_list(self):
        result = []
        cur = self.head
        while cur:
            result.append(cur.product)
            cur = cur.next
        return result


class Stack:
    def __init__(self, max_size=10):
        self.items = []
        self.max_size = max_size

    def push(self, operation):
        if len(self.items) >= self.max_size:
            self.items.pop(0)
        self.items.append(operation)

    def pop(self):
        return self.items.pop() if self.items else None

    def peek(self):
        return self.items[-1] if self.items else None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def to_list(self):
        return list(reversed(self.items))


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0) if self.items else None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def to_list(self):
        return list(self.items)


class BSTNode:
    def __init__(self, product):
        self.product = product
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, product):
        self.root = self._insert(self.root, product)

    def _insert(self, node, product):
        if not node:
            return BSTNode(product)
        if product["code"] < node.product["code"]:
            node.left = self._insert(node.left, product)
        elif product["code"] > node.product["code"]:
            node.right = self._insert(node.right, product)
        else:
            node.product = product
        return node

    def search(self, code):
        return self._search(self.root, code)

    def _search(self, node, code):
        if not node:
            return None
        if code == node.product["code"]:
            return node.product
        if code < node.product["code"]:
            return self._search(node.left, code)
        return self._search(node.right, code)

    def remove(self, code):
        self.root = self._remove(self.root, code)

    def _remove(self, node, code):
        if not node:
            return None
        if code < node.product["code"]:
            node.left = self._remove(node.left, code)
        elif code > node.product["code"]:
            node.right = self._remove(node.right, code)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            min_node = node.right
            while min_node.left:
                min_node = min_node.left
            node.product = min_node.product
            node.right = self._remove(node.right, min_node.product["code"])
        return node

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.product)
            self._inorder(node.right, result)
