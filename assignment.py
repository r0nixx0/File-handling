# You can remove 'pass' if you written code in the function
# Exercise 1
def write_shopping_list(items, filename):
    file=open(filename,"w")
    c=1
    for i in items:
        file.write(f"{c}.{i}\n")
        c=c+1
    file.close()
    pass

# Exercise 2
def read_names(filename):
    file=open(filename,"r")
    lst=[]
    lines=file.readlines()
    for line in lines:
        if line.strip()!="":
            lst.append(line.strip())
    file.close()
    return lst

    pass

# Exercise 3
def append_entry(filename, text):
    file=open(filename,"a")
    file.write(text+"\n")
    file.close()
    pass


# Exercise 4
def search_file(filename, word):
    file=open(filename,"r")
    lst=[]
    c=0
    for line in file:
        c=c+1
        line.lower()
        if word in line:
            lst.append(c)
    file.close()
    return lst
    pass

# Exercise 5
def number_the_lines(source, destination):
    file = open(source, "r")
    lines = file.readlines()
    file.close()
    file=open(destination,'w')
    c=1
    for line in lines:
        file.write(f"{c}: {line}")
        c=c+1
    file.close()
    return c-1
    pass
source="Test.txt"
destination="shopping.txt"

print(number_the_lines(source,destination))



