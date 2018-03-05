# https://leetcode.com/problems/string-compression/description/
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) <= 1:
            return len(chars)

        compressed_count = 0
        last_char, last_char_i = chars[0], 0
        i = 1
        while i < len(chars):
            cur_char = chars[i]
            if last_char == cur_char:
                if compressed_count > 0:
                    compressed_count += 1
                else:
                    compressed_count = 2
            else:
                # if cur_char is a new char
                last_char = cur_char
                if compressed_count > 0:
                    # move last_char_i forward by the length of count string
                    chars[last_char_i + 1:last_char_i + 1 + len(str(compressed_count))] = str(compressed_count)
                    last_char_i += len(str(compressed_count)) + 1
                    chars[last_char_i] = last_char
                    compressed_count = 0
                else:
                    last_char_i += 1
                    # We may need to move the char to the right place
                    if last_char_i != i:
                        chars[last_char_i] = last_char

            i += 1

        # Handle the rest count
        if compressed_count > 0:
            chars[last_char_i + 1:last_char_i + 1 + len(str(compressed_count))] = str(compressed_count)
            last_char_i += len(str(compressed_count)) + 1
        else:
            last_char_i += 1

        return last_char_i


s = Solution()
chars = ["a","b","c","d","e","f",\
         "g","g","g","g","g","g","g","g","g","g","g","g",\
         "a","b","c"]
# chars = ['a', 'b', 'c']
print(s.compress(chars))
print(chars)