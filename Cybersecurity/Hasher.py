import hashlib

def get_hash(text, algorithm):
    try:
        hash_func = getattr(hashlib, algorithm)
        hash_object = hash_func(text.encode())
        return hash_object.hexdigest()
    except AttributeError:
        return f"Error: {algorithm} is not a supported hashing algorithm."

def main():
    while  True:
        print("Hashing Program")
        text = input("Enter the text to hash: ")
        print("Select the hashing algorithm:")
        print("1. MD5")
        print("2. SHA1")
        print("3. SHA256")
        print("4. SHA512")
        print("5. BLAKE2b")
        print("6. BLAKE2s")
        print("7. SHA3-256")
        print("8. SHA3-512")
        choice = input("Enter the number of the algorithm: ")

        algorithms = {
            "1": "md5",
            "2": "sha1",
            "3": "sha256",
            "4": "sha512",
            "5": "blake2b",
            "6": "blake2s",
            "7": "sha3_256",
            "8": "sha3_512"
        }

        algorithm = algorithms.get(choice)
        if algorithm:
            hash_value = get_hash(text, algorithm)
            print(f"The hash value using {algorithm.upper()} is: {hash_value}\n")
        else:
            print("Invalid choice. Please select a valid algorithm.")
            
if __name__ == "__main__":
    main()