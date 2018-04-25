# https://leetcode.com/problems/encode-and-decode-tinyurl/description/
map_values = \
    [chr(i) for i in range(ord('a'), ord('z') + 1)] + \
    [chr(i) for i in range(ord('A'), ord('Z') + 1)] + \
    [chr(i) for i in range(ord('0'), ord('9') + 1)]

class Codec:
    def __init__(self):
        self.db = []

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        self.db.append(longUrl)
        return self.transformIDtoShortURL(len(self.db) - 1)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        id = 0
        for each_char in shortUrl[::-1]:
            id = id * len(map_values) + map_values.index(each_char)

        return self.db[id]

    def transformIDtoShortURL(self, id):
        shortURL = ""
        while id > 0:
            shortURL += map_values[id % len(map_values)]
            id /= len(map_values)
        shortURL += map_values[id]
        return shortURL


# Your Codec object will be instantiated and called as such:
codec = Codec()
for each in ["https://leetcode.com/problems/design-tinyurl"]:
    print(codec.decode(codec.encode(each)))