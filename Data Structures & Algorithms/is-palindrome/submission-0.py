class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=str.lower(s).replace(" ", "")
        print(string)

        left = 0
        right = len(string)-1
        
        for c in range(len(string)):
            leftC = string[left]
            rightC = string[right]
            
            if (leftC.isalnum() != True):
                left+=1
            elif (rightC.isalnum() != True):
                right-=1
            elif (leftC == rightC):
                left+=1
                right-=1
            else:
                return False

        return True