from sort_algorithms_pkg.sorter import Sorter

class BubbleSorter(Sorter):

    def sort(self, input_list):
        for i in range(0, len(input_list) - 1):
            for j in range(len(input_list) - 1, i, -1):
                if input_list[j] < input_list[j - 1]:
                    input_list[j], input_list[j - 1] = input_list[j - 1], input_list[j]
