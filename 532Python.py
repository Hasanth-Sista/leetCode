'''
Created on Oct 1, 2017

@author: sista
'''


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #nums=[3,1,4,1,5]
        #k=2
        output=[]
        output1=[]
        output2=[]
        var=[]
        for i in range(len(nums)):
            for j in range(i):
                if(abs(nums[i]-nums[j]) == k):
                    var.append(nums[i])
                    var.append(nums[j])
                    output.append(var)
                    var=[]

        for i in output:
            if i not in output1:
                output1.append(i)
    
        for j in output1:
            if (j not in output2) and (j[::-1] not in output2):
                output2.append(j)
        
        return (len(output2))
        
        
sol=Solution();
nums=[3,1,4,1,5];
k=2;
print(sol.findPairs(nums, k))

