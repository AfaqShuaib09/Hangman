''' Functions declared in that file to use in index.py file (main function) '''

import matplotlib.pyplot as plt
import requests

from constant import FILE_NAME, HANGMAN_API_URL, MAX_ATTEMPTS


def create_hangman_game() -> tuple():
    '''
    Creation of Hangman Game using HANGMAN_API (POST REQUEST) and return the hangman word and token
    '''
    response = requests.post(HANGMAN_API_URL)
    return (response.json().get('hangman'), response.json().get('token'))


def filter_words_from_dictionary(file_name : str, word_length : int, list_of_words : list):
    '''
    Read the dictionary file and append the words of given length to the list_of_words
    '''
    with open(file = file_name, mode = 'r', encoding = 'utf-8') as dictionary:
        for word in dictionary:
            word = word.rstrip().lower()
            if len(word) == word_length:
                list_of_words.append(word)


def play_hangman():
    '''
    Create a Hangman Game and play the game and guess the hangman word from the words filtered from the dictionary
    file and return True if it guesses the word correctly else return False
    '''

    hangman_word, req_token = create_hangman_game()

    previous_guesses = []

    remaining_attempts = MAX_ATTEMPTS
    index_list = []
    is_guess = False

    filtered_words = []
    temp_filtered_words = []

    filter_words_from_dictionary(FILE_NAME, len(hangman_word), filtered_words)

    while True: # This is like do
        letter_count = {}

        for words in filtered_words:
            for letter in words:
                if letter in previous_guesses:
                    pass
                elif letter_count.get(letter):
                    letter_count[letter] += 1
                else:
                    letter_count[letter] = 1

        # Check if the user has guessed the word
        if not letter_count and len(filtered_words) == 1:
            is_guess = True
            break

        # get maximum occurence word from the letter_count dictionary
        try:
            max_key = max(letter_count, key=letter_count.get)
            previous_guesses.append(max_key)
        except ValueError:
            print("No more words in the dictionary")
            break

        guess_response = requests.put(HANGMAN_API_URL, data={'token': req_token, 'letter': max_key})

        # update the hangman_word, req_token
        hangman_word, req_token = (guess_response.json().get('hangman').lower(), guess_response.json().get('token'))

        guess_ch_indexes = [char_position for char_position, char in enumerate(hangman_word) if char == max_key]

        if len(guess_ch_indexes) == 0:
            remaining_attempts -= 1
            index_dec = 0
            for(index, word) in enumerate(filtered_words):
                if max_key in word:
                    index_list.append(index-index_dec)
                    index_dec += 1
            # Pop the words from filtered_words at given index
            for index in index_list:
                filtered_words.pop(index)
            index_list.clear()
        else:
            for word in filtered_words:
                if (max_key in word and [char_position for char_position, char in enumerate(word)
                                            if char == max_key] == guess_ch_indexes):
                    temp_filtered_words.append(word)

            filtered_words = []
            filtered_words = temp_filtered_words
            temp_filtered_words = []

        if (is_guess or not remaining_attempts): # this is like while condition
            break

    # To check if the user has guessed the word at last attempt
    if not is_guess:
        if len(list(dict.fromkeys(filtered_words))) == 1:
            is_guess = True

    print(f"Remaining Wrong Attempts: {remaining_attempts}")
    print("Hangman Word: ", hangman_word)

    return is_guess


def plot_graph(test_case_no : list, execution_time : list):
    ''' Plot the execution time vs test case count '''
    plt.plot(test_case_no, execution_time)
    plt.xlabel('Test Case No.')
    plt.ylabel('Time (sec)')
    plt.show()
