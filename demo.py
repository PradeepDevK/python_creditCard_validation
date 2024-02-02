card_no = "5610591081018250"
number = list(card_no)

print(card_no)
print(number)

odd_index_sum = 0
even_double_list = []
for (idx,val) in enumerate(number):
    if idx%2 != 0:
        odd_index_sum += int(val)
    else:
        even_double_list.append(int(val) * 2)

print("odd_index_sum", odd_index_sum)
print("even_double_list", even_double_list)

#convert list into a string
even_double_string = ""
for x in even_double_list:
    even_double_string += str(x)

print("even_double_string", even_double_string)

#convert sting back to list
double_list = list(even_double_string)
print("double_list", double_list);

even_index_sum = 0
for x in double_list:
    even_index_sum += int(x)

print("even_index_sum", even_index_sum)

sum_odd_even = odd_index_sum + even_index_sum;
print("sum_odd_even", sum_odd_even)

if sum_odd_even % 10 == 0:
    print("Valid Card")
else:
    print("Invalid Card")