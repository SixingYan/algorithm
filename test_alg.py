import copy


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def preInput(lists):
    # 每次修改这里，构造题目的input
    return [listToLink(l) for l in lists]


class a():

    def f(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lists = [l for l in lists if l is not None]
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 0:
            return None
        vd = {}
        for i in range(len(lists)): 
            lst = lists[i]
            print('now is '+str(i))
            while lst is not None:
                ky = lst.val
                print ('val is '+str(ky))
                if not ky in vd.keys(): 
                    print('create')
                    vd[ky] = [lst, lst]
                else:
                    print('input')
                    vd[ky][1].next = lst
                    vd[ky][1] = vd[ky][1].next
                lst = lst.next
                vd[ky][1].next = None
                printLink(vd[ky][0])
            print()
        vl = sorted(list(vd.items()),key=lambda v: v[0])
        head = vl[0][1][0]
        for i in range(1, len(vl)):
            t = vl[i-1][1][1]
            t.next = vl[i][1][0]
            t = t.next
        return head


        """

        lists = [l for l in lists if l is not None]
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 0:
            return None
        
        # set head
        lists.sort(key=lambda v: v.val)
        head = lists[0]
        lists[0] = lists[0].next
        if lists[0] is None:
            del lists[0]
        t = head
        #t = t.next
        
        print(1)
        printLink(head)
        print()
        lists.sort(key=lambda v: v.val)
        for l in lists:
            printLink(l)
        print()
        
        # visit
        while len(lists) > 0:
            for i in range(len(lists)):
                t.next = lists[i]
                lists[i] = lists[i].next
                t = t.next
                if i + 1 != len(lists):
                    while lists[i] is not None and lists[i].val <= lists[i+1].val:
                        t.next = lists[i]
                        lists[i] = lists[i].next
                        t = t.next
            lists = [l for l in lists if l is not None]
            lists.sort(key=lambda v: v.val)
            print("now is ")
            for l in lists:
                printLink(l)
        return head
        """


def listToLink(lst):
    head = ListNode(lst[0])
    t = head
    for i in range(1, len(lst)):
        t.next = ListNode(lst[i])
        t = t.next
    return head

def printLink(head):
    print('------>', end=' ')
    while head is not None:
        print(head.val, end=' ')
        head = head.next
    print('<------')

if __name__ == '__main__':
    """
    head = ListNode(1);node = head
    node.next=ListNode(2);node=node.next
    node.next=ListNode(3);node=node.next
    node.next=ListNode(4);node=node.next
    node.next=ListNode(5);node=node.next
    """
    data = [[1,4,5],[1,3,4],[2,6]]
    t = a()
    r = t.f(preInput(data))
    print('result is ')
    printLink(r)
