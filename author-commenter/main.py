import os

def add_author_comments(directory_path, author_info):
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith('.java'):
                file_path = os.path.join(root, file_name)
                add_author_comment_to_file(file_path, author_info)

def add_author_comment_to_file(file_path, author_info):
    author_comment = f'''
/*
 * @Author: {author_info['name']}
 * @Email: {author_info['email']}
 * @Year: {author_info['date']}
 *
 * @Project: {author_info['project']}
 */

'''

    with open(file_path, 'r+') as file:
        content = file.read()
        file.seek(0, 0)
        file.write(author_comment + content)

if __name__ == "__main__":
    directory_path = input("Enter the directory path: ")
    author_name = input("Enter author's name: ")
    author_email = input("Enter author's email: ")
    project_date = input("Enter project date: ")
    project_name = input("Enter project name: ")

    author_info = {
        "name": author_name,
        "email": author_email,
        "date": project_date,
        "project": project_name,
    }

    add_author_comments(directory_path, author_info)
    print("Author comments added successfully.")
