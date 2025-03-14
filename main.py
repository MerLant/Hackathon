import argparse
from pathlib import Path

# Определяем расширения файлов, которые считаем текстовыми
TEXT_EXTENSIONS = {'.js', '.ts', '.css', '.tsx'}

def main(directory: str, output_file: str):
    base_path = Path(directory).resolve()
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Рекурсивно проходим по всем файлам в директории и во всех дочерних папках
        for filepath in base_path.rglob('*'):
            if filepath.is_file() and filepath.suffix in TEXT_EXTENSIONS:
                try:
                    content = filepath.read_text(encoding='utf-8')
                except Exception as e:
                    print(f"Ошибка при чтении файла {filepath}: {e}")
                    continue
                # Вычисляем относительный путь файла относительно базовой директории
                relative_path = filepath.relative_to(base_path)
                # Записываем содержимое файла в md, выделяя его с помощью тройных обратных кавычек
                outfile.write(f"```{relative_path}\n")
                outfile.write(content)
                outfile.write("\n```\n\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Скрипт для объединения содержимого текстовых файлов (js, ts, css, tsx) в один Markdown файл, включая файлы из дочерних папок. Относительный путь файла указывается в блоке кода."
    )
    parser.add_argument("directory", help="Путь к базовой директории, где следует искать файлы")
    parser.add_argument("output_file", help="Путь к выходному Markdown файлу")
    args = parser.parse_args()
    main(args.directory, args.output_file)
