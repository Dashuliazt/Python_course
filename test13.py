import os


# def file_check(filename):
#     if os.path.isfile(filename):
#         print(filename + ' is file')
#     elif os.path.isdir(filename):
#         print(filename + ' is dir')
#
#
# file_check('vene')

#task 2

# def sizefile(filename):
#     print(os.path.getsize(filename))
#
# sizefile('test12.py')

#task 3



#task 9
def tree(path):
    if os.path.isdir(path):
        for el in os.listdir(path):
            way = os.path.join(path,el)
            print(way)
            if os.path.isfile(way):
                continue
            elif os.path.isdir(way):
                tree(way)
    else:
        print(f'{path} is not directory.')


tree('Задание')