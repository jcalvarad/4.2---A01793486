"""This module ccounts the words from a list of words read from a file."""


import sys
import time

def read_words_from_file(filename):
    """Read words from a file, handling invalid data gracefully."""
    words = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                # Splitting by any whitespace and ignoring case by converting to lowercase
                words.extend(line.lower().strip().split())
    except Exception as e:
        print(f"Error reading file: {e}")
    return words

def count_words(words):
    """Count the frequency of each word in the list."""
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def write_results_to_file(filename, word_count, elapsed_time):
    """Write the word counts and time elapsed to a file."""
    with open(filename, 'w', encoding='utf-8') as file:
        for word, count in sorted(word_count.items(), key=lambda item: -item[1]):
            file.write(f"{word}: {count}\n")
        file.write(f"\nTime elapsed: {elapsed_time:.2f} seconds")

def main(filename):
    """Main function to read, count words, and output results."""
    start_time = time.time()
    words = read_words_from_file(filename)
    word_count = count_words(words)
    for word, count in sorted(word_count.items(), key=lambda item: -item[1]):
        print(f"{word}: {count}")
    elapsed_time = time.time() - start_time
    print(f"\nTime elapsed: {elapsed_time:.2f} seconds")
    write_results_to_file("WordCountResults.txt", word_count, elapsed_time)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        sys.exit(1)
    main(sys.argv[1])
