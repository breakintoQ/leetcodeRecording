# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity

#     def get(self, key: int) -> int:
        

#     def put(self, key: int, value: int) -> None:
        


# # Your LRUCache object will be instantiated and called as such:
# # obj = LRUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)




from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        # 初始化 LRU 缓存，使用 OrderedDict 来维护键值对的顺序
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        # 如果 key 存在于缓存中
        if key in self.cache:
            # 将该 key 移动到字典的末尾，表示最近使用
            self.cache.move_to_end(key)
            return self.cache[key]
        # 如果 key 不存在，返回 -1
        return -1

    def put(self, key: int, value: int) -> None:
        # 如果 key 已经存在，更新其值并移动到末尾
        if key in self.cache:
            self.cache.move_to_end(key)
        # 插入新的键值对
        self.cache[key] = value
        # 如果缓存超过容量，移除最久未使用的键值对
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # last=False 表示移除第一个插入的键值对


    #这个有点不会，直接copiot大人教

class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # 哈希表：key -> Node
        # 创建伪头部和伪尾部节点
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """从链表中删除节点"""
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _add_to_head(self, node: Node):
        """将节点添加到链表头部"""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _move_to_head(self, node: Node):
        """将节点移动到链表头部"""
        self._remove(node)
        self._add_to_head(node)

    def _pop_tail(self) -> Node:
        """移除链表尾部节点"""
        node = self.tail.prev
        self._remove(node)
        return node

    def get(self, key: int) -> int:
        if key in self.cache:
            # 如果 key 存在，移动对应节点到链表头部
            node = self.cache[key]
            self._move_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 如果 key 已经存在，更新节点值并移动到链表头部
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            # 如果 key 不存在，创建新节点
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
            # 如果缓存超过容量，移除最久未使用的节点
            if len(self.cache) > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]

            
#这个是使用双向链表的方法
