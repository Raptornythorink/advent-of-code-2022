class File:
    name = ""
    size = 0
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Directory:
    name = ""
    file_children = []
    dir_children = []
    path = ''
    size = 0
    def __init__(self, name, path, file_children, dir_children):
        self.name = name
        self.path = path
        self.file_children = file_children
        self.dir_children = dir_children
        for child in file_children:
            self.size += child.size
        for child in dir_children:
            child.path = self.path + "/" + child.name
    def add_file(self, file):
        for child in self.file_children:
            if child.name == file.name:
                return
        self.file_children.append(file)
        self.size += file.size
    def add_dir(self, dir):
        for child in self.dir_children:
            if child.name == dir.name:
                return
        dir.path = self.path + "/" + dir.name
        self.dir_children.append(dir)

def ls(a):
    a = input()
    while a and a[0] != '$':
        if a[0] == 'd':
            current.add_dir(Directory(a[4:], "", [], []))
        else:
            size, name = a.split()
            current.add_file(File(name, int(size)))
        a = input()
    return a

def find(dir, path):
    if dir.path == path:
        return dir
    for child in dir.dir_children:
        result = find(child, path)
        if result:
            return result
    return ""

def cd(a, current, root):
    if a[5] == "/":
        current = root
    elif a[5] == ".":
        current = find(root, current.path[:-len(current.name)-1])
    else:
        for child in current.dir_children:
            if child.name == a[5:]:
                current = child
                break
    a = input()
    return a, current

a = input()
root = Directory('/', '', [], [])
current = root
a = input()

while True:
    if not a:
        break
    if a[0] == "$":
        if a[2] == "c":
            a, current = cd(a, current, root)
        elif a[2] == "l":
            a = ls(a)

def update_sizes(dir):
    for child in dir.dir_children:
        update_sizes(child)
        dir.size += child.size

update_sizes(root)

space = max(0, root.size - 40000000)
min_size = root.size

def check_sizes(min_size, dir):
    if min_size >= dir.size >= space:
        min_size = dir.size
    for child in dir.dir_children:
        child_min_size = check_sizes(min_size, child)
        if min_size >= child_min_size >= space:
            min_size = child_min_size
    return min_size

print(check_sizes(min_size, root))