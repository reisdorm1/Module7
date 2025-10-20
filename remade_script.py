def main() -> None:
    """
    Demonstrate numeric and string processing functions using
    example input lists and print the results.
    """
    number_list = [1, 2, 3, 4, 5, 6, 7]
    fruit_list = ["apple", "banana", "kiwi", "grapefruit", "cherry"]

    processed_nums = process_numbers(number_list)
    processed_strings = transform_strings(fruit_list)

    # Join here for display (keeps transform_strings reusable)
    print("Processed Numbers:", processed_nums)
    print("Processed Strings:", " ".join(processed_strings))


if __name__ == "__main__":
    main()




if __name__ == "__main__":
main()
