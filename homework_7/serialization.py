import os
import json, csv, pickle


# ----------------------------------------------------------------------------------------------------------------------

# 1. Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# 1. Для дочерних объектов указывайте родительскую директорию;
# 2. Для каждого объекта укажите файл это или директория;
# 3. Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов
# и директорий.

# ----------------------------------------------------------------------------------------------------------------------

def directory_bypass(directory_path):
    result = {}

    for root, dirs, files in os.walk(directory_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_info = {
                'type': 'file',
                'parent_directory': root,
                'size': os.path.getsize(file_path)
            }
            result[file_path] = file_info

        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            dir_size = sum(
                os.path.getsize(os.path.join(dir_path, file)) for file in os.listdir(dir_path) if
                os.path.isfile(os.path.join(dir_path, file)))
            dir_info = {
                'type': 'directory',
                'parent_directory': root,
                'size': dir_size
            }
            result[dir_path] = dir_info
    return result


def save_to_json(directory_path, output_file):
    directory_info = directory_bypass(directory_path)
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(directory_info, json_file, indent=4, ensure_ascii=False)


def save_to_csv(directory_path, output_file):
    directory_info = directory_bypass(directory_path)
    with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['path', 'type', 'parent_directory', 'size']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for path, info in directory_info.items():
            row = {'path': path, **info}
            writer.writerow(row)


def save_to_pickle(directory_path, output_file):
    directory_info = directory_bypass(directory_path)
    with open(output_file, 'wb') as pickle_file:
        pickle.dump(directory_info, pickle_file)


if __name__ == "__main__":
    directory_path = 'D:\\PycharmProjects'

    save_to_json(directory_path, 'result.json')
    save_to_csv(directory_path, 'result.csv')
    save_to_pickle(directory_path, 'result.pkl')
# ----------------------------------------------------------------------------------------------------------------------

# 2. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.

# ----------------------------------------------------------------------------------------------------------------------
