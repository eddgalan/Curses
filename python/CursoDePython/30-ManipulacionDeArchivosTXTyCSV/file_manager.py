class FileManager:
    def __init__(self, file_name = 'file.txt'):
        self.file_name = file_name

    def __str__(self):
        return f'File name: {self.file_name}'

    def read_line_by_line(self):
        print("Leer línea por línea")
        with open(self.file_name, 'r') as file:
            for line in file:
                print(line.strip())
        print("\n")

    def read_all_lines(self):
        with open(self.file_name, 'r') as file:
            lines = file.readlines()
            print(lines)
        print("\n")

    def add_line(self, line):
        with open(self.file_name, 'a') as file:
            file.write("\n" + line)
            print(file.closed)

    def overwrite_file(self, line):
        with open(self.file_name, 'w') as file:
            file.write(line)
            print(file.closed)

    def get_count_lines(self):
        with open(self.file_name, 'r') as file:
            lines = file.readlines()
            return len(lines)
