


def swapPositions(list, pos1, pos2, pos3, pos4):
 
    
    get = list[pos1], list[pos2]
    list[pos2], list[pos1] = get


    get = list[pos3], list[pos4]
    list[pos4], list[pos3] = get

      
    return list

lst = [] 
lst = [int(item) for item in input( "enter the element: ").split()]
print("gift_presented_to =", end=" ")
print(lst)
       

 
pos1, pos2  = 3,5
pos3, pos4  = 4,5
print("Gift_recieved_from =", end=" ")
print(swapPositions( lst, pos1-1, pos2-1, pos3-1, pos4-1))