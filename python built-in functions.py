# some important built-in functions - pg 45 OOP Tutorials Point

x = ['Hi', 6, 7]
print(type(x))
print(len(x))

# enumerate () method adds a counter to an iterable and returns the enumerate object.

names = ['Rajesh', 'Rahul', 'Aarav', 'Sahil', 'Trevor']
print((enumerate(names)))
print(list(enumerate(names)))

# A better approach for enumerate() is keeping count within a for loop.
for i, n in enumerate(names):
    i += 1
    print('Names number: ' + str(i))
    print(n)

# reversed(seq) returns the reverse iterator

normal_list = [2, 4, 5, 7, 9]


class CustomSequence():
    def __len__(self):
        return 5

    def __getitem__(self, index):
        return "x{0}".format(index)


class FunkyBack():
    def __reversed__(self):
        return 'backwards!'


for seq in normal_list, CustomSequence(), FunkyBack():
    print('\n{}: '.format(seq.__class__.__name__), end="")  # the end=' ' is used to place a space after the displayed string instead of a newline.
    for item in reversed(seq):
        print(item, end=", ")
