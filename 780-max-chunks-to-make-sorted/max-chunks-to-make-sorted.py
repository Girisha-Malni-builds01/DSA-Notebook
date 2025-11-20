class Solution(object):
    def maxChunksToSorted(self, arr):
        max_seen=0
        chunks=0
        for i in range(0,len(arr)):
            max_seen=max(max_seen,arr[i])
            if max_seen==i:
                chunks+=1
        return chunks
        