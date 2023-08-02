from typing import Any


class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next: Node | None = None

    def has_next(self) -> bool:
        return self.next is not None

    def __repr__(self) -> str:
        return str(self.__dict__)


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self.length = 0

    def traverse(self) -> list[tuple[int, Any]]:
        """
        Trave the linked list
        """
        current = self.head
        linked_list = list()

        for index in range(self.length):
            if current:
                linked_list.append((index, current.value))
                current = current.next

        return linked_list

    def search(self, value: Any) -> bool:
        """
        Check if a value is present in the linked list
        """
        current = self.head

        while current:
            if current and current.value == value:
                return True
            current = current.next

        return False

    def get(self, index: int) -> Node:
        """
        Get the node based in the index in the linked list
        """
        if not self.head:
            raise Exception("Linked List is empty!")

        current = self.head

        for _ in range(index):
            if current.next:
                current = current.next
            else:
                raise Exception("Could not find this index")

        return current

    def set(self, index: int, value: Any) -> bool:
        node = self.get(index)
        node.value = value
        return True

    def pop_left(self) -> bool:
        if self.head:
            removed = self.head

            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                removed.next = None

            self.length -= 1
            return True

        return False

    def pop_right(self) -> bool:
        if self.tail:
            node = self.get(self.length - 1)
            self.tail = node
            self.length -= 1
            return True
        return False

    def delete(self, index: int) -> bool:
        """
        Delete node at specified index
        """
        if self.length > 0:
            if index == 0 and self.head:
                self.pop_left()
            elif index == self.length - 1:
                self.pop_right()
            else:
                previous_node = self.get(index - 1)
                excluded = previous_node.next
                if excluded:
                    previous_node.next = excluded.next
                    excluded.next = None
                    self.length -= 1

            return True

        return False

    def clear(self):
        """
        Clean all nodes in linked list
        """
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value: Any) -> None:
        """
        Insert in the end of the linked list
        """
        new_node = Node(value)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def prepend(self, value: Any) -> None:
        """
        Insert in the beginning of the linked list
        """
        new_node = Node(value)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1

    def insert(self, index: int, value: Any) -> bool:
        """
        Insert in the middle of the linked list
        """
        new_node = Node(value)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            if index < 1 or index > self.length - 1:
                return False

            current_node = self.head

            for _ in range(index - 1):
                if current_node:
                    current_node = current_node.next

            if current_node:
                new_node.next = current_node.next
                current_node.next = new_node

            self.length += 1

        return True


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.prepend(0)
    ll.append(5)
    ll.append(9)
    ll.insert(1, 10)
    print(ll.traverse())
    print(ll.search(100))
    ll.set(2, 100)
    print(ll.traverse())
    ll.pop_left()
    print(ll.traverse())
    ll.pop_right()
    print(ll.traverse())
    ll.delete(2)
    print(ll.traverse())
    ll.clear()
    print(ll.traverse())