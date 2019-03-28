class LLNode:
    def __init__(self):
        self.next = None
        self.prev = None
        self.item = None

class LList:
    def __init__(self):
        self.head = LLNode()
        self.tail = LLNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def __str__(self):
        out = ""
        point = self.head.next
        while point != self.tail:
            out += "->%s" % point.item
            point = point.next
        return out

    def __repr__(self):
        return str(self)

    def append(self, item):
        node = LLNode()
        node.item = item
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail

    def add(self, item, location):
        pointer = self.head.next
        for i in range(location):
            pointer = pointer.next
        node = LLNode()
        node.item = item
        pointer.prev.next = node
        node.prev = pointer.prev
        pointer.prev = node
        node.next = pointer
        return node

cards = LList()
operations= []

with open("input.txt") as inFile:
    line = inFile.readline()
    for char in line:
        cards.append(int(char))

def tryRemove(list, operations):
    pointer = list.head.next
    location = 0
    while pointer != list.tail:
        if pointer.item == 1:
            remove(pointer)
            operations.append(location)
            if list.head.next == list.tail:
                return True
            if not (tryRemove(list, operations)):
                location = operations.pop()
                pointer = list.add(1, location)
                prev = pointer.prev
                next = pointer.next
                if prev.item is not None:
                    if prev.item == 1:
                        prev.item = 0
                    else:
                        prev.item = 1
                if next.item is not None:
                    if next.item == 1:
                        next.item = 0
                    else:
                        next.item = 1
            else:
                return True

        pointer = pointer.next
        location += 1
    return False

def remove(pointer):
    prev = pointer.prev
    next = pointer.next
    if prev.item == 1:
        prev.item = 0
    elif prev.item == 0:
        prev.item = 1
    if next.item == 1:
        next.item = 0
    elif next.item == 0:
        next.item = 1
    prev.next = next
    next.prev = prev
    pointer.next = None
    pointer.prev = None
    pointer.item = None

if __name__ == "__main__":
    if tryRemove(cards, operations):
        operations = [str(x) for x in operations]
        print(" ".join(operations))
    else:
        print("No solution")
