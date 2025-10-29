"""
HW04 — Weather Window: Sliding Maximum

Implement sliding_window_max(nums, k) -> list
"""

def sliding_window_max(nums, k):
    # TODO:
    # Use a max-heap via (-value, index).
    # Push current item; pop while top index <= i - k (out of window).
    # When i >= k-1, record current window max as -heap[0][0].
    # Handle k <= 0, empty list, and k > len(nums).
    raise NotImplementedError
