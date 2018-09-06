import copy
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class a():
    def f(self, nums):
        if sorted(nums, reverse=True) == nums:
            return
        idx = -1
        # from tail to head
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                idx = i-1
                break
            
        if len(nums[idx+1:]) > 1 and max(nums[idx+1:]) == nums[idx+1]:
            idd =  nums.index(min([i for i in nums[idx+1:] if i>nums[idx]]))
            nums[idx], nums[idd] = nums[idd], nums[idx]
            tem = sorted(nums[idx+1:])
            j = 0
            for i in range(idx+1,len(nums)):
                nums[i] = tem[j]
                j += 1
        else:
            nums[idx], nums[idx+1] = nums[idx+1], nums[idx]

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
    r = t.f([1,3,2])
    print(r)
