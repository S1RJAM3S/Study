arr = [int(x) for x in input().split()]
k = int(input())

def check(arr: list, k: int, page_lim: int) -> bool:
    count = 1
    page_sum = 0
    for pages in arr:
        if (page_sum + pages > page_lim):
            count += 1
            page_sum = pages
        else: page_sum += pages
    return count <= k

def find_pages(arr: list, k: int) -> int:
    if (k > len(arr)): return -1
    
    low = max(arr)
    high = sum(arr)
    res = -1
    
    while (low <= high):
        mid = low + (high - low) // 2
        if (check(arr, k, mid)):
            res = mid
            high = mid - 1
        else: low = mid + 1
    return res

print(find_pages(arr, k))