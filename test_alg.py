
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class a():
    def f(self, head):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        f = head
        s = head.next
        while s is not None:
            printLink(head)
            t = s.next
            s.next = s
            s = t
            f = s
        print()
        printLink(head)
        return f

def printLink(head):
    print('------>')
    while head is not None:
        print(head.val)
        head = head.next
    print('<------')
    
if __name__ == '__main__':
    head = ListNode(1);node = head
    node.next=ListNode(2);node=node.next
    node.next=ListNode(3);node=node.next
    node.next=ListNode(4);node=node.next
    node.next=ListNode(5);node=node.next

    t = a()
    r = t.f(head)
    printLink(r)
