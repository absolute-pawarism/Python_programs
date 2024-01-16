import bisect

def binary_search(word_list, target):
    sorted_word_list = sorted(word_list)
    left, right = 0, len(sorted_word_list)

    while left < right:
        mid = (left + right) // 2
        mid_word = sorted_word_list[mid]

        if mid_word == target:
            return True
        elif mid_word < target:
            left = mid + 1
        else:
            right = mid

    return False

def bisect_main():
    word_list = input("Enter the word list: ").split(' ')
    word_list = [word.strip() for word in word_list]
    word = input("Enter the word to search: ")
    result = binary_search(word_list, word)

    if result:
        print(f"The word '{word}' is present in the word list.")
    else:
        print(f"The word '{word}' is not present in the word list.")

if __name__ == "__main__":
    bisect_main()
