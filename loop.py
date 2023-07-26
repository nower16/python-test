
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
print(raise_to_power(3,4))


#2D List 

number_grid = [
    [1,2,3], 
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[2][2])

# Nested loops(for loop inside for loop)

for row in number_grid:
    for col in row:
        print(col)