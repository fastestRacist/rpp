import sys

args_list = sys.argv

array = [int(args_list[i]) for i in range(1, len(args_list))]
even_sum = 0
odds_prod = 1
for i in range(len(array)):
    if not i % 2:
        even_sum += array[i]
    else:
        odds_prod *= array[i]
print(array,'\n',even_sum,'\n',odds_prod)