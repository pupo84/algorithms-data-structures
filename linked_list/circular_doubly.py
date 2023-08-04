class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: Node | None = None
        self.previous: Node | None = None

    def __repr__(self) -> str:
        return str(self.__dict__)


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def __reversed__(self):
        node = self.tail
        while node:
            yield node
            if node.previous == self.tail:
                break
            node = node.previous

    def insert(self, index: int, value: int) -> None:
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
            node.next = None
            node.previous = None
        else:
            current_node = self.head

            if index == 0:
                head = self.head
                head.previous = node
                node.next = head
                self.head = node
                self.tail.next = self.head
            elif current_node == self.tail:
                tail = self.tail
                tail.next = node
                node.previous = tail
                self.tail = node
                self.tail.next = self.head
            else:
                for _ in range(index - 1):
                    current_node = current_node.next

                if current_node.next == self.head:
                    current_node.next = node
                    node.previous = current_node
                    self.tail = node
                    self.tail.next = self.head
                else:
                    next_node = current_node.next  # 2
                    current_node.next = node
                    node.next = next_node
                    node.previous = current_node
                    next_node.previous = node

    def search(self, value):
        for index, node in enumerate(self):
            if node.value == value:
                return index
        raise LookupError(f"Could not find value {value}")

    def delete(self, value):
        if self.head.value == value:
            head_node = self.head
            next_node = head_node.next
            self.head = next_node
            self.tail.next = self.head
            next_node.previous = None
        else:
            previous_node = None
            for node in self:
                if node.value == value:
                    next_node = node.next
                    previous_node.next = next_node
                    next_node.previous = previous_node

                    if self.tail.value == value:
                        self.tail = node.next
                    return
                previous_node = node
            raise LookupError(f"Could not find value {value}")

    def clear(self):
        self.head = None
        self.tail.next = None
        self.tail = None


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert(0, 0)
    dll.insert(1, 1)
    dll.insert(2, 2)
    dll.insert(2, -1)
    dll.insert(0, -2)
    print([n.value for n in dll])
    print([n.value for n in reversed(dll)])
    print(dll.search(1))
    dll.delete(-2)
    print([n.value for n in dll])
    print([n.value for n in reversed(dll)])
    dll.clear()
    print([n.value for n in dll])
