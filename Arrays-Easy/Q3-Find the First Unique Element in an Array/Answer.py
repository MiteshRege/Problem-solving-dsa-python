def answer(a):
    freq = {}
    for i in a:
        freq[i] = freq.get(i, 0) + 1

    # print(freq)
    # Not Recommended to traverse freq dict instead traverse array
    # from python 3.7+ dict preserve order of insertion still traverse array
    # kept below code jsut for ref (dont do that):
    # for k,v in freq.items():
    #     if v==1:
    #         print(f"answer : {k}")

    # Do this instead:
    for elem in a:
        if freq.get(elem) == 1:
            return elem
    return -1


if __name__ == "__main__":
    a1 = [2, 3, 2, 4, 3]
    a = [4, 5, 4, 6, 5, 7]

    print(f"First unique element is : {answer(a1)}")  # Output: 4
    print(f"First unique element is : {answer(a)}")  # Output: 6
