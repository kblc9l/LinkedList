class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value

    def __str__(self):
        return f'{self.value}'


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        """ Return str(self). """
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.value))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, value):
        """ Added object to the start of the list. """
        const = Node(value, self.head)

        self.head = const
        self.tail = self.tail if self.tail else const

        return self

    def add_end(self, value):
        """ Added object to the end of the list. """
        const = Node(value, None)

        if self.head is None:
            self.head = const
            self.tail = const

            return self

        self.tail.next = const
        self.tail = const

        return self

    def to_list(self):
        current_node: Node = self.head
        items = []
        while current_node:
            items.append(current_node.value)
            current_node = current_node.next

        return items

    def clear(self):
        """ Remove all items from list. """
        self.head = None
        self.tail = None

    def count(self, value):
        """ Return number of occurrences of value. """

        return self.to_list().count(value)

    def extend(self, llist: Node):
        """ Extend list by appending elements from the iterable. """
        if llist.head:
            self.tail.next = llist.head
            self.tail = llist.tail

    def insert(self, value, new_node: Node):
        """ Insert object before index. """
        if self.head is None:
            raise Exception('List is empty')

        for node in self:

            if node.value == value:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception(f"Node with data {value} not found")

    def pop_first(self):
        """Remove and return first item."""
        if self.head:
            poped = self.head
            self.head = self.head.next
            return poped

    def pop_end(self):
        """Remove and return end item."""
        current_note = self.head
        if self.head.next is None:
            poped = self.head

            self.clear()
            return poped

        while current_note.next != self.tail:
            current_note = current_note.next

        poped = self.tail
        current_note.next = None
        self.tail = current_note

        return poped

    def reverse(self):
        """ Reverse *IN PLACE*. """
        l1 = self.to_list()
        self.write_llist(l1)

    def sort(self, *args, **kwargs):
        """
        Sort the list in ascending order and return None.

        The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
        order of two equal elements is maintained).

        If a key function is given, apply it once to each list item and sort them,
        ascending or descending, according to their function values.

        The reverse flag can be set to sort in descending order.
        """
        l1 = self.to_list()
        l1.sort(*args, **kwargs)
        l1.reverse()

        self.write_llist(l1)

    def write_llist(self, l1):
        l_list = LinkedList()
        for i in range(len(l1)):
            l_list.add_first(l1[i])

        self.clear()
        current_node = l_list.head
        while current_node:
            self.add_end(current_node.value)
            current_node = current_node.next

    def __len__(self):
        """ Return len(self). """
        return len(self.to_list())
