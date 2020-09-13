from xallen1110.sorter.bubble_sorter import BubbleSorter
from xallen1110.sorter.insertion_sorter import InsertionSorter
from xallen1110.sorter.selection_sorter import SelectionSorter

if __name__ == '__main__':
    input_list = [14, 21, 3, 9, 15, 10, 15, 20, 6]
    expected_list = [3, 6, 9, 10, 14, 15, 15, 20, 21]

    list_for_bubble_sort = list(input_list)
    bubble_sorter = BubbleSorter()
    bubble_sorter.sort(list_for_bubble_sort)
    print("Result of Bubble Sort: " + str(list_for_bubble_sort))
    print("Is sorted result expected? " + str(expected_list == list_for_bubble_sort))

    list_for_selection_sort = list(input_list)
    selection_sorter = SelectionSorter()
    selection_sorter.sort(list_for_selection_sort)
    print("Result of Selection Sort: " + str(list_for_selection_sort))
    print("Is sorted result expected? " + str(expected_list == list_for_selection_sort))

    list_for_insertion_sort = list(input_list)
    insertion_sorter = InsertionSorter()
    insertion_sorter.sort(list_for_insertion_sort)
    print("Result of Insertion Sort: " + str(list_for_insertion_sort))
    print("Is sorted result expected? " + str(expected_list == list_for_insertion_sort))
