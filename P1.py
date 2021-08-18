lst = [5, 10, 15, 20, 25, 50, 20]
lst_1 = lst.index(20)
lst.pop(lst_1)
lst.insert(lst_1, 200)
print(lst)
