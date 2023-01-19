import unittest


class Solution:
    def intersect(self, nums1, nums2):
        if nums2 < nums1:
            nums1, nums2 = nums2, nums1

        map1 = {}
        for i in range(len(nums1)):
            if nums1[i] not in map1:
                map1[nums1[i]] = 0
            map1[nums1[i]] += 1

        result = []
        for i in range(len(nums2)):
            if nums2[i] in map1:
                map1[nums2[i]] -= 1
                result.append(nums2[i])
                if map1[nums2[i]] == 0:
                    del map1[nums2[i]]

        return result


class TestTwoSum(unittest.TestCase):

    def test_first(self):
        expected = [2, 2]
        self.assertEqual(expected, Solution().intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))

    def test_second(self):
        expected = [4, 9]
        self.assertEqual(expected, Solution().intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))


if __name__ == "__main__":
    unittest.main()
