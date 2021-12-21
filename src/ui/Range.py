class Range:

    def __init__(self, max, min):
        self.max = max
        self.min = min

    def getPortion(self, d):
        d1 = d - self.min
        ans = d1 / (self.max - self.min)
        return ans

    def fromPortion(self, p):
        return self.min + p * (self.max - self.min)


class Range2D:

    # x_range , y_rang -> Range
    def __init__(self, x_range, y_range):
        self.x_range = x_range
        self.y_range = y_range

    def getPortion(self, p):
        x = self.x_range.getPortion(p[0])
        y = self.y_range.getPortion(p[1])

        return (x, y, 0)

    def fromPortion(self, p):
        x = self.x_range.fromPortion(p[0])
        y = self.y_range.fromPortion(p[1])

        return (x, y, 0)


class Range2Range:
    # w , f->Range2D
    def __init__(self, world, frame):
        self.world = world
        self.frame = frame

    def worldToframe(self, p):
        d = self.world.getPortion(p)
        ans = self.frame.fromPortion(d)

        return ans

    def frameToWorld(self, p):
        d = self.frame.getPortion(p)

        return self.world.fromPortion(d)


class WorldGraph:

    def __init__(self):
        pass

    def GraphRange(self, graph):

        x0, x1, y0, y1 = 0, 0, 0, 0
        first = True
        for n in graph.get_all_v().values():
            p = n.pos

            if first:
                x0 = p[0]
                x1 = x0
                y0 = p[1]
                y1 = y0
                first = False
            else:
                if p[0] < x0:
                    x0 = p[0]

                if p[0] > x1:
                    x1 = p[0]
                if p[1] < y0:
                    y0 = p[1]
                if p[1] > y1:
                    y1 = p[1]

        xr = Range(x0, x1)
        yr = Range(y0, y1)

        return Range2D(xr, yr)

    def w2f(self, g, frame):
        world = self.GraphRange(g)
        ans = Range2Range(world, frame)

        return ans
