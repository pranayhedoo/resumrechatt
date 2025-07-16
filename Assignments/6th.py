#    Q1. Find the Intersection of two lists  

# List1 = [1,2,3,4]
# list2 = [3,4,5,6]

# def intersection_loop(lst1 , lst2):
#     common_list = []
#     for item in lst1:
#         if item in lst2 and item not in common_list:
#             common_list.append(item)
#     return common_list

# print(intersection_loop(List1,list2))

#   Q2.  Find the most frequent element in a list 

# Number = [1,2,2,3,3,3,4,4,5]

# def most_freq(lst):
#     max_count = 0
#     max_freq = None
#     for item in lst:
#         count = lst.count(item)
#         if count > max_count:
#             max_count = count
#             most_freq = item
#     return most_freq

# print(most_freq(Number))

#    Q3.  Find cumulative sum of a list     Addition for all sums

# Number = [1,2,3,4,5,6]
# def Cumulative_sum(lst):
#     cum_sum = []
#     total = 0
#     for num in lst:
#         total += num
#         cum_sum.append(total)
#     return cum_sum
    
# print(Cumulative_sum(Number))

#   Q4.   Remove duplicates from a list - 2 methods

# fruits = ["Apple" , "banana" , "cherry" , "Apple"]

# def remove_duplicate(lst):
#     unique = []
#     seen = set()
#     for item in lst:
#         if item not in seen:
#          unique.append(item)
#          seen.add(item)
#     return unique
# print(remove_duplicate(fruits))

#  Q5.  Find the index of an element in a tuple 

# my_tuple = (1,2,3,4)

# def find_index(tuple , element):
#    return tuple.index(element) if element in tuple else -1

# print(find_index(my_tuple,2))

#  Q6.  Find the most frequent value in a dictonary 

# data = {"a" : 1 , "b" : 2 , "c" : 2 , "d" : 4 , "e" : 5}

# def most_frequent(dct):
#     frequency = {}
#     for value in dct.values():
#         if value not in frequency:
#             frequency[value] = 0 
#         frequency[value] += 1
#     max_value = max(frequency , key= frequency.get)
#     return max_value
# print(most_frequent(data))

#   Q7.  Merge Dictonaries with summaton

# dict1 = {"a" : 10 , "b" : 20 , "c" : 30} 
# dict2 = {"b" : 40 , "c" : 50 , "d" : 60}

# def merge_dict(dict1 , dict2):
#     result = dict1.copy()
#     for key, value in dict2.items():
#       if key in result:
#          result[key] += value
#       else:
#          result[key] = value
#     return result
# print(merge_dict(dict1 , dict2))

#   Q8.  Flatten a Nested Dictonary

# data = {"a" : {"b" : {"c":42} , "d" : 7 }, "e" : 10}

# def flatten_dict(data,parent_key="", sep = "."):
#   item = {}    #  initialize empty dict to share flattened item
#   for key , value in data.items():
#     #  combine curren key with parent key
#     new_key = f"{parent_key}{sep}{key}" if parent_key else key
#     if isinstance(value , dict):
#       item.update(flatten_dict(value, new_key , sep))
#       #  recursive flatten the nested disc
#     else:
#       # adding key-value ti flatten dict
#       item[new_key] = value
#   return item
# print(flatten_dict(data))

#   Q9.  Sort a dictonary by values       Accending order 

# data = {"a" : 5, "b" : 9, "c" : 8, "d" : 5}

# def sort_by_values(data):
#     sorted_items = sorted(data.items(),key = lambda item : item[1])    # adding  reverse=True for decending
#     return {key : value for key , value in sorted_items}
# print(sort_by_values(data)) 

#   Q10.  Access vaulue from a nested dictonary  

# data = {
#     'person': {
#         'name': 'Alice',
#         'address': {
#             'city': 'Wonderland',
#             'zip': '12345'
#         }
#     }
# }

# # Accessing the city
# city = data['person']['address']['city']
# print(city)  # Output: Wonderland
