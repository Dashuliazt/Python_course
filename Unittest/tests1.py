import random

#
# class SortAlgorithms:

    # def bubble_sort(self, iteration):
    #
    #     if not isinstance(iteration, list):
    #         raise TypeError('object must be a list')
    #
    #     elif not all(list(map(lambda x: isinstance(x,int), iteration))):
    #         raise TypeError('object must only be digits')
    #
    #     for i in range(len(iteration)):
    #         for j in range(len(iteration)-1-i):
    #             if iteration[j] > iteration[j+1]:
    #                 iteration[j], iteration[j+1] = iteration[j+1], iteration[j]
    #     return iteration


 def bubble_sort(iteration):
    """
    >>> bubble_sort([2, 1, 5, -1])
    [-1, 1, 2, 5]
    >>> bubble_sort([-2, 1, 5, -1])
    [-2, -1, 1, 5]
    """
    if not isinstance(iteration, list):
        raise TypeError('object must be a list')
    elif not all(list(map(lambda x: isinstance(x,int), iteration))):
        raise TypeError('object must only be digits')
    for i in range(len(iteration)):
        for j in range(len(iteration)-1-i):
            if iteration[j] > iteration[j+1]:
                iteration[j], iteration[j+1] = iteration[j+1], iteration[j]
        return iteration

# тест с помощью assert
# random_list = random.sample(range(100), 10)
# assert bubble_sort(random_list.copy()) == sorted(random_list.copy()), \
#     'bubble_sort !=sorted'
