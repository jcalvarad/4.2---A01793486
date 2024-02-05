import sys
import time

def read_numbers_from_file(filename):
    """Read numbers from a file, handling invalid data gracefully."""
    numbers = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                numbers.append(int(line.strip()))
            except ValueError as e:
                print(f"Error converting to number: {line.strip()} ({e})")
    return numbers

def to_binary(number):
    """Convert a number to its binary representation using basic algorithms."""
    if number == 0:
        return '0'
    binary = ''
    while number > 0:
        binary = str(number % 2) + binary
        number //= 2
    return binary

def to_hexadecimal(number):
    """Convert a number to its hexadecimal representation using basic algorithms."""
    if number == 0:
        return '0'
    hex_chars = '0123456789ABCDEF'
    hexadecimal = ''
    while number > 0:
        hexadecimal = hex_chars[number % 16] + hexadecimal
        number //= 16
    return hexadecimal

def convert_numbers(numbers):
    """Convert a list of numbers to binary and hexadecimal, returning the results."""
    results = []
    for number in numbers:
        binary = to_binary(number)
        hexadecimal = to_hexadecimal(number)
        results.append((number, binary, hexadecimal))
    return results

def write_results_to_file(filename, results, elapsed_time):
    """Write the conversion results and time elapsed to a file."""
    with open(filename, 'w', encoding='utf-8') as file:
        for number, binary, hexadecimal in results:
            file.write(f"{number}: Binary = {binary}, Hexadecimal = {hexadecimal}\n")
        file.write(f"Time elapsed: {elapsed_time} seconds\n")

def main(filename):
    """Main function that orchestrates the reading, conversion, and output."""
    start_time = time.time()
    numbers = read_numbers_from_file(filename)
    results = convert_numbers(numbers)
    for number, binary, hexadecimal in results:
        print(f"{number}: Binary = {binary}, Hexadecimal = {hexadecimal}")
    elapsed_time = time.time() - start_time
    print(f"Time elapsed: {elapsed_time:.2f} seconds")
    write_results_to_file("ConversionResults.txt", results, elapsed_time)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        sys.exit(1)
    main(sys.argv[1])
