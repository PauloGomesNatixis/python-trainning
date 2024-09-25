class ContextManager:
    def __enter__(self):
        print('Entering the context')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f'An exception occurred: {exc_value}')
        else:
            print('No exception occurred')
        print('Exiting the context')

with ContextManager() as cm:
    print('Inside the context')
    raise Exception('An error occurred')
    
    
