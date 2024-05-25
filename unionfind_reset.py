class UnionFind:
    def __init__(self, size: int):
        self.group = [i for i in range(size)]
        self.rank = [0] * size
        self.components = size
    def find(self, node: int) -> int:
        if self.group[node] != node:
            self.group[node] = self.find(self.group[node])
        return self.group[node]
    def reset(self,node):
        self.group[node] = node
        self.rank[node] = 0
    def union(self, node1: int, node2: int):
        group1 = self.find(node1)
        group2 = self.find(node2)
        
        # node1 and node2 already belong to same group.
        if group1 == group2:
            return 1
        self.components-=1
        if self.rank[group1] > self.rank[group2]:
            self.group[group2] = group1
        elif self.rank[group1] < self.rank[group2]:
            self.group[group1] = group2
        else:
            self.group[group1] = group2
            self.rank[group2] += 1
        return 0
    def connected(self, node1: int, node2: int) -> bool:
        return self.find(node1) == self.find(node2)
    def done(self):
        return self.components == 1