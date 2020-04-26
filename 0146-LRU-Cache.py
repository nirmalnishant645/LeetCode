'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''
class Node:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self
        self.next = self

class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(1,1)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key in self.d:
            cur_node = self.d[key]
            self.remove_from_list(cur_node)
            self.insert_at_head(cur_node)
            return cur_node.value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            cur_node = self.d[key]
            self.remove_from_list(cur_node)
            self.insert_at_head(cur_node)
            cur_node.value = value
        else:
            if len(self.d) >= self.capacity:
                self.remove_from_tail()
            cur_node = Node(key, value)
            self.d[key] = cur_node
            self.insert_at_head(cur_node)
            
    def remove_from_list(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def insert_at_head(self, node):
        head_next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = head_next
        head_next.prev = node
        
    def remove_from_tail(self):
        if len(self.d) == 0:
            return
        tail_node = self.tail.prev
        del self.d[tail_node.key]
        self.remove_from_list(tail_node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
