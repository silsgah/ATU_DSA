def binary_search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        # Avoids integer overflow in languages like Java/C++, standard Python handles large ints fine
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            # We need bigger numbers, discard left half
            left = mid + 1
        else:
            # We need smaller numbers, discard right half
            right = mid - 1
            
    return -1


def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left: list[int], right: list[int]) -> list[int]:
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    # Append any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    print("Find 9 index:", binary_search(nums, 9)) 
    print("Find 2 index:", binary_search(nums, 2)) 

    unsorted_arr = [38, 27, 43, 3, 9, 82, 10]
    print("Sorted array:", merge_sort(unsorted_arr)) 
