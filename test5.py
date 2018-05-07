# 冒泡排序
def bubble_sort(s_list):
    for j in range(len(s_list) - 1, 0, -1):
        for i in range(j):
            if s_list[i] > s_list[i+1]:
                s_list[i], s_list[i+1] = s_list[i+1], s_list[i]


# 选择排序
def selection_sort(s_list):
    for i in range(len(s_list)):

        min_temp = i

        for j in range(i+1, len(s_list)):
            if s_list[min_temp] > s_list[j]:
                min_temp = j

        if min_temp != i:
            s_list[i], s_list[min_temp] = s_list[min_temp], s_list[i]


# 插入排序
def insertion_sort(s_list):
    for i in range(1, len(s_list)):
        for j in range(i, 0, -1):
            if s_list[j] < s_list[j-1]:
                s_list[j], s_list[j-1] = s_list[j-1], s_list[j]


def main():

    li = [12, 45, 89, 100, 980, 1, 3, 1, 67]

    insertion_sort(li)

    print(li)


if __name__ == '__main__':
    main()
