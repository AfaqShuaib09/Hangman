# Hangman

## Task Description
An Automated Hangman Game developed using [Hangman API](https://hangman-api.herokuapp.com/api). **(Hangman Bot)**

### Constraints
- The maximum number of chances for guessing a word in each round is 7.
- The probability of guessing a word is 100%
- There can be upper/lower letters within the string from [Hangman API](https://hangman-api.herokuapp.com/api), but in the dictionary may or may not. 

 ## Task Solution (Approach)
 ---
 The solution Approach is as follows
 - Create a new Hangman game using Hangman API
 - Then after getting a word from Hangman API, I filter out all the words from the text file named *'dictionary.txt' having a length equal to the word which I get from Hangman API.
 - Instead of making a random guess, I will calculate the occurrence of each letter from the filtered words. 
 - The advantage of the frequency matrix over the random guess is that by getting the occurrences of each letter from the frequency matrix, we can have the now greater probability of making the correct guess, but in case it's not correct then it will reduce the filtered words (searching domain) to a larger extent and frequency matrix will be updated on each iteration of guessing a word. On the other hand, if we use a random guess probability of each word occurrence is 1/26 for the first guess for each position and 1/25 (because guessed letter removes from the domain of alphabets in case of wild guess) for 2nd guess for each of the remaining positions and so on. 

 - Then I go by guessing the letter having the maximum occurrences (because it has the highest probability of occurrence in it)
 - When I will guess the letter, there might be three possibilities  
 The guessed letter   
    1. Doesn't occur in that word  
    2. Having a single occurrence in that word
    3. Having multiple occurrences in that word      
<br>

    -  For Case 1: (No Occurrence)
        > I will exclude all the words, having the occurrence of the guessed letter, so that my searching domain will reduce. Then I will go with the letter having the maximum probability of occurrence in the remaining filtered words and so on.

    -  For Case 2: (Single Occurrence)
        > In case of a single occurrence, I will check for all those words from my filtered domain of words having that guessed letter at the same index as of word, which I get from Hangman API and having only a single occurrence (not more than once) of the guessed letter, so that our searching domain will further reduce and then go with a guess of the most frequent letter in our updated domain of words.

    - For Case 3: (Multiple Occurrences)
        > In case of multiple occurrences, I will further reduce the domain down to only those words having an equal number of occurrences of the guessed letter and at the same indexes to the word which I get from API and then go with a guess of the most frequent letter in our updated domain of words.

- If there is a tie between the occurrence of two letters, then we will pick one of them randomly. 

- Tries count always decreases after making the wrong attempt. The round will end after 7 wrong attempts.

- After completing the round, the user will be prompted to enter the next round.

----
<br>

## Pseudo Code

```python
 1. Get the word from API Call in underscore format 
 2. Filter out only those words from dictionary.txt having length equal to the word which I get from API.
 3. Initialize tries_count to 0 and boolean variable gussed to False
 4. Calculate occurrence of each letter in words

 5.  do
    5.1 Get the Letter with maximum occurrences in filtered words from dictionary
    5.2 Request with that letter to the API
    5.3 If letter not occurs
        5.3.1 Remove all those words from filtered words having that guessed letter.
        5.3.2 tries_count increment by one.
    5.4 elif letter occurs
        5.4.1 If all letters guessed
            5.4.1.1 set guessed variable to true
        5.4.2 else
            5.4.2.1 Update the filtered words by keeping only those words having the letter positions in the word at the same index.
    while guessed != True or tries_count == 7  

6. if guessed is True
    6.1. Prompt some "Congratulations" message and move the user to the other level
7. else 
    7.1. Prompt some "Try Again" message and move the user back to menu.
    

```

