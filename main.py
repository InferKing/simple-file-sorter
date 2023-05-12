import os
import dictpy


class FileSorter:
    """
        If you want to create other folders with specific extensions, then:
        1. Add a key to the list below (this is what the folder name will look like)
        2. The values for the key will be the extensions you want to sort.
    """
    exts = {
        "Images": ["png", "jpeg", "bmp"],
        "Music": ["mp3"],
        "Text": ["txt", "docx"]
    }

    def __init__(self, path):
        self.path = path if path else os.getcwd()

    def sort_files(self):
        count = 0
        try:
            folders = os.listdir(self.path)
        except FileNotFoundError:
            return "Wrong path. Try to change destination."
        for item in folders:
            temp = item.split('.')
            if len(temp) > 1 and len(temp[0]) > 0:
                for ext_value in self.exts.values():
                    if not ext_value.count(temp[-1]):
                        continue
                    result_folder = dictpy.DictSearch(data=self.exts, target=temp[-1]).result[0][0]
                    if not os.path.isdir(result_folder):
                        os.mkdir(result_folder)
                    os.replace(item, result_folder + "/" + item)
                    count += 1
        return f"Successfully sorted {count} files"


if __name__ == '__main__':
    print("Powered by 1nfer.exe", "-" * 60, sep="\n")
    srt = FileSorter(input("Sorting path (leave the field empty if current path): "))
    print(srt.sort_files())
