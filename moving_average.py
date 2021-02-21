#Calculate moving average for a given window size
#example input: 10, 11, 12, 12, 13, 15, 17, 18
#size = 3
#returns list [11.667,12.333,13.333,15,16.667]

input= [10, 11, 12, 12, 13, 15, 17, 18]
size = 3


def get_moving_average(input:list, window_size: int) -> list:
    moving_average_list = []
    for i in range(len(input)):
        if i <= (len(input)-window_size):
            moving_average = sum(input[i: i+window_size])/window_size
            moving_average_list.append(moving_average)
    print(f"moving_average_list:{moving_average_list}")
    return moving_average_list
 
# Same function using list comprehension and lambda          
def get_moving_average(input:list, window_size: int) -> list:
    lists_with_window_size = [input[i: i+window_size] for i in range(len(input)) if i <= (len(input)-window_size)]
    print(f"lists_with_window_size: {lists_with_window_size}")
    moving_average_list = list(map(lambda x:sum(x)/window_size, lists_with_window_size))
    print(f"moving_average_list: {moving_average_list}")
    return moving_average_list

moving_average_list = get_moving_average(input, size)
