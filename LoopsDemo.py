i = 1
while i <= 10:
    print(i)
    i+=1
print("Done with while loop")

for letter in "Giraffe Academy":
    print(letter)

friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)

for index in range(len(friends)):
    print(friends[index])

for index in range(5, 10):
    print(index)

print("\n\n\n")
number_grid = [ #2D list
    [1, 2, 3],
    [4,5,6],
    [7,8,9],
    [0]
]
for row in number_grid:
    for col in row:
        print(col)
