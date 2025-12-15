class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            prev = res[-1] #this gets the previous row
            curr = [1] #new row starts with 1

            #middle elements: curr[j] = prev[j-1] + prev[j]
            for j in range(1, i):
                curr.append( prev[j-1] + prev[j])
            curr.append(1) # adding the last element
            res.append(curr) #adding the complete row into res
        return res

