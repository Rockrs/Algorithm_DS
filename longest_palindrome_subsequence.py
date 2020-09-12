dp = [[0]*13 for _ in range(13)]

def l_palindrome(s,i,j):
    if i==j:
        return 1
    if i>j:
        return 0
    
    if dp[i][j] is not 0:
        return dp[i][j]
    
    
    if s[i]==s[j]:
        dp[i][j]= 2+l_palindrome(s,i+1,j-1)
        return dp[i][j]
    else:
        temp1=l_palindrome(s,i,j-1) 
        temp2=l_palindrome(s,i+1,j)
        
        if temp1>temp2:
            dp[i][j]= temp1
        else:
            dp[i][j]= temp2
        
        return dp[i][j]
        
    return dp[4][4]


s = "geeksforgeeks"
l = len(s)
print(l_palindrome(s,0,l-1))