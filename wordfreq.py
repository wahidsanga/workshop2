def count_words(file_path):
    try:
        with open(file_path, 'r', encoding='ISO-8859-1') as file:
            content = file.read()
            word_count = len(content.split())
            return word_count
    except FileNotFoundError:
        print("File not found.")
        return -1
    except Exception as e:
        print("Error occurred:", e)
        return -1

file_path = "Phillip.txt"
word_count = count_words(file_path)

if word_count >= 0:
    print("Number of words in the file:", word_count)
