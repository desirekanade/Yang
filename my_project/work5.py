import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start time
        result = func(*args, **kwargs)  # Call the decorated function
        end_time = time.time()  # Record end time
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper


@timing_decorator
def add_numbers(a, b):
    result = a + b
    print(f"Sum: {result}")
    return result


@timing_decorator
def read_and_write_numbers(input_file, output_file):
    with open(input_file, 'r') as file:
        a, b = map(int, file.readline().split())
    result = a + b
    with open(output_file, 'w') as file:
        file.write(f"Sum: {result}\n")
    print(f"Result written to {output_file}")

# Example usage
add_numbers(3, 5)


with open('input.txt', 'w') as file:
    file.write("4 6\n")

read_and_write_numbers('input.txt', 'output.txt')
