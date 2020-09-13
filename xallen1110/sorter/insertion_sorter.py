from xallen1110.sorter.sorter import Sorter

class InsertionSorter(Sorter):
    def sort(self, input_list):
        for i in range(1, len(input_list)):
            current = input_list[i]
            if input_list[i - 1] <= current:
                continue

            for j in range(i, 0, -1):
                if input_list[j - 1] <= current:
                    break
                if input_list[j - 1] > current and j == 1:
                    j = 0

            for k in range(i, j, -1):
                input_list[k] = input_list[k - 1]
            input_list[j] = current 
