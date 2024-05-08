class Solution:
    def merge(self, nums1, m, nums2, n):
        # Initialize pointers for nums1, nums2 and the last index of merged array
        i, j, k = m - 1, n - 1, m + n - 1

        # Merge in reverse order
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
