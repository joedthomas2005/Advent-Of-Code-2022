class File:
    def __init__(self, parent, name: str, size: int, isdir: bool):
        self.parent = parent
        self.name = name
        self.size = size
        self.isdir = isdir
        self.children = []
    def addchild(c):
        self.children.append(n)

def dirsizes(r: File):
    sizes = []
    sizes.append((r.name, dirsize(r)))
    for c in r.children:
        if c.isdir:
            for s in dirsizes(c):
                sizes.append(s)
    return sizes

def dirsize(r: File):
    size = 0
    for c in r.children:
        if c.isdir:
            size += dirsize(c)
        else:
            size += c.size
    return size

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

unused = 70000000-dirsize(root)
tofree = 30000000-unused
candidates = dirsizes(root)
best = candidates[0]
for candidate in dirsizes(root):
    if candidate[1] >= tofree and candidate[1] < best[1]:
        best = candidate

print(best)
