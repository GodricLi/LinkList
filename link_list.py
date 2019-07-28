# _*_ coding=utf-8 _*_


class Node:
    """
    创建链表的属性
    """

    def __init__(self, item):
        self.item = item
        self.next = None


def create_head_linklist(arr):
    """
    头插法创建链表
    :param arr:
    :return:
    """
    head = Node(arr[0])  # 确定头部元素
    for element in arr[1:]:
        node = Node(element)
        node.next = head  # 从头部插入元素
        head = node  # 插入的元素成为头部元素

    return head


def create_tail_linklist(arr):
    """
    尾插法创建链表
    :param arr:
    :return:
    """
    head = Node(arr[0])
    tail = head  # 开始链表为空，头尾指向同一个位置
    for element in arr[1:]:
        node = Node(element)
        tail.next = node  # 从尾部插入元素
        tail = node  # 插入的元素成为尾部元素
    return head


def print_linklist(lk):
    while lk:
        print(lk.item, end=',')
        lk = lk.next


li = [1, 2, 3, 4, 5]
link_list1 = create_tail_linklist(li)
link_list2 = create_head_linklist(li)
print_linklist(link_list1)
print_linklist(link_list2)
