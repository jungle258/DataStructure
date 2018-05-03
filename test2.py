# 单向链表


class SigleNode(object):
    """
    节点
    """

    def __init__(self, item):

        self.item = item

        self.next = None


class SingleLinkList(object):
    """单向链表"""

    def __init__(self):
        self.head = None

    def is_empty(self):
        """
        判断链表是否为空
        :return:
        """
        return self.head is None

    def length(self):
        """
        返回链表的长度
        :return:
        """
        count = 0
        cur = self.head

        while cur is not None:
            count += 1
            cur = cur.next

        return count

    def travel(self):
        """
        遍历链表
        :return:
        """
        cur = self.head

        while cur is not None:
            print(str(cur.item))
            cur = cur.next

    def add(self, item):
        """
        头部插入
        :return:
        """
        node = SigleNode(item)
        node.next = self.head
        self.head =node

    def append(self, item):
        """
        向尾添加
        :param item:
        :return:
        """
        node = SigleNode(item)

        temp = self.head

        if temp is None:
            self.head = node
        else:

            while temp.next is not None:
                temp = temp.next

            temp.next = node

    def insert(self, position, item):
        """
        指定位置插入
        :param position: 插入第几个
        :param item:
        :return:
        """
        item = SigleNode(item)

        if position <= 0:
            self.add(item)
            return
        if position > self.length()-1:
            self.append(item)
            return

        count = 0
        cur = self.head

        while count != position - 1:
            cur = cur.next
            count += 1

        temp = cur.next
        cur.next = item
        item.next = temp

    def remove(self, item):
        """
        移除某个节点
        :param item:
        :return: 成功返回True，失败返回False
        """

        cur = self.head
        pre = None

        while cur is not None:

            if cur.item == item:
                if pre is None:
                    self.head = cur.next
                    return True
                pre.next = cur.next
                return True
            else:
                pre = cur
                cur = cur.next

        return False

    def search(self, item):
        """
        查找节点是否存在，存在返回True,失败返回False
        :param item:
        :return:
        """
        cur = self.head

        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False


def main():

    link_list = SingleLinkList()
    for i in range(0, 11):
        link_list.add(i)
    link_list.travel()
    print('#'*20)
    link_list.length()
    print(link_list.is_empty())
    link_list.append(11)
    link_list.travel()
    print('#' * 20)
    link_list.insert(3, 12)
    link_list.travel()
    print('#' * 20)
    link_list.remove(8)
    link_list.travel()
    print('#' * 20)
    print(link_list.search(8))
    print(link_list.search(1))


if __name__ == '__main__':
    main()
