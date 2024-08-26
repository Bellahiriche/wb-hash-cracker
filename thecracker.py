import hashlib
import sys
import pyfiglet

def display_banner(text):
    """Displays an ASCII banner using the provided text."""
    print(pyfiglet.figlet_format(text))

def get_user_input(prompt):
    """Prompts the user for input and returns the stripped input."""
    return input(prompt).strip()

def read_file_with_encoding(file_path):
    """Attempts to read a file with different encodings."""
    encodings = ['utf-8', 'latin1', 'ascii']
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                return file.read()
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError("Failed to decode file with any known encodings.")

def hash_word(word, hash_type):
    """Returns the hash of the word using the specified hash algorithm."""
    try:
        hash_func = hashlib.new(hash_type)
    except ValueError:
        sys.exit('Invalid or unsupported hash algorithm specified.')

    hash_func.update(word.encode('utf-8'))
    return hash_func.hexdigest()

def main():
    display_banner("The Cracker")

    # List available hash algorithms
    available_algorithms = sorted(hashlib.algorithms_available)
    print('Available Algorithms:', ' | '.join(available_algorithms))

    hash_type = get_user_input('Enter the hash algorithm: ').lower()
    wordlist_location = get_user_input('Enter the wordlist location: ')
    hash_value = get_user_input('Enter the hash: ')

    try:
        word_list = read_file_with_encoding(wordlist_location)
    except FileNotFoundError:
        sys.exit(f"Error: File '{wordlist_location}' not found.")
    except UnicodeDecodeError:
        sys.exit("Error: Failed to decode the file with available encodings.")
    except Exception as e:
        sys.exit(f"An unexpected error occurred: {e}")

    for word in word_list.splitlines():
        if hash_value == hash_word(word, hash_type):
            print(f"Hash Found: {word}")
            break
    else:
        print('Hash not found in the provided wordlist.')

if __name__ == "__main__":
    main()
