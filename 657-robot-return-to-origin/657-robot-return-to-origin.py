class Solution:
    def judgeCircle(self, moves: str) -> bool:
        movement = {
            "U": [0, 1],
            "D": [0, -1],
            "L": [-1, 0],
            "R": [1, 0]
        }
        
        startX = 0
        startY = 0
        for move in moves:
            startX += movement[move][0]
            startY += movement[move][1]
        return startX == 0 and startY == 0