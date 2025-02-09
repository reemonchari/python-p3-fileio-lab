def write_file(file_name, file_content):
    text_file = open(f"{file_name}.txt", mode = "w")
    text_file.write(file_content)
    text_file.close()

def append_file(file_name, append_content):
    text_file = open(f"{file_name}.txt", mode = "a")
    text_file.write(append_content)
    text_file.close()

def read_file(file_name):
    with open(f"{file_name}.txt", mode = "r") as text_file:
        return text_file.read()