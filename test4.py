# 双向链表


class Node(object):

    def __init__(self, item):

        self.item = item
        self.next = None
        self.pre = None


class LinkList(object):

    def __init__(self):
        self._head = None

    def is_empty(self):

        if self._head is None:
            return True
        return False

    def add(self, item):
        node = Node(item)

        if self.is_empty():
            self._head = node
            return True

        temp = self._head

        self._head = node
        temp.pre = self._head
        self._head.next = temp
        return True

    def travel(self):

        cur = self._head

        while cur is not None:
            print(cur.item)
            cur = cur.next

    def length(self):
        count = 0
        cur = self._head
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
            return
        cur = self._head

        while cur.next is not None:
                cur = cur.next
        cur.next = node
        node.pre = cur

    def insert(self, position, item):

        if position <= 1:
            self.add(item)
        elif position > self.length():
            self.append(item)
        else:
            count = 1
            cur = self._head
            while count != position:
                cur = cur.next
                count += 1
            node = Node(item)
            node.pre = cur.pre
            node.next = cur
            node.pre.next = node
            cur.pre = node

    def remove(self, item):

        if self.is_empty():
            return
        if self._head.item == item:
            self._head = self._head.next
            self._head.pre = Node
            return
        cur = self._head

        while cur is not None:
            if cur.item == item:
                cur.pre.next = cur.next
                if cur.next is not None:
                    cur.next.pre = cur.pre
                return
            cur = cur.next

    def search(self, item):
        cur = self._head
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next

        return False


def main():

    link_list = LinkList()
    for i in range(10):
        link_list.add(i)

    link_list.travel()
    print('#')
    print(link_list.length())
    print('#')
    link_list.append(100)
    link_list.travel()
    print('!')
    link_list.insert(1, 888)
    link_list.travel()
    print('!')
    link_list.remove(8888)
    link_list.travel()
    print('!')
    print(link_list.search(100))


if __name__ == '__main__':
    main()
