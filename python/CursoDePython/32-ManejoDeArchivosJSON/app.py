from json_file_manager import JsonFileManager

json_manager = JsonFileManager()
options = [
    {'id': 1, 'option': 'Show all file content', 'method': 'show_all_file_content'},
    {'id': 2, 'option': 'Show all file content (Main fields)', 'method': 'show_all_file_content_main_fields'},
    {'id': 3, 'option': 'Add new Product', 'method': 'add_new_product'},
    {'id': 0, 'option': 'Exit'}
]

while True:
    print("Chose a option: ")
    for option in options:
        print(f"{option['id']}. {option['option']}")

    selected_option = int(input("Selected option: "))

    if selected_option == 0:
        print("Good Bye...")
        break
    for option in options:
        if option['id'] == selected_option:
            print(f"Selected option: {option['option']}")
            if 'method' in option:
                method = getattr(json_manager, option['method'])
                method()
            else:
                print("Method not found...")
    input("Press ENTER to continue...")
