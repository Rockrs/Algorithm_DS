class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:

        queens_set = set()
        for item in queens:
            queens_set.add(tuple(item))

        ans = []

        def inside(row, col):
            if row<0 or row==8 or col<0 or col==8:
                return False
            else:
                return True

        for i in range(-1, 2):
            for j in range(-1, 2):
                row = king[0]
                col = king[1]

                if i==0 and j==0:
                    pass
                else:
                    while inside(row, col)==True and (row, col) not in queens_set:
                        row += i
                        col += j

                    if (row, col) in queens_set:
                        ans.append([row, col])

        return ans
        
