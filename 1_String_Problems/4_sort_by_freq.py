
def sort_freq(list):
    length = len(list)

    count_dict = {}
    
    for i in range(length):
        if list[i] in count_dict.keys():
            count_dict[list[i]] += 1
        else:
            count_dict[list[i]] = 1
        print(count_dict)
        

list = [1,2,3,4,1,2,1,3,1,3]
sort_freq(list)