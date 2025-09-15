class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = []
        self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        items = self.dict[key]
        l, r = 0, len(items) - 1
        while l <= r:
            if l == r:
                # return items[l][1]
                if items[l][0] == timestamp:
                    return items[l][1]
                elif items[l][0] < timestamp:
                    return items[l][1]
                else:
                    if l > 0: return items[l-1][1]
                    return ""
            m = l + ((r - l) // 2)
            if timestamp == items[m][0]:
                return items[m][1]
            elif timestamp < items[m][0]:
                r = m - 1
            else:
                l = m + 1
        return ""
