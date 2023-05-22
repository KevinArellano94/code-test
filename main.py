import tkinter as tk

num_rows = 5
num_columns = 5

letter_set = (
    ('L', 'I', 'O', 'N', 'F'),
    ('B', 'E', 'A', 'R', 'D'),
    ('I', 'S', 'H', 'C', 'A'),
    ('R', 'D', 'T', 'I', 'T'),
    ('F', 'A', 'C', 'T', 'S')
)

window = tk.Tk()
window.title('Word Search')

buttons = []
letters = []
selected_letters = []

answer_key = ['LION', 'BEAR', 'FISH', 'BIRD', 'CAT']
remaining_words = answer_key.copy()

def button_click(i, j):
    letter = letter_set[i][j]
    selected_letters.append(letter)
    display_selected_letters()
    validate_word()

def validate_word():
    selected_word = ''.join(selected_letters)
    if selected_word in answer_key:
        print(f"Found word: {selected_word}")
        remaining_words.remove(selected_word)
        display_remaining_words()
        clear_selection()
        if not remaining_words:
            print("Congratulations! You found all the words.")
    else:
        print(f"Current selection: {selected_word}")

def clear_selection():
    selected_letters.clear()
    display_selected_letters()

def display_selected_letters():
    selected_letters_label.config(text='Selected Letters: ' + ''.join(selected_letters))

def display_remaining_words():
    remaining_words_label.config(text='Remaining Words: ' + ', '.join(remaining_words))

for i in range(num_rows):
    row = []
    for j in range(num_columns):
        button = tk.Button(window, text=letter_set[i][j], width=10, height=3, command=lambda i=i, j=j: button_click(i, j))
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

selected_letters_label = tk.Label(window, text='Selected Letters: ')
selected_letters_label.grid(row=num_rows+1, columnspan=num_columns)

remaining_words_label = tk.Label(window, text='Remaining Words: ' + ', '.join(remaining_words))
remaining_words_label.grid(row=num_rows+2, columnspan=num_columns)

clear_button = tk.Button(window, text='Clear Selection', command=clear_selection)
clear_button.grid(row=num_rows+3, columnspan=num_columns)

window.mainloop()