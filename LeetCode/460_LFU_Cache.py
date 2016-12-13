# https://leetcode.com/problems/lfu-cache/


class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._capa = capacity
        self._map = {} # key -> value
        self._key_to_freq = {} # key -> freq
        self._freq_to_key_list = {} # freq -> LRU key list


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
            self._key_to_freq[key] = new_freq # Increase the freq

            # Remove the key from the current freq to key list
            for each in self._freq_to_key_list[cur_freq]:
                if each == key:
                    self._freq_to_key_list[cur_freq].remove(each)
                    break

            if len(self._freq_to_key_list[cur_freq]) == 0:
                self._freq_to_key_list.pop(cur_freq)

            # Add the key to the new freq to key list
            if new_freq not in self._freq_to_key_list:
                self._freq_to_key_list[new_freq] = [key]
            else:
                self._freq_to_key_list[new_freq].insert(0, key)

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

        if len(self._key_to_freq) == self._capa:
            freqs = self._freq_to_key_list.keys()
            sorted(freqs)
            lfu_freq = freqs[0]
            lfu_key = self._freq_to_key_list[lfu_freq].pop() # pop away the last one
            if len(self._freq_to_key_list[lfu_freq]) == 0:
                self._freq_to_key_list.pop(lfu_freq)

            # Now remove this key-value pair
            self._key_to_freq.pop(lfu_key)
            self._map.pop(lfu_key)
        self._map[key] = value
        self._key_to_freq[key] = 0
        if 0 in self._freq_to_key_list:
            self._freq_to_key_list[0].insert(0, key)
        else:
            self._freq_to_key_list[0] = [key]



        # Your LFUCache object will be instantiated and called as such:
        # obj = LFUCache(capacity)
        # param_1 = obj.get(key)
        # obj.set(key,value)