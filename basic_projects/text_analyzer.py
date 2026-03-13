# Text Analyzer
# Analyze text statistics, repeated words, and keyword usage

import string

current_text = ""


def get_clean_words(text):
    words = []
    for word in text.split():
        cleaned = word.strip(string.punctuation).lower()
        if cleaned:
            words.append(cleaned)
    return words


def enter_text():
    global current_text
    current_text = input("Enter your text: ").strip()
    if not current_text:
        print("No text entered!")
        return
    print("\nText saved for analysis.")


def show_analysis():
    if not current_text:
        print("\nPlease enter text first!")
        return

    words = get_clean_words(current_text)
    characters = len(current_text)
    characters_no_spaces = len(current_text.replace(" ", ""))
    word_count = len(words)
    sentence_count = sum(current_text.count(mark) for mark in ".!?")
    if sentence_count == 0:
        sentence_count = 1 if current_text else 0
    vowels = sum(1 for char in current_text.lower() if char in "aeiou")
    unique_words = len(set(words))
    average_word_length = sum(len(word) for word in words) / word_count if word_count else 0

    print("\nText Analysis")
    print("-" * 30)
    print(f"Characters:           {characters}")
    print(f"Characters(no space): {characters_no_spaces}")
    print(f"Words:                {word_count}")
    print(f"Sentences:            {sentence_count}")
    print(f"Vowels:               {vowels}")
    print(f"Unique words:         {unique_words}")
    print(f"Average word length:  {average_word_length:.2f}")


def show_word_frequency():
    if not current_text:
        print("\nPlease enter text first!")
        return

    words = get_clean_words(current_text)
    if not words:
        print("\nNo valid words found!")
        return

    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    sorted_words = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

    print("\nTop Word Frequency")
    print("-" * 25)
    for index, (word, count) in enumerate(sorted_words[:10], 1):
        print(f"{index}. {word} - {count}")


def search_word():
    if not current_text:
        print("\nPlease enter text first!")
        return

    keyword = input("Enter a word to search: ").strip().lower()
    if not keyword:
        print("Please enter a word!")
        return

    words = get_clean_words(current_text)
    matches = words.count(keyword)

    if matches == 0:
        print(f"\n'{keyword}' was not found.")
    else:
        print(f"\n'{keyword}' appears {matches} time(s).")


def main():
    print("=" * 40)
    print("         TEXT ANALYZER")
    print("=" * 40)

    while True:
        print("\n1. Enter Text")
        print("2. Show Analysis")
        print("3. Show Word Frequency")
        print("4. Search Word")
        print("5. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            enter_text()
        elif choice == "2":
            show_analysis()
        elif choice == "3":
            show_word_frequency()
        elif choice == "4":
            search_word()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()