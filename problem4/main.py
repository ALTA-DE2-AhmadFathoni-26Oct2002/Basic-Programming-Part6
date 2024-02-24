def find_max_sum_sub_array(k, arr):
    n = len(arr)
    max_sum = 0
    window_sum = 0 
    for x in range(n - k + 1):
        window_sum  = 0
        for y in range(x, x+k ):
            window_sum += arr[y] 

            max_sum = max(window_sum, max_sum)
    return max_sum

if __name__ == '__main__':
    print(find_max_sum_sub_array(3, [2, 1, 5, 1, 3, 2])) # 9
    print(find_max_sum_sub_array(2, [2, 3, 4, 1, 5])) # 7
    print(find_max_sum_sub_array(2, [2, 1, 4, 1, 1])) # 5
    print(find_max_sum_sub_array(3, [2, 1, 4, 1, 1])) # 7
    print(find_max_sum_sub_array(4, [2, 1, 4, 1, 1])) # 8