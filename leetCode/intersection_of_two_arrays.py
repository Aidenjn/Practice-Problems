# Given two arrays, write a function to compute their intersection

def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    """

    # Try 1: Double for-loop brute force
    """
    retAr = []
    nums1.sort()
    nums2.sort()

    for i in range(0, len(nums1)):
        for j in range(0, len(nums2)):
            if (nums1[i] == nums2[j]):
                retAr.append(nums2[j])
                del nums2[j]
                break
    return retAr
    """

    # Try 2: Treat as two stacks only comparing and removing the tops
    retAr = []
    nums1.sort()
    nums2.sort()

    while (len(nums1) != 0 and len(nums2) != 0):
        if (nums1[0] == nums2[0]):
            retAr.append(nums1[0])
            del nums1[0]
            del nums2[0]
        elif (nums1[0] < nums2[0]):
            del nums1[0]
        else:
            del nums2[0]
    return retAr

A = [1,2,2,1]
B = [2,2]

print(intersect(A, B))
