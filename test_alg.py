import copy
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class a():
    def f(self, time):
        if time == "23:59":
            return "22:22"
        nums = [int(t) for t in time if t != ':']
        result = nums[:2] + [':'] + nums[2:]
        MM = nums[2:]
        # generate possible MM
        if MM[1] != max(nums):
            # if there exist larger num than MM-1
            can = [i for i in nums if i>MM[1]]
            if can != []:
                result[4] = min(can)
                return ''.join(str(e) for e in result)
        if MM[0] != 5:
            # if there are larger num than MM-0 and <=5
            can = [i for i in nums if i > MM[0] and i <=5]
            if can != []:
                result[3] = min(can)
                return ''.join(str(e) for e in result)
        
        HH = int(''.join(str(e) for e in nums[:2]))
        # generate possible HH 
        def gen(nums, n, k, HH):
            result = []
            tem = [0] * k
            def next_num(a, ni):
                if ni == k:
                    result.append(copy.copy(tem))
                    return
                for i in range(len(a)):
                    tem[ni] = a[i]
                    b = a[:]
                    #b.pop(i)
                    next_num(b, ni+1)
            c = nums[:]
            next_num(c,0)
            digs = [int(''.join(str(d) for d in r)) for r in result]
            print(digs)
            return min([i for i in digs if i < 24 and i>HH])

        newHH = gen(nums, 4, 2, HH)
        newMM = ''.join([str(min(nums))]*2)

        return str(newHH) + ':' + str(newMM)

def printLink(head):
    print('------>')
    while head is not None:
        print(head.val)
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
    t = a()
    r = t.f('20:48')
    print(r)
