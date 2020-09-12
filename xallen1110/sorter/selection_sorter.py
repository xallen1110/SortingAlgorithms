from xallen1110.sorter.sorter import Sorter

class SelectionSorter(Sorter):

    def sort(self, input_list):
        for i in range(0, len(input_list)):
            base, position = input_list[i], i
            for j in range(i + 1, len(input_list)):
                if input_list[j] >= base:
                    continue
                base, position = input_list[j], j
            input_list[i], input_list[position] = input_list[position], input_list[i]
