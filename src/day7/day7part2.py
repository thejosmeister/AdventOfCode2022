# Day 7 part 2
# Just faffing with basic arithmetic
from common.common import parse_input_into_list_of_strings, flatten_list
from anytree import Node, RenderTree, search

# created this to do the attributes, not sure if I needed it.
class Node2(Node, object):

    def __init__(self, name, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
        self.size = kwargs["size"]
        self.dir = kwargs["dir"]


commands = parse_input_into_list_of_strings("input.txt")

commands = commands[1:]
file_tree = {}

nodes = [ Node2("root", size=0, dir=True) ]

index = 0
current_node = nodes[0]


def create_tree():
    global index
    global current_node
    global nodes
    current = commands[index]


    if current[0] == '$':
        if current.split(' ')[1] == 'ls':
            i = 1
            while True:
                if index + i == len(commands):
                    break
                c = commands[index + i].split(' ')
                if c[0] == '$':
                    break
                if c[0] == 'dir':
                    if any(c[1] == e.name for e in current_node.children) is False:
                        nodes.append(Node2(c[1], parent=current_node, size=0, dir=True))
                else:
                    if any(c[1] == e.name for e in current_node.children) is False:
                        nodes.append(Node2(c[1], parent=current_node, size=int(c[0]), dir=False))

                i += 1

            index += i
        else:
            com = current.split(' ')

            index += 1
            if com[2] == '..':
                current_node = current_node.parent
            elif com[2] == '/':
                current_node = nodes[0]
            else:
                for x in current_node.children:
                    if x.name == com[2]:
                        current_node = x
                        break


while index < len(commands):
    create_tree()

dir_sizes = []

while any(e.size == 0 for e in nodes) is True:
    for node in nodes:
        if node.dir is True and node.size == 0:
            if any(e.size == 0 for e in node.children) is False:
                node.size = sum([n.size for n in node.children])

b = 70000000 - nodes[0].size

size_to_delete = 30000000 - b

min = min([n.size for n in list(filter(lambda x: (x.dir is True and x.size > size_to_delete), nodes))])

for x in nodes:
    if x.size == min:
        print(x)
        break

