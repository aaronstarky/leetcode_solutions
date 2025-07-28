# IN PROGRESS

# if domino i and j are pushed in opposite directions and the dominoes between them is divisible by two
# tile[i] = L will progress to left if tile[i-1] != L || R and tile[i-2] != R
# tile[i] = R will progress to right if tile[i+1] != L || R and tile[i+2] != L
class Solution:

    def makeEvenSplit(self, length: int) -> str:
        return "R" * (length // 2) + "." * (length % 2) + "L" * (length // 2)
    
    def pushDominoes(self, dominoes: str) -> str:
        print(dominoes)
        indexOfLastR = -1
        stuck = []
        for i in range(len(dominoes)):
            if dominoes[i] == ".":
                continue
            if dominoes[i] == "L":
                if indexOfLastR == -1:
                    dominoes = dominoes[:i] + "L" * (i + 1) + dominoes[i+1:]
                else:
                    dominoes = dominoes[:indexOfLastR + 1] + self.makeEvenSplit(i - indexOfLastR - 1) + dominoes[i:]
                indexOfLastR = -1
            elif dominoes[i] == "R":
                indexOfLastR = i
        if indexOfLastR != -1:
            dominoes = dominoes[:indexOfLastR + 1] + "R" * (len(dominoes) - indexOfLastR - 1)
            
            