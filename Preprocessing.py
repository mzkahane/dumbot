import sys
import os
import re

# Function to clean and format a single conversation entry
def format_conversation_entry(entry):
    parts = entry.split(': ', 1)
    if len(parts) == 2:
        speaker, dialogue = parts
        dialogue = dialogue.strip().replace('\\n', '<NEWLINE>')
        return f"{speaker}: {dialogue}"
    return ""

# Function to process a single file
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    entries = re.split(r'\t|\n', text)
    return '\n'.join(filter(None, [format_conversation_entry(entry) for entry in entries]))

# Function to process all files in a directory and append them into one formatted file
def process_directory(directory_path, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        # Iterate over all files in the given directory
        for filename in os.listdir(directory_path):
            if filename.endswith('.txt'):
                file_path = os.path.join(directory_path, filename)
                formatted_text = process_file(file_path)
                output_file.write(formatted_text + '\n\n')

if __name__ == "__main__":
    # Improper usage
    if len(sys.argv) != 3:
        print("Usage: python3 Preprocessing.py <directory path> <output filename>")
        exit(-1)

    # Pass the directory path and output CSV file name as command-line arguments
    directory_path = sys.argv[1]
    output_file_name = sys.argv[2]
    process_directory(directory_path, output_file_name)
