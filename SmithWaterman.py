def get_file_data(prompt):
    filename = input(prompt)
    file = open(filename, 'r')
    return file.read()

get_file_data("Enter first file name: ")
get_file_data("Enter second file name: ")


