import sys
import timeit
# Lists
my_first_list=["java","R","Python"]
print(my_first_list)
  #Empty List
my_empty_list=list()
print(my_empty_list)
my_first_list.append("Kotlin")
print(my_first_list)
my_first_list.insert(3,"NJ")
print(my_first_list)
last_element=my_first_list.pop()
print(last_element)
print(my_first_list)
my_first_list.remove("java")
print(my_first_list)
# my_first_list.remove("LL");
print(my_first_list)
my_empty_list.append(3)
my_empty_list.append(5)
print(my_empty_list)
my_second_list=[1,2,-1,-5,-10,20]
print(my_second_list)
my_second_list.sort()
print(my_second_list)
my_second_list.reverse()
print(my_second_list)
my_third_list=my_first_list+my_second_list
print(my_third_list)
  #slicing
print(my_third_list[::-1])
my_first_list=my_third_list.copy()
my_first_list.append("Crazy")
print(my_first_list)
sequare_list=[i*2 for i in my_second_list]
print(sequare_list)
#Tuples
my_first_tuples=("java","python","R")
print(type(my_first_tuples))
number_of_java=my_first_tuples.count("java")
print("The number of elements "+str(number_of_java))
my_first_tuples.index("java")
my_second_tuples=tuple(my_first_list)
print(my_first_tuples.index("java"))
print(my_first_tuples.__repr__())
for i in my_first_tuples:
    print(i)
print(my_second_tuples[-1])
print(my_second_tuples)

if "R" in my_second_tuples:
    print(my_second_tuples.index("R"))
#unpacking using argument
my_third_tuples=("java","python","C++","MMM")
i1,*i2,i3=my_third_tuples
print(i2)
print(sys.getsizeof(my_third_list),"Megabytes")
print(timeit.timeit(stmt="[0,1,2,3,4]",number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4)",number=1000000))