def intersection():
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    hashmap = {}
    intersection = []

    # for i in range(len(nums1)):
    #     hashmap[i] = hashmap.get(i, 0) + 1

    print(hashmap)

    print(nums2)

    for i in range(len(nums1)):
        if i in hashmap:
            hashmap[i] = hashmap.get(i, 0)
            intersection.append()

    print(intersection)
    return intersection


intersection()
