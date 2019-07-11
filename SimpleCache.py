"""Key/value cache class"""
import sys
class SimpleCache:
    """Key/value cache class

    Usage
    -----
    Cache = SimpleCache(maxkeys=1000, maxsize=1000000)
    Cache.set(key) = value
    key and value may have arbitrary type. maxsize is sum of
    sys.getsizeof(key) + sys.getsizeof(val) for all key/value pairs

    Example
    -------
    >>> Cache = SimpleCache(maxkeys=1000, maxsize=1000000)
    >>> Cache.set(1, 11)
    >>> Cache.get(1) # returns 11
    >>> Cache.get(0) # returns None

    """

    def __init__(self, maxkeys=1000, maxsize=100000, log=False):
        self.cache = {}
        self.keys = []
        self.size = 0
        self.log = log
        self.maxkeys = maxkeys
        self.maxsize = maxsize

    def cache(self):
        """Return cache (a dict)"""

        return self.cache

    def set(self, key, val):
        """Add key/value pair to cache"""

        self.cache[key] = val
        self.size = self.size + sys.getsizeof(key) + sys.getsizeof(val)

        if self.log:
            print("Set %s to %s" % (key, val))
            print("# elements in cache = %d" % len(self.cache))
            print("Size of cache = %d bytes" % self.size)

        if len(self.cache) > 1:
            if len(self.cache) > self.maxkeys:
                if self.log: print("# keys > maxkeys. Deleting key/value pair associated with key %s" % list(self.cache.keys())[0])
                del self.cache[list(self.cache.keys())[0]]

        key_list = list(self.cache.keys())
        i = 0
        while self.size > self.maxsize and len(self.cache) > 1:
            if self.log: print("size > maxsize. Deleting key/value pair associated with key %s" % self.cache[key_list[i]])
            self.size = self.size \
                        - sys.getsizeof(key_list[i]) \
                        - sys.getsizeof(self.cache[key_list[i]])
            del self.cache[key_list[i]]
            i = i + 1

    def get(self, key):
        """Get value from cache"""

        if key in self.cache:
            return self.cache[key]

        return None

    def test(self):
        """Run unit tests"""

        Cache = SimpleCache()
        Cache.set(1, 1)
        Cache.set(2, 2)
        Cache.set(3, {})
        Cache.set(4, {'a':'b'})

        assert Cache.get(1) == 1
        assert Cache.get(2) == 2
        assert Cache.get(3) == {}
        assert Cache.get(4) == {'a':'b'}

        Cache = SimpleCache(maxkeys=1)
        Cache.set(1, 1)
        Cache.set(2, 2)
        assert Cache.get(1) is None
        assert Cache.get(2) == 2

        a = {1:1}
        Cache = SimpleCache(maxsize=sys.getsizeof(1)+sys.getsizeof(1))
        Cache.set(1, 1) # Cache is now {1:1}
        assert Cache.cache == a
        Cache.set(2, 2) # 1:1 key/value pair is deleted after 2:2 is added to cache
        assert Cache.get(1) is None
        assert Cache.get(2) == 2

        return True
