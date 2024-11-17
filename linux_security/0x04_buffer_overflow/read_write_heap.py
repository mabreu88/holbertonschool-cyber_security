#!/usr/bin/python3

"""
read_write_heap.py - Script to search and replace a string in the heap of a running process.

Usage:
    python3 read_write_heap.py pid search_string replace_string

Arguments:
    pid - Process ID of the target process
    search_string - ASCII string to search for in the heap
    replace_string - ASCII string to replace the search_string
"""

import sys

def usage():
    """
    Prints the usage instructions for the script.
    
    Usage:
        python3 read_write_heap.py pid search_string replace_string
    
    Arguments:
        pid - Process ID of the target process
        search_string - ASCII string to search for in the heap
        replace_string - ASCII string to replace the search_string
    """
    print("Usage: read_write_heap.py pid search_string replace_string")
    sys.exit(1)

def main():
    """
    Main function to search and replace a string in the heap of a running process.
    
    Parses arguments, opens the process's memory and mappings, and performs the
    replacement if the target string is found in the heap segment.
    """
    if len(sys.argv) != 4:
        usage()

    pid = int(sys.argv[1])
    search_string = sys.argv[2].encode()
    replace_string = sys.argv[3].encode()

    if len(replace_string) < len(search_string):
        replace_string += b'\x00' * (len(search_string) - len(replace_string))

    mem_route = f"/proc/{pid}/mem"
    map_route = f"/proc/{pid}/maps"

    try:
        with open(map_route, 'r') as maps_file:
            for line in maps_file:
                parts = line.split()
                start = int(parts[0].split('-')[0], 16)
                end = int(parts[0].split('-')[1], 16)
                permissions = parts[1]

                if 'heap' in line and 'rw-p' in permissions:
                    with open(mem_route, 'r+b') as mem_file:
                        chunk_size = 4096
                        while start < end:
                            size_to_read = min(chunk_size, end - start)
                            mem_file.seek(start)
                            data = mem_file.read(size_to_read)

                            index = data.find(search_string)
                            if index != -1:
                                mem_file.seek(start + index)
                                mem_file.write(data[:index] + replace_string + data[index + len(search_string):])
                                print(f"Replaced '{search_string.decode()}' with '{replace_string.decode()}'")
                                return
                            start += chunk_size

        print("Error: String not found in heap")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
