# ✏️ Description
# ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
# Q. Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class.

# If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

# Examples:
# See test cases.
# ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
# 🟦 Python
# ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
class LRUCache:
  def __init__(self):
    self.capacity = 3

  def get(self, key: int) -> int:
    pass

  def put(self, key: int, val: int) -> int:
    pass

# Test Cases
cache = LRUCache()
print(cache.get(0)) // None
cache.put(1, 10)
cache.put(2, 20)
cache.put(3, 30)
print(cache.get(1)) // 10
print(cache.get(2)) // 20
cache.put(key: 4, val: 40)
print(cache.get(3)) // None because purged when 4 was put in.
