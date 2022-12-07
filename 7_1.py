class File:
    def __init__(self, parent, name: str, size: int, isdir: bool):
        self.parent = parent
        self.name = name
        self.size = size
        self.isdir = isdir
        self.children = []
    def addchild(c):
        self.children.append(n)

def dirsize(r: File):
    size = 0
    for c in r.children:
        if c.isdir:
            size += dirsize(c)
        else:
            size += c.size
    return size

def getdeletable(r: File):
    deletable = 0
    if dirsize(r) <= 100000:
        deletable += dirsize(r)

    for c in r.children:
        if c.isdir:
            deletable += getdeletable(c)

    return deletable 
    
with open("input.txt", "r") as f:
    cmds = f.read().split('\n')[1:-1]
root = File(None, '/', 0, True)
curdir = root
for cmd in cmds:
    if 'cd' in cmd.split(' '):
        arg = cmd.split(' ')[2]
        if arg == "..":
            curdir = curdir.parent
        else:
            new = File(curdir, cmd.split(' ')[2], 0, True)
            curdir.children.append(new)
            curdir = new
    elif cmd.split(' ')[0] != "$":
        if cmd.split(' ')[0] == "dir":
            curdir.children.append(File(curdir, cmd.split(' ')[1], 0, True))
        else:
            curdir.children.append(File(curdir, cmd.split(' ')[1], int(cmd.split(' ')[0]), False))

print(getdeletable(root))
