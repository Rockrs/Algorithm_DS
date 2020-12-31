class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:

        if x==0:
            return 0
        forbidden_set = set(forbidden)
        visited = set()

        def min_jump(curr_pos, b_jump):
            if (curr_pos, b_jump) in visited:
                return float("inf")
            elif curr_pos in forbidden_set:
                return float("inf")
            elif curr_pos < 0:
                return float("inf")
            elif curr_pos > 6544:
                return float("inf")
            elif curr_pos ==x:
                return 0
            elif b_jump ==1:
                visited.add((curr_pos, b_jump))
                return 1 + min_jump(curr_pos + a, 0)
            else:
                visited.add((curr_pos, b_jump))
                c = 1 + min_jump(curr_pos + a, 0)
                d = 1 + min_jump(curr_pos - b, 1)
                return min(c, d)

        res = min_jump(0, 0)
        if res==0 or res==float("inf"):
            return -1
        else:
            return res
