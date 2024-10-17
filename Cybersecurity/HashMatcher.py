import time
import string
import sys
import threading
import hashlib
import itertools
import os

# Global variable to control the stopping of the brute force process
stop_process = False
lock = threading.Lock()
num_cores = os.cpu_count()

# Data structure to store statistics
stats = {
    "algorithms_attempted": [],
    "total_attempts": 0,
    "thread_attempts": {},
    "start_time": None,
    "end_time": None
}

#Calculate the hash of a given text using a specified algorithm
def get_hash(text, algorithm):
    try:
        hash_func = getattr(hashlib, algorithm)
        hash_object = hash_func(text.encode())
        return hash_object.hexdigest()
    except AttributeError:
        return None

#Detect the possible hash algorithms based on the length of the hash value
def detect_hash_algorithm(hash_value):
    hash_length_to_algorithms = {
        32: ["md5"],
        40: ["sha1"],
        56: ["sha3_256"],
        64: ["sha256", "blake2s"],
        128: ["sha512","sha3_512", "blake2b"],
    }

    hash_length = len(hash_value)
    possible_algorithms = hash_length_to_algorithms.get(hash_length, None)

    if possible_algorithms:
        print(f"Possible algorithms for the given hash: {', '.join(possible_algorithms).upper()}\n")
        return possible_algorithms
    else:
        print("Unable to determine the algorithm error in hash length\n")
        return None

#Brute force attack to find the password that generates a given hash value
def brute_force(target_hash, charset, lower_range, upper_range, algorithm, thread_id, num_threads):
    global stop_process
    start_time = time.time()
    combinations_tried = 0

    for length in range(lower_range, upper_range + 1):
        for i, attempt in enumerate(itertools.product(charset, repeat=length)):
            if i % num_threads != thread_id:
                continue

            with lock:
                if stop_process:
                    elapsed_time = time.time() - start_time
                    stats["thread_attempts"][thread_id] = combinations_tried
                    return None, None, elapsed_time, combinations_tried

            password = ''.join(attempt)
            pass_hash = get_hash(password, algorithm)
            combinations_tried += 1

            # Print the current status
            with lock:
                print(f"Thread:{thread_id:<3}| Hash:{algorithm.upper()} | L:{length} | A:{combinations_tried} | {password}")
                sys.stdout.flush()

            if pass_hash == target_hash:
                with lock:
                    stop_process = True
                    stats["thread_attempts"][thread_id] = combinations_tried
                    print(f"\nPassword found: {password} \nHash: {pass_hash}\n")
                elapsed_time = time.time() - start_time
                return password, pass_hash, elapsed_time, combinations_tried

    elapsed_time = time.time() - start_time
    with lock:
        stats["thread_attempts"][thread_id] = combinations_tried
    return None, None, elapsed_time, combinations_tried

def listen_for_exit():
    global stop_process
    while True:
        user_input = input()
        if user_input.strip().lower() == "eq" or user_input.strip().lower() == "exit":
            with lock:
                stop_process = True
                stats["end_time"] = time.time()
            break

def print_brute_force_statistics(stats, total_time):
    print("\nBrute Force Statistics:")
    print(f"Total Time: {total_time:.2f} seconds")
    print(f"Total Attempts: {stats['total_attempts']}")
    print("Thread Attempts:")
    for thread_id, attempts in stats["thread_attempts"].items():
        print(f"  Thread {thread_id}: {attempts} attempts")
    print("Algorithms Attempted:")
    for algorithm in stats["algorithms_attempted"]:
        print(f"  {algorithm.upper()}")

