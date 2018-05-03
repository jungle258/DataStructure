# 单向循环链表


class SingleNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class SinCycLinkList(object):

    def __init__(self):
        self._head = None

    def is_empty(self):
        if self._head is None:
            return True
        else:
            return False

    def travel(self):

        if self.is_empty():
            return

        cur = self._head

        while cur.next != self._head:
            print(cur.item)
            cur = cur.next
        print(cur.item)

    def add(self, item):

        node = SingleNode(item)

        if self.is_empty():
            self._head = node
            node.next = self._head
            return

        cur = self._head

        while cur.next != self._head:
            cur = cur.next
        node.next = self._head
        self._head = node
        cur.next = self._head

    def append(self, item):

        node = SingleNode(item)
        if self.is_empty():
            self._head = node
            self._head.next = node

        cur = self._head

        while cur.next != self._head:
            cur = cur.next

        node.next = self._head
        cur.next = node

    def length(self):

        if self.is_empty():
            return 0

        if self._head == self._head.next:
            return 1
        count = 0
        cur = self._head
        while cur.next != self._head:
            count += 1
            cur = cur.next
        return count

    def insert(self, position, item):

        if position <= 0:
            self.add(item)
            return
        if position >= self.length()-1:
            self.append(item)
            return
        node = SingleNode(item)
        n = 0
        cur = self._head
        pre = None
        while n < position-1:
            pre = cur
            cur = cur.next
            n += 1
        pre.next = node
        node.next = cur

    def remove(self, item):
        if self.is_empty():
            return
        cur = self._head
        pre = None

        if cur.item == item:

            if cur.next != self._head:
                while cur.next != self._head:
                    cur = cur.next
                self._head = self._head.next
                cur.next = self._head
            else:
                self._head = None
            return True
        else:

            while cur.next != self._head:
                if cur.item == item:
                    pre.next = cur.next
                    return True
                pre = cur
                cur = cur.next

            if cur.item == item:
                pre.next = cur.next

                return True

            return False

    def search(self, item):
        if self.is_empty():
            return False
        cur = self._head
        if cur.item == item:
            return True
        while cur.next != self._head:
            if cur.item == item:
                return True
            cur = cur.next
        if cur.item == item:
            return True
        return False


def main():

    link_list = SinCycLinkList()
    print(link_list.is_empty())
    link_list.travel()
    for i in range(1, 11):
        link_list.add(i)
    link_list.travel()
    print(link_list.length())
    print(link_list.is_empty())
    print('@'*30)
    link_list.insert(3, 11)
    link_list.travel()
    print('+' * 30)
    print(link_list.remove(10))
    link_list.travel()
    print('-' * 30)
    print(link_list.search(-1))


if __name__ == '__main__':
    main()
