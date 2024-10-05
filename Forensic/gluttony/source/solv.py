import os
import sys

def append_files(output_file):
    input_folder = "dump"

    if not os.path.exists(input_folder):
        print(f"Error: Folder '{input_folder}' not found.")
        sys.exit(1)

    files = sorted(os.listdir(input_folder))

    with open(output_file, 'wb') as outfile:
        for file in files:
            file_path = os.path.join(input_folder, file)

            if not file.endswith('.bin'):
                continue

            with open(file_path, 'rb') as infile:
                outfile.write(infile.read())

    print(f"Files successfully appended into '{output_file}'.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 solv.py <output_file>")
        sys.exit(1)
    
    output_file = sys.argv[1]

    append_files(output_file)
