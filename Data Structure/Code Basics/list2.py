heros=['spider man','thor','hulk','iron man','captain america']
print("Length of the list {}".format(len(heros)))
heros.append("black panther")
print(heros)
heros.remove("black panther")
print(heros)
heros.insert(3, "black panther")
print(heros)
del heros[1:3]
print(heros)
heros.insert(1, "doctor strange")
print(heros)
heros.sort()
print(heros)