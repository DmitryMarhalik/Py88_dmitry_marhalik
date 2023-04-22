x = 1
y = 2
sum_id_numbers = str(id(x)) + str(id(y))
result = int(sum_id_numbers) - id(y)
print(result)
