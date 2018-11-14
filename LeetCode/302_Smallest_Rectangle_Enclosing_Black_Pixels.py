# http://buttercola.blogspot.com/2016/01/leetcode-smallest-rectangle-enclosing.html
# An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel
# . The black pixels are connected, i.e., there is only one black region.
# Pixels are connected horizontally and vertically.
# Given the location (x, y) of one of the black pixels,
# return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.
# For example, given the following image:
# [
#   "0010",
#   "0110",
#   "0100"
# ]
# and x = 0, y = 2,
# Return 6.

class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        # Given (x, y), binary search the top, bottom, left, right boundary
        if not image:
            return 0

        def binary_search(start, end, is_vertical, has_one):
            # end inclusive
            while start <= end:
                mid = (start + end) // 2
                if is_vertical:
                    search_array = [int(image[k][mid]) for k in range(len(image))]
                else:
                    search_array = [int(c) for c in image[mid]]

                if any(search_array) == has_one:
                    # If has_one is True, it means we find 1
                    # then we want to find the first 1
                    # If has_one is False, it means we find 0
                    # then we want to find the first 0
                    end = mid - 1
                else:
                    start = mid + 1

            return start

        # if row[mid] has 1 then we further search above, else we search latter half
        top = binary_search(0, x-1, False, True)
        bottom = binary_search(x+1, len(image) - 1, False, False)
        left = binary_search(0, y-1, True, True)
        right = binary_search(y+1, len(image[0]) - 1, True, False)

        print(top, bottom, left, right)

        return (right - left) * (bottom - top)


s = Solution()
# x = 4
# y = 4
# image = ["1111111101","1000000101","1011110101","1010010101","1010110101","1010000101","1011111101","1000000001","1111111111"]
x = 0
y = 2
image = ["0010","0110","0100"]

print("image:")
for i in range(len(image)):
    print(image[i])

print(s.minArea(image, x, y))
