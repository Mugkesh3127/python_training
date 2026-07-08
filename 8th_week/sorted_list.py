import heapq

def merge_k_sorted_lists(lists):
    heap = []
    result = []

    # Push the first element of each list into the heap
    for list_index, lst in enumerate(lists):
        if lst:  # Ignore empty lists
            heapq.heappush(heap, (lst[0], list_index, 0))

    while heap:
        # Get the smallest element
        value, list_index, element_index = heapq.heappop(heap)
        result.append(value)

        # Push the next element from the same list
        next_index = element_index + 1
        if next_index < len(lists[list_index]):
            heapq.heappush(
                heap,
                (
                    lists[list_index][next_index],
                    list_index,
                    next_index
                )
            )

    return result


# -----------------------------
# Test
# -----------------------------
lists = [
    [1, 4, 5],
    [1, 3, 4],
    [2, 6]
]

print(merge_k_sorted_lists(lists))