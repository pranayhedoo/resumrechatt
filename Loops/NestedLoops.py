    # Defn  :-  loop inside another loop is called nested loop.

#  priny number from 1 to 3

# for i in range(3):    #  outer loop
#  for num in range(1,4):    # inner loop
#     print(num)
#  print("-----")


    # for using while loop  in nested loop 

# i = 1

# while i < 4:
#     for j in range(1,4):
#         print(j)
#     print("-----")
#     i += 1


    #  print prime no. betn 2 to 10

for num in range(2,20):
    for i in range(2,num):
        if num % i == 0:
            break
        else:
            print(num)