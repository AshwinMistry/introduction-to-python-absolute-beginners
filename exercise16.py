filename = input('File name? ')
data = open(filename, 'r')

n_lines = 0
n_words = 0
n_chars = 0

for line in data:
    n_lines += 1

    words_in_line = line.split()
    n_words += len(words_in_line)

    n_chars += data

data.XXXX()
print(filename, n_lines, n_words, n_chars)

