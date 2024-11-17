#!/usr/bin/python3

import sys
import os

# Function to display usage instructions
def usage():
    """
    Prints the correct usage of the script and exits the program.

    Usage: read_write_heap.py pid search_string replace_string
    - pid: Process ID of the target process
    - search_string: The string to search for in the heap memory
    - replace_string: The string to replace the search_string with
    """
    print("Usage: read_write_heap.py pid search_string replace_string")
    sys.exit(1)

# Main function to perform the heap memory search and replacement
def main():
    # Validate the number of arguments
    if len(sys.argv) != 4:
        usage()

    # Parse command-line arguments
    pid = int(sys.argv[1])  # Target process ID
    search_string = sys.argv[2].encode()  # String to search for (encoded to bytes)
    replace_string = sys.argv[3].encode()  # Replacement string (encoded to bytes)

    # Paths to the process's memory and memory mappings
    mem_route = f"/proc/{pid}/mem"
    map_route = f"/proc/{pid}/maps"

    try:
        # Open the memory mappings file for the target process
        with open(map_route, 'r') as maps_file:
            for line in maps_file:
                # Parse each line to extract memory region information
                parts = line.split()
                start = int(parts[0].split('-')[0], 16)  # Start address of the memory region
                end = int(parts[0].split('-')[1], 16)  # End address of the memory region
                permissions = parts[1]  # Permissions of the memory region

                # Check if the current memory region is the heap and writable
                if 'heap' in line and 'rw-p' in permissions:
                    # Open the memory file for the target process in read/write mode
                    with open(mem_route, 'r+b') as mem_file:
                        # Read data from the heap memory
                        mem_file.seek(start)
                        data = mem_file.read(end - start)

                        # Search for the specified string in the memory data
                        index = data.find(search_string)
                        if index != -1:
                            # Replace the string if found
                            new_data = (
                                data[:index] +
                                replace_string +
                                data[index + len(search_string):]
                            )
                            # Write the modified data back to memory
                            mem_file.seek(start)
                            mem_file.write(new_data)
                            print(f"Replaced '{search_string.decode()}' with '{replace_string.decode()}'")
                            sys.exit(0)

        # If the string is not found in the heap
        print("Error: String not found in heap")
    except Exception as e:
        # Handle any errors that occur during the process
        print(f"Error: {e}")
        sys.exit(1)

# Entry point of the script
if __name__ == "__main__":
    main()
