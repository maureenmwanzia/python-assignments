def modify_content(text):
    """
    Modify the content of the file.
    For demo: convert all text to uppercase.
    """
    return text.upper()


def main():
    # Ask user for filename
    filename = input("Enter the filename to read: ")

    try:
        # Try opening and reading the file
        with open(filename, "r") as infile:
            content = infile.read()

        # Modify the content
        modified = modify_content(content)

        # Write modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as outfile:
            outfile.write(modified)

        print(f"✅ Modified content has been written to {new_filename}")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# Run the program
if __name__ == "__main__":
    main()
