from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        k = 0
        students_que = deque(students)
        sandwiches = deque(sandwiches)

        while len(students_que) >= 0:
            if k == len(students_que):
                return len(students_que)
            elif students_que[0] == sandwiches[0]:
                students_que.popleft()
                sandwiches.popleft()
                k =0
            else:
                x = students_que.popleft()
                students_que.append(x)
                k +=1

        return 0
