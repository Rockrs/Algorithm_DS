class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome)==1:
            return ""

        n = len(palindrome)
        arr = [item for item in palindrome]

        for i in range(n):
            if i ==n//2 and n %2==1:
                pass
            elif arr[i] !='a':
                arr[i] = 'a'
                break

        if "".join(arr) == palindrome:
            arr[n-1] = 'b'
            return "".join(arr)
        else:
            return "".join(arr)
