class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        left, right = 0, len(A) - 1
        while True:
            i = (left + right) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i + 1] if (i + 1) < len(A) else float('inf')

            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j + 1] if (j + 1) < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1


def main():
    print(Solution().findMedianSortedArrays(nums1=[1, 3], nums2=[2]))
    print(Solution().findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))


main()
