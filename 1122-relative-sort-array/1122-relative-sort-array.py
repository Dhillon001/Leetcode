class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = Counter(arr1)
        result = []

    # add elements in arr2 order
        for x in arr2:
            result.extend([x] * freq[x])
            del freq[x]

    # add remaining elements sorted
        for x in sorted(freq):
            result.extend([x] * freq[x])

        return result