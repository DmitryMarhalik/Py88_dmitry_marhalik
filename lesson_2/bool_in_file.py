myfile = open("bool.txt", "w")
x = input()
print(bool(x), file=myfile)
myfile.close()
