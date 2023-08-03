from typing import Optional


class Node:
    def __init__(self, value: int | None = None):
        self.value: Optional[int] = value
        self.next: Optional[Node] = None

    def __repr__(self) -> str:
        return str(self.__dict__)


class CircularSinglyLinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def insert(self, index, value):
        node: Node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            current_node = self.head

            if index == 0:
                previous_head = self.head
                node.next = previous_head
                self.head = node
                self.tail.next = node
            elif current_node == self.tail:
                last_node = self.tail
                self.tail = node
                last_node.next = node
                node.next = self.head
            else:
                for _ in range(index - 1):
                    current_node = current_node.next

                next_node = current_node.next
                current_node.next = node
                node.next = next_node

                if current_node == self.tail:
                    self.tail = node


if __name__ == "__main__":
    cll = CircularSinglyLinkedList()
    cll.insert(0, 0)
    cll.insert(1, 1)
    cll.insert(2, 2)
    cll.insert(3, 3)
    cll.insert(2, 5)
    cll.insert(0, -1)
    cll.insert(5, 19)
    cll.insert(10, 19)
    print([node.value for node in cll])
