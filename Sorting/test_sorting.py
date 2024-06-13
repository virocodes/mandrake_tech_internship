import unittest
import random
from sorting import bubble_sort, quick_sort

class TestSorting(unittest.TestCase):

    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(bubble_sort([3, 1, 4, 5, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(bubble_sort([1]), [1])
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(bubble_sort([2, 2, 2, 2, 2]), [2, 2, 2, 2, 2])
        self.assertEqual(bubble_sort([5, 3, 8, 6, 2, 7, 4, 1, 9, 0]), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(bubble_sort([i for i in range(100)]), [i for i in range(100)])
        self.assertEqual(bubble_sort([i for i in range(100, 0, -1)]), [i for i in range(1, 101)])
        large_random_list = [random.randint(0, 1000) for _ in range(100)]
        self.assertEqual(bubble_sort(large_random_list), sorted(large_random_list))
        self.assertEqual(bubble_sort([-1, -3, -2, 0, 2, 1, -4]), [-4, -3, -2, -1, 0, 1, 2])
        self.assertEqual(bubble_sort([4, 1, 3, 2, 2, 4, 5, 3, 1]), [1, 1, 2, 2, 3, 3, 4, 4, 5])

    def test_quick_sort(self):
        self.assertEqual(quick_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(quick_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(quick_sort([3, 1, 4, 5, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(quick_sort([1]), [1])
        self.assertEqual(quick_sort([]), [])
        self.assertEqual(quick_sort([2, 2, 2, 2, 2]), [2, 2, 2, 2, 2])
        self.assertEqual(quick_sort([5, 3, 8, 6, 2, 7, 4, 1, 9, 0]), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(quick_sort([i for i in range(100)]), [i for i in range(100)])
        self.assertEqual(quick_sort([i for i in range(100, 0, -1)]), [i for i in range(1, 101)])
        large_random_list = [random.randint(0, 1000) for _ in range(100)]
        self.assertEqual(quick_sort(large_random_list), sorted(large_random_list))
        self.assertEqual(quick_sort([-1, -3, -2, 0, 2, 1, -4]), [-4, -3, -2, -1, 0, 1, 2])
        self.assertEqual(quick_sort([4, 1, 3, 2, 2, 4, 5, 3, 1]), [1, 1, 2, 2, 3, 3, 4, 4, 5])


if __name__ == '__main__':
    unittest.main()