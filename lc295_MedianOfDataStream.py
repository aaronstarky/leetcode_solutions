class MedianFinder:
    arr: list[int]

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        if len(self.arr) == 0: 
            self.arr.append(num)
            return
        # binary search to find the place for the number
        l, r = 0, len(self.arr) - 1
        while l <= r:
            if r == l:
                if num <= self.arr[l]:
                    self.arr.insert(l, num)
                else:
                    self.arr.insert(l+1, num)
                break
            m = l + ((r - l) // 2)
            if self.arr[m] < num:
                l = m + 1
            elif self.arr[m] > num:
                r = m
            else:
                l, r = m, m

    def findMedian(self) -> float:
        if len(self.arr) % 2 == 0:
            m  = len(self.arr) // 2
            return (self.arr[m] + self.arr[m-1]) / 2
        else:
            m = len(self.arr) // 2
            return self.arr[m]
