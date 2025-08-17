'''
Longest Consecutive Sequence 
o Example: 
Input: [100,4,200,1,3,2] 
Output: 4 
'''
def longestConsecutiveSeq(arr):
    seq=0
    num=set(arr)
    for n in num:
        if n-1 not in arr:
            count=1
            while n+1 in arr:
                count+=1
                n=n+1
        seq=max(count,seq)
    print(seq)
longestConsecutiveSeq([1,2,100,3,4,5,6,8])
            
                
