
### General Tree Creation In Python and printing created tree based of some condition

# =============================================================================
#     Abhishek (CEO)
#         Divas (CTO)
#             Shekhar (INFRA Head)
#             Vipul (Cloud Head)
#             Rakesh (App Manager)
#         Naveen (HR Head)
#             Sanjay (Recruitement Head)
#             Bhavesh (Company HR)
# =============================================================================



# =============================================================================
# if condition =="name"
# print tree with name only
# 
# elif condition=="desig"
# print tree with designation only
# 
# else
# print whole tree
# =============================================================================



class Tree:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent  = None
        
    def add_child(self,node):
        self.children.append(node)
        node.parent = self 
        
    def print_tree(self,condition,space=0):
        spaces = " " * space
        print_by = ""
        name , *temp = self.data.split()
        desig = " ".join(str(items) for items in temp)
        
        if condition=="designation":
            print_by = desig
        elif condition=="name":
            print_by = name
        else:
            print_by = self.data
            
        print (spaces + print_by)
        if self.children is []:
            return
        else:
            for child in self.children:
                child.print_tree(condition,space =space+3)


def build_product_tree(condition):
    CEO = Tree("Abhishek (CEO)")
    CTO = Tree("Divas (CTO)")
    HR = Tree("Naveen (HR Head)")
    
    CEO.add_child(CTO)
    CEO.add_child(HR)
    
    CTO.add_child(Tree("Shekhar (INFRA Head)"))
    CTO.add_child(Tree("Vipul (Cloud Head)"))
    CTO.add_child(Tree("Rakesh (App Manager)"))
    
    HR.add_child(Tree("Sanjay (Recruitement Head)"))
    HR.add_child(Tree("Bhavesh (Company HR)"))
    
    return CEO.print_tree(condition)

if __name__ =="__main__":
    print(build_product_tree("name"))
    print (build_product_tree("designation"))
    print(build_product_tree("both"))
    