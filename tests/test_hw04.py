import importlib.util, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("main", ROOT / "weather_window.py")
main = importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(main)
sliding_window_max = main.sliding_window_max

def ref_sw_max(nums, k):
    if not nums or k <= 0:
        return []
    if k > len(nums):
        return [max(nums)]
    return [max(nums[i:i+k]) for i in range(len(nums)-k+1)]

# --- normal (4) ---
def test_classic_case():
    nums = [1,3,-1,-3,5,3,6,7]
    assert sliding_window_max(nums, 3) == [3,3,5,5,6,7]

def test_k_equals_len():
    assert sliding_window_max([4,2,12,3], 4) == [12]

def test_two_window():
    assert sliding_window_max([4,2,12,3], 2) == [4,12,12]

def test_k_one():
    assert sliding_window_max([1,-1], 1) == [1, -1]

# --- edge (3) ---
def test_empty_or_zero_k():
    assert sliding_window_max([], 3) == []
    assert sliding_window_max([1,2,3], 0) == []

def test_k_greater_than_len():
    assert sliding_window_max([2,2,2], 5) == [2]

def test_all_equal():
    assert sliding_window_max([5,5,5,5], 2) == [5,5,5]

# --- complex (3) ---
def test_increasing():
    nums = list(range(1,21))
    assert sliding_window_max(nums, 5) == ref_sw_max(nums, 5)

def test_decreasing():
    nums = list(range(20,0,-1))
    assert sliding_window_max(nums, 5) == ref_sw_max(nums, 5)

def test_mixed_large():
    nums = [9,1,3,7,7,2,6,6,6,5,4,10,10,9,8,7,6,5,4,3]
    assert sliding_window_max(nums, 4) == ref_sw_max(nums, 4)
