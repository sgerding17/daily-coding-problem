#!/usr/bin/python3

class heap:
    def __init__(self):
        self.a = []

    def parent(idx):
        return int((idx - 1) / 2)

    def lchild(idx):
        return idx * 2 + 1

    def rchild(idx):
        return idx * 2 + 2

    def minchild(self, idx):
        lchild = heap.lchild(idx)
        rchild = heap.rchild(idx)

        assert lchild < len(self.a)

        if rchild < len(self.a) and self.a[rchild] < self.a[lchild]:
            return rchild
        else:
            return lchild

    def swap(self, idx1, idx2):
        temp = self.a[idx1]
        self.a[idx1] = self.a[idx2]
        self.a[idx2] = temp

    def push(self, v):
        self.a.append(v)

        idx = len(self.a) - 1
        while heap.parent(idx) >= 0:
            parent = heap.parent(idx)
            if self.a[idx] < self.a[parent]:
                self.swap(idx, parent)
                idx = parent
            else:
                break

    def pop(self):
        self.swap(0, -1)
        top = self.a.pop()

        idx = 0
        while heap.lchild(idx) < len(self.a):
            minchild = self.minchild(idx)
            if self.a[idx] > self.a[minchild]:
                self.swap(idx, minchild)
                idx = minchild
            else:
                break

        return top

if __name__ == '__main__':
    import random
    for i in range(100):
        a = [random.randrange(-100, 100) for _ in range(random.randrange(1, 100))]
        random.shuffle(a)
        h = heap()
        for v in a: h.push(v)
        b = [h.pop() for _ in a]
        assert sorted(a) == b
