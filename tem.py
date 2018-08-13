148

    def function():
        if head is None:
            return head

        nums = []
        node = head
        while node is not None:
            nums.append(node.val)
            node = node.next

        nums.sort()
        node = head
        i = 0
        while node is not None:
            node.val = nums[i]
            node = node.next
            i += 1

        return head

    39

    def function(c, t):

        # delete the value which is larger than target
        avaliable = [v for v in c if c <= t]
        result = []
        values = []
        while avaliable is not None:
            if len(result) == 0:
                for c in avaliable:
                    if c <= t:
                        result.append([c])
                        values.append(c)
            else:
                newAvaliable = []
                newResult = []
                newValues = []
                for i in range(len(avaliable)):
                    c = avaliable[i]
                    for r in result:
                        if sum(r) + c < t:
                            r.append(c)
                            newResult.append(r[:])
                            values.append(sum(r))
                            newAvaliable.append(c)

                avaliable = newAvaliable[:]
                result = newResult[:]
                values = newValues[:]

        return [r for r in result if sum(r) == t]

        82

        def function():
            nums = []
            node = head
            while node is not None:
                nums.append(node.val)
                node = node.next

            newNums = []
            for i in range(len(nums)):
                if nums.count(nums[i]) == 1:
                    newNums.append(nums[i])

            ndoe = head
            if len(newNums) > 0:
                for i in range(len(newNums)):
                    node.val = newNums[i]
                    if i == len(newNums) - 1:
                        node.next = None
                    else:
                        node = node.next
            else:
                return None

            return head


        100
        def function():
            return self.verifyTwo()

        def verifyTwo(self, tr1, tr2):
            if tr1.val == tr2.val:
                if (self.theSame(tr1.right, tr2.right) and self.theSame(tr1.left, tr2.left)) is False:
                    return False

                if tr1.right is not None:
                    r = self.verifyTwo(tr1.right, tr2.right)
                    if r is False:
                        return False

                if tr1.left is not None:
                    r = self.verifyTwo(tr1.left, tr2.left)
                    if r is False:
                        return False

                return True

            else:
                return False

        def theSame(self, n1, n2):
            if n1 is not None and n2 is not None:
                return True

            if n1 is None and n2 is None:
                return True

            return False