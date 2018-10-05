# https://leetcode.com/problems/lru-cache/
class DoubleLinkedListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev, self.next = None, None

class LRUCache(object):

    # Double Linked List + Hash Map

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.count = 0
        self.cache = {}
        self.head = DoubleLinkedListNode()
        self.tail = DoubleLinkedListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def removeNode(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def addToHead(self, node):
        cur_first_node = self.head.next
        self.head.next = node
        cur_first_node.prev = node
        node.prev, node.next = self.head, cur_first_node

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def popTail(self):
        node = self.tail.prev
        node.prev.next = self.tail
        self.tail.prev = node.prev
        return node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node = self.cache[key]
            self.moveToHead(node)
            return node.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.moveToHead(node)
        else:
            if self.count == self.capacity:
                node = self.popTail()
                # print("poptail: ", node.key)
                del self.cache[node.key]
                del node
                self.count -= 1
            new_node = DoubleLinkedListNode(key, value)
            self.cache[key] = new_node
            self.addToHead(new_node)
            self.count += 1


# Your LRUCache object will be instantiated and called as such:
capacity = 2
obj = LRUCache(capacity)
obj.put(1,1)
obj.put(2,2)
print(obj.get(1))
obj.put(3,3)
print(obj.get(2))
obj.put(4,4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))

