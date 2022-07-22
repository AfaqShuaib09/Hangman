''' Main Function of Hangman Program '''

from datetime import datetime

import utils
from constant import TEST_CASES_COUNT

exec_time_of_each_test_case = []

if __name__ == "__main__":
    for test_case in range(0, TEST_CASES_COUNT):
        print("Test Case: ", test_case + 1)
        exec_start_time = datetime.now()
        print("Congratulations! You won"
                if utils.play_hangman()
                else "Sorry! You have failed to guess the word!")
        exec_end_time = datetime.now()

        execution_time = (exec_end_time - exec_start_time).total_seconds()
        exec_time_of_each_test_case.append(execution_time)
        print("Execution Time:", execution_time, " seconds\n")

    print("Average Execution Time:", sum(exec_time_of_each_test_case) / TEST_CASES_COUNT, "seconds")

    test_case = list(range(1, TEST_CASES_COUNT + 1))
    utils.plot_graph(test_case, exec_time_of_each_test_case)
