fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits,len(fruits),fruits[0],fruits[-1])

person = {"name": "Asha", "phone": "99999"}
person["email"] = "asha@example.com"
print(person["email"], person.get("age", "unknown"))