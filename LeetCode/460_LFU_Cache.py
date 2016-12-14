# https://leetcode.com/problems/lfu-cache/
DEBUG = False

class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._capa = capacity
        self._map = {}  # key -> value
        self._key_to_freq = {}  # key -> freq
        self._freq_to_key_list = {}  # freq -> LRU key list

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # Corner case:
        if self._capa == 0:
            return -1

        if key in self._map:
            cur_freq = self._key_to_freq[key]
            new_freq = cur_freq + 1
            self._key_to_freq[key] = new_freq  # Increase the freq

            # Remove the key from the current freq to key list
            self._freq_to_key_list[cur_freq].remove(key)
            if len(self._freq_to_key_list[cur_freq]) == 0:
                if DEBUG:
                    print("Delete _freq_to_key_list[%d]" % cur_freq)
                self._freq_to_key_list.pop(cur_freq)

            # Add the key to the new freq to key list
            if new_freq not in self._freq_to_key_list:
                self._freq_to_key_list[new_freq] = [key]
            else:
                self._freq_to_key_list[new_freq].insert(0, key)

            if DEBUG:
                print("Increase freq of %d from %d to %d" % (key, cur_freq, new_freq))

            return self._map[key]
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # Corner case:
        if self._capa == 0:
            return

        if len(self._map) == self._capa and key not in self._map:
            freqs = self._freq_to_key_list.keys()
            sorted(freqs)
            lfu_freq = freqs[0]
            lfu_key = self._freq_to_key_list[lfu_freq].pop()  # pop away the last one
            if len(self._freq_to_key_list[lfu_freq]) == 0:
                self._freq_to_key_list.pop(lfu_freq)

            # Now remove this key-value pair
            try:
                self._key_to_freq.pop(lfu_key)
            except KeyError:
                if DEBUG:
                    print("Encounter KeyError: key = %d value = %d" % (key, value))
            self._map.pop(lfu_key)
            if DEBUG:
                print("Remove key %d" % lfu_key)

        # Now we add new key
        if key not in self._key_to_freq:
            self._key_to_freq[key] = 0
            if 0 in self._freq_to_key_list:
                self._freq_to_key_list[0].insert(0, key)
            else:
                self._freq_to_key_list[0] = [key]
        else:
            self._freq_to_key_list[self._key_to_freq[key]].remove(key)
            self._freq_to_key_list[self._key_to_freq[key]].insert(0, key)
        self._map[key] = value

        if DEBUG:
            print("Cache size = %d" % len(self._map))




            # Your LFUCache object will be instantiated and called as such:
            # obj = LFUCache(capacity)
            # param_1 = obj.get(key)
            # obj.set(key,value)


test_cmd = ["LFUCache", "set", "set", "set", "set", "set", "get", "set", "get", "get", "set", "get", "set", "set",
            "set", "get", "set", "get", "get", "get", "get", "set", "set", "get", "get", "get", "set", "set", "get",
            "set", "get", "set", "get", "get", "get", "set", "set", "set", "get", "set", "get", "get", "set", "set",
            "get", "set", "set", "set", "set", "get", "set", "set", "get", "set", "set", "get", "set", "set", "set",
            "set", "set", "get", "set", "set", "get", "set", "get", "get", "get", "set", "get", "get", "set", "set",
            "set", "set", "get", "set", "set", "set", "set", "get", "get", "get", "set", "set", "set", "get", "set",
            "set", "set", "get", "set", "set", "set", "get", "get", "get", "set", "set", "set", "set", "get", "set",
            "set", "set", "set", "set", "set", "set"]
test_value = [[10], [10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22],
              [5, 5], [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1],
              [3], [10, 11], [8], [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27],
              [2, 12], [5], [2, 9], [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10],
              [4, 15], [7, 22], [11, 26], [8, 17], [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6], [3, 4],
              [1], [10], [3, 29], [10, 28], [1, 20], [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26], [8], [7], [5],
              [13, 17], [2, 27], [11, 15], [12], [9, 19], [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19], [4], [5],
              [5], [8, 1], [11, 7], [5, 2], [9, 28], [1], [2, 2], [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]

for i in range(len(test_cmd)):
    if i == 0:
        lfuCache = LFUCache(test_value[i][0])
        print("LFUCache(%d)" % test_value[i][0])
    else:
        if test_cmd[i] == "set":
            lfuCache.set(test_value[i][0], test_value[i][1])
            print("set(%d, %d)" % (test_value[i][0], test_value[i][1]))
        else:
            print("get(%d) = %d\n" % (test_value[i][0], lfuCache.get(test_value[i][0])))
        print("map: " + str(lfuCache._map) + "\n")
