
##Complete this code
def arrange(arr, n):

    for i in range(n):
        arr[i] = arr[i]+ (arr[arr[i]]%n)*n

    for i in range(n):
        arr[i] = arr[i]//n



#{
#  Driver Code Starts
#Initial Template for Python 3


import math
def main():
        T=int(input())
        while(T>0):

            n=int(input())

            arr=[int(x) for x in input().strip().split()]

            arrange(arr,n)

            for i in arr:
                print(i,end=" ")

            print()

            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
