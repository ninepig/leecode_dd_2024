# https://www.fastprep.io/problems/find-minimum-pages-per-day

'''

A student is preparing for a test from amazon academy for a scholarship.

The student is required to completely read n chapters (which is the length of the pages array) for the test where the ith chapter has pages[i] number of pages.
The chapters are read in increasing order of the index. Each day the student can either read till the end of a chapter or at the most x pages, whichever is minimum. The number of pages remaining to read decreases by x in the later case.

'''
def minimumNumberOfPages(pages, days):
    def totalDays(num_pages):
        total = 0
        for page_count in pages:
            total += (page_count + num_pages - 1) // num_pages
        return total

    low = 1
    high = max(pages)
    result = float('inf')

    while low <= high:
        mid = (low + high) // 2
        total = totalDays(mid)

        if total <= days:
            # OK but try to find a smaller solution
            result = min(result, mid)
            high = mid - 1
        else:
            low = mid + 1

    if result == float('inf'):
        return -1
    else:
        return result


print(minimumNumberOfPages([5, 3, 4], 4))  # output 4
print(minimumNumberOfPages([2, 3, 4, 5], 5))  # output 4
print(minimumNumberOfPages([2, 3, 4], 4))  # output 3