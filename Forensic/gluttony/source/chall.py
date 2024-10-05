import sys
import os

def split_file(input_file):
    # Create the "dump" folder if it doesn't exist
    output_folder = "dump"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the input file in binary mode
    with open(input_file, 'rb') as f:
        data = f.read()

    # Iterate over the file data in 128-bit (16-byte) chunks
    for i in range(0, len(data), 16):
        # Extract 16-byte chunk (128 bits)
        chunk = data[i:i+16]
        
        # Create a filename with 8-character zero-padded hex, starting from 1
        file_name = f"{i // 16 + 1:08x}.bin"

        # Write each chunk to a new file inside the "dump" folder
        with open(os.path.join(output_folder, file_name), 'wb') as chunk_file:
            chunk_file.write(chunk)

    print(f"File '{input_file}' split successfully into {len(data)//16} parts, saved in '{output_folder}'.")

if __name__ == "__main__":
    # Ensure the input file is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python3 split.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]

    # Check if the input file exists
    if not os.path.isfile(input_file):
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    # Split the file
    split_file(input_file)
