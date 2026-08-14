class Stack:

    class Node:
        def __init__(self, data, succ=None):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None
        self.Fiba = 1
        self.Fibb = 1
    def __iter__(self):
        current = self.first
        while current:
            yield current.data
            current = current.succ
    def __str__(self):
        return '(' + ', '.join([str(x) for x in self]) + ')'

    def Push(self, x):
        self.first = Stack.Node(x, self.first)

    def Pop(self): ##Exercise A3
        if self.first == None:
            return None
        self.first = self.first.succ
class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self):
        self.root = None

    def __iter__(self):
        if self.root:
            yield from self.root

    def __str__(self):
        return '<' + ', '.join([str(x) for x in self]) + '>'

    def insert(self, key):
        def _insert(r, key):
            if r is None:
                return self.Node(key)
            elif key < r.key:
                r.left = _insert(r.left, key)
            elif key > r.key:
                r.right = _insert(r.right, key)
            else:
                pass  # Already there
            return r

        self.root = _insert(self.root, key)

    def min(self): ##Exercise A3
        if self.root == None:
            return None
        else:
            r = self.root
            while r.left:
                r = r.left
            return r.key
class LinkedList:

    class Node:
        def __init__(self, data, succ=None):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __str__(self):
        return '(' + ', '.join([str(x) for x in self]) + ')'

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = LinkedList.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = LinkedList.Node(x, f.succ)

    def middle(self): ##Exercise B2
        if self.first == None:
            return None
        else:
            hoppare = mitt = self.first
            while hoppare and hoppare.succ:
                hoppare = hoppare.succ.succ
                mitt = mitt.succ
            return mitt.data

        pass
class Fib: #Exercise B3. Write Class Lucas below Class Fib.

    def __init__(self):
        self.a = 1
        self.b = 1
    def __next__(self):
        print(str(self.a), end=" ")
        self.a, self.b = self.b, self.b + self.a
class Lucas(Fib):
    def __init__(self):
        self.a = 2
        self.b = 1



    def __str__(self):
        return ("I represent an infinite sequence!")

def main():
    print("Test A3:")
    X = [[5, 8, 3, 7, 2, 6, 9], [4, 1, 3, 6, 7, 5, 8], []]
    for x in X:
        bst = BST()
        for i in x:
            bst.insert(i)
        m = bst.min()
        print(m)
    print("Test A4:")
    stack = Stack()
    for x in ["A", "B", "C", "D", "E"]:
        stack.Push(x)
    print(stack)
    for _ in range(6):
        stack.Pop()
        print(stack)
    print("Test B2:")
    X = [[0], [1,2],[1,2,3],[1,2,3,5],[1,2,3,5,8], list(range(100))] #
    for lst in X:
        ll = LinkedList()
        for x in lst:
            ll.insert(x)
        print(ll.middle(), lst[(len(lst))//2])
    print("Test B3:")
    F = Fib()
    for _ in range(15):
        next(F)
    print("")
    L = Lucas()
    for _ in range(15):
        next(L)
    print("")
    print(L)
if __name__ == '__main__':
    main()

