class a():
    def function():

        if x < 0:
            return False
        if -1< x < 10:
            return True

        # cal digs
        ten = 10
        while x/ten >= 1:
            ten *= 10
        ten /= 10
        
        # get dig list
        dig_list = []

        while ten >= 1:
            dig = int(x/ten)
            dig_list.append(dig)

            x -= dig * ten
            ten /= 10
        
        # check list
        for i in range(int(len(dig_list)/2)+1):
            if dig_list[i] != dig_list[len(dig_list)-i-1]:
                return False
        return True


    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <=0:
            return False
        
        if n!=1 and n%2 !=0:
            return False
        if n == 1 or n==2:
            return True
        
        x = n
        while x!= 1:
            if (x/2) %2 != 0:
                return False
            x /= 2
            x = int(x)
            if x == 2:
                break
                
        return True        
    
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num = n
        while (num > 1):
            if num % 2 == 1:
                return False
            num /= 2
        if num == 1:
            return True
        return False

        
Input:
536870912
Output:
false
Expected:
true
        

Input:
536870913
Output:
true
Expected:
false
    
            
    
        

    def insertionSortList147(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        Input: 4->2->1->3
        Output: 1->2->3->4
        """
        if head is None:
            return head
        node = head

        # 比当前最小更小，说明要往前移动
        cur_min = node.val

        last_node = node
        node = node.next

        while node is not None:
            if node.val < cur_min:

                self.insert(head, node)
                # update min
                cur_min
            else:
                pass
    def insert(self, head, min_node):
        # smaller than head, replace head
        if min_node.val < head.val:
            min_node
        # other

    def link2list(self, l1, l2):
        list1 = []
        list2 = []

        while l1 is not None:
            list1.append(l1.val)
            l1.next = l1

        while l2 is not None:
            list2.append(l2.val)
            l2.next = l2

        if len(l1) < len(l2):
            return list1, list2
        else:
            return list2, list1

    def myPow50(self, x: float, n: int):
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == -1:
            return round(1 / x, 5)
        if n < 0:
            return 1 / self.pow(x, n)
        else:
            return self.pow(x, n)

    def pow(self, x, n):
        v = round(float(x), 5) * 100000
        val = list(str(v))
        sm = val[-5:]
        lg = val[:-5]
        print(sm)
        print(lg)
        i = 0
        """
        while i < n:
            lg = self.multiply(lg, lg)
            sm = self.multiply(sm, sm)
            sm = sm[:5]

            i += 1
        lg = ''.join(str(i) for i in lg)
        sm = ''.join(str(i) for i in sm)
        sm = float(int(sm)/100000)
        return int(lg) + round(sm,5)
        """

    def multiply(self, num1, num2):
        """
        :type num1: List[str]
        :type num2: List[str]
        :rtype: str
        """
        int1 = 0
        int2 = 0
        if num1 == ["0"] or num2 == ["0"]:
            return "0"
        total = ""
        for char in num1:
            int1 *= 10
            int1 += self.getInt(char)
        for char in num2:
            int2 *= 10
            int2 += self.getInt(char)

        numTotal = int1 * int2
        print(numTotal)
        while numTotal != 0:
            digit = numTotal % 10
            numTotal = numTotal / 10
            total = self.getStr(digit) + total

        return total

    def getInt(self, digit):
        mapp = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return mapp.get(digit, 0)

    def getStr(self, digit):
        mapp = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
        return mapp.get(digit, '0')


if __name__ == '__main__':
    t = a()
    # r = t.func('401716832807512840963',
    #           '167141802233061013023557397451289113296441069')
    r = t.myAtoi("3.14159")
    print(r)
