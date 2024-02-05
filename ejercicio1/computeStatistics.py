"""This module computes descriptive statistics from a list of numbers read from a file."""

import sys
import time

def mean(numbers):
    """Calculate the mean of a list of numbers."""
    return sum(numbers) / len(numbers)

def median(numbers):
    """Calculate the median of a list of numbers."""
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    return sorted_numbers[mid]  # Simplified control flow

def mode(numbers):
    """Calculate the mode of a list of numbers."""
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1
    max_frequency = max(frequency.values())
    modes = [number for number, freq in frequency.items() if freq == max_frequency]
    if len(modes) == len(numbers):
        return "No mode"
    return modes[0]

def variance(numbers):
    """Calculate the variance of a list of numbers."""
    m = mean(numbers)
    return sum((x - m) ** 2 for x in numbers) / len(numbers)

def standard_deviation(numbers):
    """Calculate the standard deviation of a list of numbers."""
    return variance(numbers) ** 0.5

def read_numbers_from_file(filename):
    """Read numbers from a file, skipping over invalid data."""
    numbers = []
    with open(filename, 'r', encoding='utf-8') as file:  # Specified encoding
        for line in file:
            try:
                number = float(line.strip())
                numbers.append(number)
            except ValueError:
                print(f"Skipping invalid data: {line.strip()}")
    return numbers

def write_results_to_file(filename, results):
    """Write the calculated statistics to a file."""
    with open(filename, 'w', encoding='utf-8') as file:  # Specified encoding
        for stat, value in results.items():
            file.write(f"{stat}: {value}\n")

def compute_statistics(filename):
    """Compute and return descriptive statistics for a list of numbers."""
    numbers = read_numbers_from_file(filename)
    if not numbers:
        print("No valid numbers were read from the file.")
        return {}

    results = {
        "Mean": mean(numbers),
        "Median": median(numbers),
        "Mode": mode(numbers),
        "Variance": variance(numbers),
        "Standard Deviation": standard_deviation(numbers)
    }

    return results

def main(filename):
    """Main function to compute statistics from a file and output results."""
    start_time = time.time()
    results = compute_statistics(filename)
    if results:
        elapsed_time = time.time() - start_time
        results["Time elapsed"] = f"{elapsed_time} seconds"
        for stat, value in results.items():
            print(f"{stat}: {value}")
        write_results_to_file("StatisticsResults.txt", results)

if len(sys.argv) != 2:
    print("Usage: python computeStatistics.py fileWithData.txt")
    sys.exit(1)
else:
    main(sys.argv[1])
