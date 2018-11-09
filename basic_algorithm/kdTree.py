from typing import List
import math


class kdNode(object):
    """kdNode of k-d Tree"""

    def __init__(self, data: List[int], level: int):
        self.data = data
        self.level = level
        self.left = None
        self.right = None


def insert(nums: List[List], level: int=0):
    # nums = [[1,2,3,4,...],[1,2,3,4,...],...]
    level = (level + 1) % len(nums[0])
    nums.sort(key=lambda n: n[level])
    root = kdNode(int(len(nums) / 2), level)
    root.left = insert(nums[:int(len(nums) / 2)], level)
    root.right = insert(nums[int(len(nums) / 2 + 1):], level)
    return root


def search(root, item: List[int]) -> tuple:
    # return the closest node, and its distance
    minDist = minDistance(root.data, item)
    nodes = []
    curNode = root

    # dfs
    while curNode is not None:
        nodes.append(curNode)
        dist = minDistance(curNode.data, item)
        if dist < minDist:
            minDist = dist

        level = curNode.level
        curNode = curNode.left if item[
            level] <= curNode.data[level] else curNode.right

    # backtrack
    while nodes != []:
        node = nodes.pop()
        level = node.level
        tmpNode = node.right if abs(
            node.data[level] - item[level]) < minDist else node.left

        if tmpNode is not None:
            nodes.append(tmpNode)
            dist = minDistance(tmpNode.data, item)
            if dist < minDist:
                minDist = dist
                curNode = tmpNode

    return curNode, minDist


def minDistance(data, item)
    return math.sqrt(sum((data[i] - item[i])**2 for i in range(len(data))))
