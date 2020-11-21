lucky_numbers = [4,8,15,16,23,42]
friends = ["Kevin", 2, False, 2]
friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1, "Kelly")
friends.remove("Kevin")  #friends.sort() doesn't work on python3
print(friends.count(2))
print(friends)
friends.reverse()
print(friends)