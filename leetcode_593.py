class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        if p1==p2 or p2==p3 or p3==p4 or p4==p1 or p1==p3 or p2==p4:
            return False

        d = set()
        x1,y1 = tuple(p1)
        x2,y2 = tuple(p2)
        x3,y3 = tuple(p3)
        x4,y4 = tuple(p4)

        #p1,p2
        l1 = sqrt((x1-x2)**2 + (y1-y2)**2)
        d.add(l1)
        #p2,p3
        l2 = sqrt((x2-x3)**2 + (y2-y3)**2)
        d.add(l2)
        #p3,p4
        l3 = sqrt((x3-x4)**2 + (y3-y4)**2)
        d.add(l3)
        #p4,p1
        l4 = sqrt((x4-x1)**2 + (y4-y1)**2)
        d.add(l4)
        #p1,p3
        l5 = sqrt((x3-x1)**2 + (y3-y1)**2)
        d.add(l5)
        #p2,p4
        l6 = sqrt((x4-x2)**2 + (y4-y2)**2)
        d.add(l6)

        if len(d)==2:
            return True
        else:
            return False
