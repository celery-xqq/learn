# 146. LRU 缓存
# 请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
# 实现 LRUCache 类：
# LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；
# 如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

# 示例：
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4

# 以下是用 Python 实现 LRU 缓存的代码，结合哈希表和双向链表的思路，但利用 Python 的 OrderedDict 简化实现。
# OrderedDict 内部维护了一个按插入顺序排序的双向链表，可以高效地移动节点到末尾或弹出头部节点。

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 将访问的键移动到字典末尾（表示最近使用）
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 如果键已存在，更新值并移动到末尾
            self.cache.move_to_end(key)
            self.cache[key] = value
        else:
            # 插入新键值对到末尾
            self.cache[key] = value
            # 检查容量是否超限
            if len(self.cache) > self.capacity:
                # 弹出最久未使用的键（字典头部）
                self.cache.popitem(last=False)


# 代码解释
# 1. 数据结构
# OrderedDict：
# 内部维护了一个双向链表，按插入顺序排序。
# 尾部是最近操作（插入或访问）的键，头部是最久未操作的键。
# 支持 move_to_end(key)（将键移动到尾部）和 popitem(last=False)（弹出头部键）。

# 2. 核心操作
# get 方法：
# 如果键不存在，返回 -1。
# 如果键存在，调用 move_to_end(key) 将其标记为最近使用，并返回值。
# put 方法：
# 如果键已存在，更新值并调用 move_to_end(key)。
# 如果键不存在，插入新键值对到末尾。
# 如果容量超限，调用 popitem(last=False) 删除最久未使用的键（即头部键）。

# 为什么用 OrderedDict？
# 高效操作：
# move_to_end 和 popitem 的时间复杂度均为 O(1)。
# 简化实现：
# 无需手动维护双向链表和哈希表，代码更简洁。
# 符合 LRU 逻辑：
# 尾部表示最近使用，头部表示最久未使用，直接通过 popitem(last=False) 淘汰数据。
