my_dict={"Katya": 1989, "Liza": 1996}
print(my_dict)
print(my_dict.get("Katya"))
print(my_dict.get("Vika"))
my_dict.update({"Alex": 1985,
                "Anna": 1989})
a=my_dict.pop("Katya")
print(a)
print(my_dict)
my_set={1,2,3,'Urban',True,35.5,1,2,3,35.5}
print(my_set)
my_set.update({4,5,"University"})
print(my_set.remove(35.5))
print(my_set)
