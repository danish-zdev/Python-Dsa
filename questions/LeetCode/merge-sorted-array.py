def merge(nums1, m, nums2, n):

    k = len(nums1)-m
    for _ in range(k):
        nums1.pop(-1)
    nums1.extend(nums2)
    return sorted(nums1)

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

print(merge(nums1, m, nums2, n))
# Output: [1,2,2,3,5,6]