import sys
import time

def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def mode(numbers):
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1
    max_frequency = max(frequency.values())
    modes = [number for number, freq in frequency.items() if freq == max_frequency]
    if len(modes) == len(numbers):
        return "No mode"
    return modes[0]

def variance(numbers):
    m = mean(numbers)
    return sum((x - m) ** 2 for x in numbers) / len(numbers)

def standard_deviation(numbers):
    return variance(numbers) ** 0.5

def read_numbers_from_file(filename):
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            try:
                number = float(line.strip())
                numbers.append(number)
            except ValueError:
                print(f"Skipping invalid data: {line.strip()}")
    return numbers

def write_results_to_file(filename, results):
    with open(filename, 'w') as file:
        for stat, value in results.items():
            file.write(f"{stat}: {value}\n")

def compute_statistics(filename):
    numbers = read_numbers_from_file(filename)
    if not numbers:
        print("No valid numbers were read from the file.")
        return

    results = {
        "Mean": mean(numbers),
        "Median": median(numbers),
        "Mode": mode(numbers),
        "Variance": variance(numbers),
        "Standard Deviation": standard_deviation(numbers)
    }

    return results

def main(filename):
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
