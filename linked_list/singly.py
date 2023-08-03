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
        """
        Change value of element based on it's position
        """
        node = self.get(index)
        node.value = value
        return True

    def pop_left(self) -> bool:
        """
        Reveme element from the left side
        """
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
        """
        Remove element from the right side
        """
        if self.tail:
            node = self.get(self.length - 2)
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

    def reverse(self) -> None:
        """
        Reverse linked list
        """
        current_node = self.head
        previous_node = None
        for _ in range(self.length):
            if current_node:
                next_node = current_node.next
                current_node.next = previous_node
                previous_node = current_node
                current_node = next_node
        self.head, self.tail = self.tail, self.head

    def remove_duplicates(self):
        """
        Remove duplicated elements from the linked list
        """
        seen = set()
        current_node = self.head
        previous_node = None
        for _ in range(self.length):
            if current_node:
                next_node = current_node.next

                if current_node.value in seen and previous_node:
                    if current_node == self.tail:
                        previous_node.next = None
                        self.tail = previous_node
                    else:
                        previous_node.next = next_node

                    self.length -= 1

                seen.add(current_node.value)
                previous_node = current_node
                current_node = next_node


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.prepend(0)
    ll.append(5)
    ll.append(9)
    ll.insert(1, 10)
    print(f"Add many: {ll.traverse()}")
    print(f"Search 100: {ll.search(100)}")
    print(f"Search: {ll.traverse()}")
    ll.set(2, 100)
    print(f"Set: {ll.traverse()}")
    ll.pop_left()
    print(f"Pop left: {ll.traverse()}")
    ll.pop_right()
    print(f"Pop right: {ll.traverse()}")
    ll.delete(2)
    print(f"Delete: {ll.traverse()}")
    ll.append(21)
    print(f"Append: {ll.traverse()}")
    ll.insert(2, 15)
    print(f"Insert itens: {ll.traverse()}")
    ll.reverse()
    print(f"Reverse: {ll.traverse()}")
    ll.append(5)
    ll.append(21)
    print(f"Add itens: {ll.traverse()}")
    ll.remove_duplicates()
    print(f"Remove duplicates: {ll.traverse()}")
    ll.clear()
    print(f"Clear: {ll.traverse()}")
