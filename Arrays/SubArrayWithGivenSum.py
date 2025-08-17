'''
Subarray with Given Sum 
o Example: 
Input: arr = [1,2,3,7,5], sum = 12 
Output: [2,4] '''
def subArray(arr,sum):
    currsum=0
    start=0
    for end in range(len(arr)):
        currsum+=arr[end]
        while currsum>sum and start<len(arr):
            currsum-=arr[start]
            start+=1
        if currsum==sum:
            return [start+1,end+1]

arr=[1,2,3,7,5]
sum=12
print(subArray(arr,sum))
    