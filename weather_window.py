import heapq

def sliding_window_max(nums, k):
    if k <= 0 or not nums:
        return []
    if k > len(nums):
        return [max(nums)]

    result = []
    heap = []  # max-heap using (-value, index)

    for i in range(len(nums)):
        heapq.heappush(heap, (-nums[i], i))

        # Remove elements that are out of the current window
        while heap[0][1] <= i - k:
            heapq.heappop(heap)

        # Record max value once the first window is complete
        if i >= k - 1:
            result.append(-heap[0][0])

    return result