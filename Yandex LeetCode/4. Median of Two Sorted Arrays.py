class Solution:
    def find(self, array1, first_idx1, last_idx1, array2, first_idx2, last_idx2, length_half):
        if last_idx1 - first_idx1 < 0:
            return array2[length_half + first_idx2]

        if last_idx2 - first_idx2 < 0:
            return array1[length_half + first_idx1]

        if length_half < 1:
            return min(array1[length_half + first_idx1], array2[length_half + first_idx2])

        ia, ib = (first_idx1 + last_idx1) // 2, (first_idx2 + last_idx2) // 2
        ma, mb = array1[ia], array2[ib]
        if (ia - first_idx1) + (ib - first_idx2) < length_half:
            if ma > mb:
                return self.find(array1, first_idx1, last_idx1, array2, ib + 1, last_idx2, length_half - (ib - first_idx2) - 1)
            else:
                return self.find(array1, ia + 1, last_idx1, array2, first_idx2, last_idx2, length_half - (ia - first_idx1) - 1)
        else:
            if ma > mb:
                return self.find(array1, first_idx1, ia - 1, array2, first_idx2, last_idx2, length_half)
            else:
                return self.find(array1, first_idx1, last_idx1, array2, first_idx2, ib - 1, length_half)

    def findMedianSortedArrays(self, nums1, nums2):
        length = len(nums1) + len(nums2)
        last_idx1 = len(nums1) - 1
        last_idx2 = len(nums2) - 1

        # odd
        if length % 2 == 1:
            return self.find(
                array1=nums1,
                first_idx1=0,
                last_idx1=last_idx1,

                array2=nums2,
                first_idx2=0,
                last_idx2=last_idx2,

                length_half=length // 2
            )
        # even
        else:
            a = self.find(
                array1=nums1,
                first_idx1=0,
                last_idx1=last_idx1,

                array2=nums2,
                first_idx2=0,
                last_idx2=last_idx2,

                length_half=length // 2
            )

            b = self.find(
                array1=nums1,
                first_idx1=0,
                last_idx1=last_idx1,

                array2=nums2,
                first_idx2=0,
                last_idx2=last_idx2,

                length_half=length // 2 - 1
            )

            return a + b / 2.0


print(Solution().findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))
