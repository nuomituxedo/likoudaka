class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks, counter_a, counter_b = 0, collections.Counter(), collections.Counter()
        for a, b in zip(arr, sorted(arr)):
            counter_a[a] += 1
            counter_b[b] += 1
            #at any time where both counter arrays are identical
            #it means we've reached a new sortable chunk 
            chunks += counter_a == counter_b
        return chunks