def main():
    while True:
        global stop_process
        print("\nHash Matcher Program\n")

        # Ask for target hash
        target_hash = input("Enter the target hash value: ").strip()
        possible_algorithms = detect_hash_algorithm(target_hash)
        if not possible_algorithms:
            print("Invalid hash value exiting....")
            return

        print("Select the hashing algorithm option:")
        print("1. Select one suggested algorithm")
        print("2. Try all suggested algorithms")
        print("3. All  algorithms")
        print("4. Select a specific algorithm")

        choice = input("Enter your choice: ").strip()
        print()

        if choice == "1":
            print("Select the hashing algorithm:")
            for idx, algo in enumerate(possible_algorithms, start=1):
                print(f"{idx}. {algo.upper()}")
            algo_choice = input("Enter the number of the algorithm: ").strip()
            try:
                algorithm = possible_algorithms[int(algo_choice) - 1]
                algorithms = [algorithm]
                print(f"Selected algorithm: {algorithm.upper()}\n")
            except (IndexError, ValueError):
                print("Invalid choice exiting...\n")
                return
            
        elif choice == "2":
            algorithms = possible_algorithms
            print(f"Trying all suggested algorithms: {', '.join(algo.upper() for algo in algorithms)}\n")

        elif choice == "3":
            algorithms = ["md5", "sha1", "sha256", "sha512", "blake2b", "blake2s", "sha3_256", "sha3_512"]
            print("Trying all available algorithms.\n")

        elif choice == "4":
            print("Select the hashing algorithm:")
            print("1. MD5")
            print("2. SHA1")
            print("3. SHA256")
            print("4. SHA512")
            print("5. BLAKE2b")
            print("6. BLAKE2s")
            print("7. SHA3-256")
            print("8. SHA3-512")
            algo_choice = input("Enter the number of the algorithm: ").strip()
            algorithms_dict = {
                "1": "md5",
                "2": "sha1",
                "3": "sha256",
                "4": "sha512",
                "5": "blake2b",
                "6": "blake2s",
                "7": "sha3_256",
                "8": "sha3_512"
            }
            algorithm = algorithms_dict.get(algo_choice)
            if not algorithm:
                print("Invalid choice exiting...")
                return
            algorithms = [algorithm]
            print(f"Selected algorithm: {algorithm.upper()}\n")
        else:
            print("Invalid choice exiting...")
            return

        # Ask for password length
        length_input = input("Enter password length (leave blank if unknown): ").strip().lower()
        if length_input.isdigit():
            print(f"# Password length = {length_input} \n")
            max_length = int(length_input)
            min_length = max_length 
        else:
            print("# Assuming maximum length of 10 characters\n")
            max_length = 10
            min_length = 1

        # Ask for character set
        print("Character Set Menu:")
        print("0. All printable characters")
        print("1. Numbers")
        print("2. Lower case letters")
        print("3. Numbers & lower case letters")
        print("4. Upper case letters")
        print("5. Numbers & upper case letters")
        print("6. Lower & upper case letters")
        print("7. Numbers, lower & upper case letters")
    
        charset_choice = input("Select: ").strip()
        charsets = {
            "0": string.printable,
            "1": string.digits,
            "2": string.ascii_lowercase,
            "3": string.digits + string.ascii_lowercase,
            "4": string.ascii_uppercase,
            "5": string.digits + string.ascii_uppercase,
            "6": string.ascii_lowercase + string.ascii_uppercase,
            "7": string.digits + string.ascii_lowercase + string.ascii_uppercase
        }
        charset = charsets.get(charset_choice)
        print(f"#Charset: {charset}\n")
        if not charset:
            charset = string.printable
            print("Defaulting to all printable characters.")
            return

        print("Thread Menu:")
        print("0. Default  [4]")
        print("1. Single ")
        print("2. Med ium  [half of the cores]")
        print("3. Max  [all cores - 1]")
        print("4. Custom")

        thread_choice = input("Select: ").strip()
        thread_charsets = {
            "0": 4,
            "1":1,
            "2": num_cores // 2,
            "3": num_cores - 1,
            "4": None  # Placeholder for custom input
        }

        if thread_choice == "4":
            while True:
                try:
                    custom_thread_count = int(input("Custom thread count: ").strip())
                    if 0< custom_thread_count < num_cores:
                        thread_charsets["4"] = custom_thread_count
                        break
                    else:
                        print(f"Please enter a number greater than 0 and less than {num_cores}.")
                except ValueError:
                    print("Please enter a valid number.")

        num_threads = thread_charsets.get(thread_choice, 4)
        print(f"#Thread count: {num_threads}\n")
        threads = []

        # Start a thread to listen for the "eq" input
        listener_thread = threading.Thread(target=listen_for_exit)
        listener_thread.daemon = True
        listener_thread.start()

        stats["start_time"] = time.time()

        algorithm_known = choice == "1" or choice == "4"
        if algorithm_known:
            stats["algorithms_attempted"].append(algorithms[0])
            for i in range(num_threads):
                thread = threading.Thread(target=brute_force, args=(target_hash, charset, min_length, max_length, algorithms[0], i, num_threads))
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()

            stats["end_time"] = time.time()
            stats["total_attempts"] = sum(stats["thread_attempts"].values())

            if stop_process:
                print("Process stopped.")
            else:
                print("Password not found.")
        else:
            for algorithm in algorithms:
                if stop_process:
                    break
                print(f"Trying algorithm: {algorithm.upper()}")
                stats["algorithms_attempted"].append(algorithm)
                threads = []
                for i in range(num_threads):
                    thread = threading.Thread(target=brute_force, args=(target_hash, charset, min_length, max_length, algorithm, i, num_threads))
                    threads.append(thread)
                    thread.start()

                for thread in threads:
                    thread.join()

                stats["total_attempts"] = sum(stats["thread_attempts"].values())

                if stop_process:
                    print("Process stopped.")
                    break
                else:
                    print(f"Algorithm {algorithm.upper()} failed.")
            stats["end_time"] = time.time()

        total_time = stats["end_time"] - stats["start_time"] if stats["end_time"] else 0
        print_brute_force_statistics(stats, total_time)

if __name__ == "__main__":
    main()