# http://www.cnblogs.com/grandyang/p/5209621.html
class Vector2D:
    def __init__(self, vec2d):
        self.vec2d = vec2d

    def next(self):
        return self.vec2d.pop(0)

    def hasNext(self):
        if len(self.vec2d) > 0:
            if type(self.vec2d[0]) is list:
                for i in self.vec2d.pop(0)[::-1]:
                    self.vec2d.insert(0, i)
            return True
        else:
            return False

vector = \
[
  [1,2],
  [3],
  [4,5,6]
]
s = Vector2D(vector)
while s.hasNext():
    print(s.next())


