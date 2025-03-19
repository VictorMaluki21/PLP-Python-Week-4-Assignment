# Python program to read a file, modify its content, and write to a new file
# Includes error handling for missing or unreadable files

def read_and_write_files():
    try:
        # Ask the user for the input filename
        input_filename = input("Enter the name of the file to read: ")
        
        # Open the input file for reading
        with open(input_filename, 'r') as infile:
            # Read the content of the file
            content = infile.readlines()
        
        # Modify the content (example: adding line numbers)
        modified_content = [f"{i + 1}: {line}" for i, line in enumerate(content)]
        
        # Ask the user for the output filename
        output_filename = input("Enter the name of the new file to write to: ")
        
        # Open the output file for writing
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)
        
        print(f"Modified content written to '{output_filename}' successfully.")
    
    except FileNotFoundError:
        print("Error: The specified file does not exist.")
    except IOError:
        print("Error: The file cannot be read or written.")

# Run the function
read_and_write_files()
