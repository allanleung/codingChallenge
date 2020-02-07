import math

class Solution(object):
    def findStartingPosition(self, arr):
        """
        :type arr: Array[Array[int]]
        :rtype: (int, int)
        """
        
        height = len(arr)
        width = len(arr[0])
        startingX = 0
        startingY = 0
        # Height is EVEN and Width is EVEN
        if height % 2 == 0 and width % 2 == 0:
            x1 = int(width / 2)
            x2 = int((width / 2) - 1)
            y1 = int(height / 2)
            y2 = int((height / 2) - 1)

            a1 = arr[y1][x1]
            a2 = arr[y1][x2]
            a3 = arr[y2][x1]
            a4 = arr[y2][x2]

            mostCarrots = max(a1, a2, a3, a4)

            if mostCarrots == a1:
                startingX = x1
                startingY = y1
            elif mostCarrots == a2:
                startingX = x2
                startingY = y1
            elif mostCarrots == a3:
                startingX = x1
                startingY = y2
            else:
                startingX = x2
                startingY = y2

        # Height is ODD and Width is EVEN
        if height % 2 == 1 and width % 2 == 0:
            x1 = int(width / 2)
            x2 = int((width / 2) - 1)

            startingY = int(math.floor(height / 2))

            if arr[startingY][x1] > arr[startingY][x2]:
                startingX = x1
            else:
                startingX = x2

        # Height is EVEN and width is ODD
        if height % 2 == 0 and width % 2 == 1:
            y1 = int(height / 2)
            y2 = int((height / 2) - 1)

            startingX = int(math.floor(width / 2))

            if arr[y1][startingX] > arr[y2][startingX]:
                startingY = y1
            else:
                startingY = y2

        # Height and width is ODD
        if height % 2 == 1 and width % 2 == 1:
            startingY = int(math.floor(height / 2))
            startingX = int(math.floor(width / 2))

        return (startingX, startingY)

    def recursiveStep(self, arr, x, y):
        # We have eaten this many carrots
        currentCarrots = arr[y][x]
        # Mark the carrots as "eaten" (no more)
        arr[y][x] = 0
        print("Rabbit ate:", currentCarrots, "on position",(x,y))
        # Find the next place to hop
        nextStep = self.nextPosition(arr, x, y)

        if nextStep[0] == x and nextStep[1] == y:
            return currentCarrots
        else:
            return currentCarrots + self.recursiveStep(arr, nextStep[0], nextStep[1])

    def solveRecursively(self, arr):
        startingPosition = self.findStartingPosition(arr)
        return self.recursiveStep(arr, startingPosition[0], startingPosition[1])

    def solveIteratively(self, arr):
        # Find the starting position
        pos = self.findStartingPosition(arr)

        # Eat the carrots
        currentCarrots = arr[pos[1]][pos[0]]
        # Set the carrots to none
        arr[pos[1]][pos[0]] = 0
        # Find the next hop position
        nextPos = self.nextPosition(arr, pos[0], pos[1])

        print("Rabbit total carrots:", currentCarrots, "on position", pos[0], pos[1])
        # If there is a "next move" (where we don't sit in the same spot)
        while nextPos[0] != pos[0] or nextPos[1] != pos[1]:
            # Next position is our new position
            pos = nextPos

            # Eat the carrots and set it to none
            currentCarrots += arr[pos[1]][pos[0]]
            arr[pos[1]][pos[0]] = 0
            print("Rabbit total carrots:", currentCarrots, "on position", pos[0], pos[1])

            # Calculate the next hop
            nextPos = self.nextPosition(arr, pos[0], pos[1])

        return currentCarrots


    def nextPosition(self, arr, x, y):
        """
        :type arr: Array[Array[int]]
        :type x, y: int int 
        :rtype: (int, int)
        """
        height = len(arr)
        width = len(arr[0])

        nextStep = (x, y)
        maxCarrots = 0

        # Check if we can go UP
        if y - 1 >= 0:
            if arr[y - 1][x] > maxCarrots:
                nextStep = (x, y - 1)
                maxCarrots = arr[y - 1][x]
        # Check if we can go RIGHT
        if x + 1 < width:
            if arr[y][x + 1] > maxCarrots:
                nextStep = (x + 1, y)
                maxCarrots = arr[y][x + 1]
        # Check if we can go BOTTOM
        if y + 1 < height:
            if arr[y + 1][x] > maxCarrots:
                nextStep = (x, y + 1)
                maxCarrots = arr[y + 1][x]
        # Check if we can go LEFT
        if x - 1 >= 0:
            if arr[y][x - 1] > maxCarrots:
                nextStep = (x - 1, y)
                maxCarrots = arr[y][x - 1]

        return nextStep

if __name__ == '__main__':
    # Eating Order: 7,8,7,5 
    board_thin = [
                [5, 7, 8, 6, 3],
                []
            ]
    # Eating Order: 7,8,7,5 
    board = [
                [5, 7, 8, 6, 3],
                [0, 0, 7, 0, 4],
                [4, 6, 3, 4, 9],
                [3, 1, 0, 5, 8]
            ]
    # Eating Order 6, 7, 8, 6, 3, 4 
    board_even_odd = [
                [5, 8, 6, 3],
                [0, 7, 0, 4],
                [4, 6, 4, 0],
                [8, 1, 7, 9],
                [3, 1, 5, 8]
            ]
    # Eatinng Order: 4,9,8,5,1,3,4,3
    board_even_even = [
                [5, 7, 8, 3],
                [0, 0, 0, 4],
                [4, 3, 4, 9],
                [3, 1, 5, 8]
            ]
    # Eating Order: 3,8,3,6,4,1,3,1
    board_odd_odd = [
                [5, 7, 8, 6, 3],
                [0, 0, 7, 0, 4],
                [4, 6, 3, 4, 9],
                [1, 3, 8, 2, 2],
                [3, 1, 0, 5, 8]
            ]
    solution = Solution()
    #print(solution.solveIteratively(board))
    #print(solution.solveIteratively(board_even_odd))
    #print(solution.solveIteratively(board_even_even))
    #print(solution.solveIteratively(board_odd_odd))
    print(solution.solveRecursively(board))
    #print(solution.solveRecursively(board_even_odd))
    #print(solution.solveRecursively(board_even_even))
    #print(solution.solveRecursively(board_odd_odd))



    