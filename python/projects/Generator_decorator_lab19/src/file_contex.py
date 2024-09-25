#import pdb; 
#pdb.set_trace()

class FileContextManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'r')
        #pdb.set_trace()      
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            self.file.close()
        finally:
            print('File closed')

with FileContextManager('sample.txt') as file:
    try:
        print(file.read())
    except FileNotFoundError as e:
        # Handle the case where the file does not exist
        print(f"Error: {e}")
    except Exception as e:
        # Handle any other exception
        print(f"An unexpected error occurred: {e}")
        raise Exception('An error occurred')
# OR

#with open('sample.txt', 'r') as file:
#    print(file.read())

# OR

"""
# Create an instance of the FileContextManager
file_context = FileContextManager('sample.txt')
# Manually call __enter__ to open the file
file = file_context.__enter__()
try:
    # Read and print the contents of the file
    print(file.read())
finally:
    # Ensure __exit__ is called to close the file
    file_context.__exit__(None, None, None)
"""