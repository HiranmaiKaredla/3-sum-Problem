class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        mini = abs(min(max(A),sum(A)))
        s=0
        for i in range(len(A)-2):
            for j in range(i+1,len(A)-1):
                for k in range(j+1,len(A)):
        
                    summ=A[i] + A[j] + A[k]
                    if abs(summ-B) < mini:
                        mini=abs(summ-B)
                        s=summ
        return s
