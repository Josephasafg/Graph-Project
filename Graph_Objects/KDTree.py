import scipy.spatial


class KDTree:
    def __init__(self, data):
        # store kd-tree
        self.__tree = scipy.spatial.cKDTree(data)

    @property
    def tree(self):
        return self.__tree

    @tree.setter
    def tree(self, value):
        self.__tree = value

    def search(self, inp, k=1):
        if len(inp.shape) >= 2:  # multi input
            index = list()
            dist = list()

            for i in inp.T:
                i_dist, i_index = self.tree.query(i, k=k)
                index.append(i_index)
                dist.append(i_dist)

            return index, dist

        dist, index = self.tree.query(inp, k=k)
        return index, dist

    def search_in_distance(self, inp, radius):
        index = self.tree.query_ball_point(inp, radius)
        return index
