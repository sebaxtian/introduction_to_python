import some_module

print(f'This is a message from {__name__}.')
# Call func() from the imported module
some_module.func()

# Make a change here (add a main block)
if __name__ == "__main__":
    print('This should be printed ONLY when task.py is called directly.')

