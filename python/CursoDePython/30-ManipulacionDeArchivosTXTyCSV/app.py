from file_manager import FileManager

file_manager = FileManager()
file_manager.read_line_by_line()
file_manager.read_all_lines()

file_manager.add_line("Hello World!, I'm learning Python")
file_manager.read_all_lines()
print(file_manager)

#file_manager.overwrite_file('Sobreescribiendo el archivo de nuevo')
#file_manager.read_all_lines()
print(file_manager.get_count_lines())
