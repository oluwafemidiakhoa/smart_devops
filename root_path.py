import os

class FileReader:
    def __init__(self, file_path):
        # Verify if the file exists before proceeding
        if not os.path.isfile(file_path):
            raise ValueError(f"The file path {file_path} does not exist.")

        self.file_path = file_path

    def read_file(self):
        """
        Function to read a file
        """
        try:
            with open(self.file_path, 'r') as file:
                print(file.read())
        except IOError as e:
            print(f"I/O error occurred: {str(e)}")
        except Exception as e:
            print(f"Unexpected error occurred: {str(e)}")

# Mocking the file system for testing
file_content = "This is a test file."
mock_file_path = "/mock/test/file.txt"

os.makedirs(os.path.dirname(mock_file_path), exist_ok=True)
with open(mock_file_path, 'w') as mock_file:
    mock_file.write(file_content)

reader = FileReader(mock_file_path)
reader.read_file()
