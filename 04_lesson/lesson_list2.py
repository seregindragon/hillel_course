first_list = [2, 4, 5, 6, 7]
#first_list = first_list[1:3]  list_ part срез
#first_list[1:3] = [6, 7, 8]  # change element замена елемента
#print(first_list)
#####
#count

#print(first_list.count(6)) # count element = 6
#print(first_list.index(6)) # find index element
#first_list.sort() # sorting sort(reverse=True)

#second_list = first_list.copy() # copy list (but not list in list) the same list2 = list[:]
#list2 = list1.deepcopy() full copy list but need library "copy" import copy
#second_list.clear() clearing the list
# min max min(first_list) , max (first_list)
# all(list) if one have false = false
# any(list) if one have true = true


print(all(first_list))

