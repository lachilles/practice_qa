from llist import dllist

class LRUCache():

    def __init__(self, maxSize):
        self._maxSize = maxSize
        self._curSize = 0
        self.table = {}
        self.list = dllist()

    def _remove(self, node):
        """remove the node from the cache; debit currentSize, remove from table and list"""
        self._curSize -= node.value['thing'].size()
        del self.table[node.value['key']]
        self.list.remove(node)

    def put(self, key, thing):
        if thing.size() > self._maxSize:
            raise Exception('ThatThangTooBig')
        # Remove current thing at this key
        if (key in self.table):
            _remove(self.table[key])

        # Make space for new thing, by removing LRU
        while self._curSize + thing.size() > self._maxSize:
            _remove(self.list.last)

        # Put thing at head of list, add the node to the table, and update curSize
        node = self.list.appendleft({'thing':thing, 'key':key})
        self.table[key] = node

        return thing

def get(self, key):
    if key not in self.table :
        raise Exception('AintNoSuchThang')

    node = self.table[key]
    self.list.appendleft(self.list.remove(node))
    return node.value['thing']
