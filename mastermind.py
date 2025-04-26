import random


class Mastermind:
    def __init__(self):
        self.goal_combination = [random.choice(range(1, 9)) for i in range(5)]
        self.num_of_guesses = 0
        self.correct = False

    def ask_for_guess(self):
        guess_validity = False
        while guess_validity == False:
            guess = input(
                'Please input your guess in the form of five numbers from 1-8 with no other characters.')
            if len(guess) != 5:
                print('Invalid guess')
                continue
            elif '0' in guess or '9' in guess:
                print('Invalid guess')
                continue
            elif guess.isnumeric():
                guess_validity = True
        guess = list(guess)
        for i in range(5):
            guess[i] = int(guess[i])
        return guess

    def compare_guess_to_goal_easy(self, goal_combination, guess):
        incorrect_indices = [0, 1, 2, 3, 4]
        result = ['_' for i in range(5)]
        for i in range(5):
            if goal_combination[i] == guess[i]:
                incorrect_indices.remove(i)
                result[i] = 'Black'
        guess_incorrect = [guess[i] for i in incorrect_indices]
        goal_combination_incorrect = [goal_combination[i]
                                      for i in incorrect_indices]
        for i in range(5):
            if guess[i] in guess_incorrect and guess[i] in goal_combination_incorrect:
                goal_combination_incorrect.remove(guess[i])
                result[i] = 'White'
        if len(incorrect_indices) == 0:
            self.correct = True
        self.num_of_guesses += 1
        return result

    def compare_guess_to_goal_hard(self, goal_combination, guess):
        black_count = 0
        white_count = 0
        incorrect_indices = [0, 1, 2, 3, 4]
        for i in range(5):
            if goal_combination[i] == guess[i]:
                black_count += 1
                incorrect_indices.remove(i)
        guess_incorrect = [guess[i] for i in incorrect_indices]
        goal_combination_incorrect = [goal_combination[i]
                                      for i in incorrect_indices]
        for num in guess_incorrect:
            if num in goal_combination_incorrect:
                white_count += 1
                goal_combination_incorrect.remove(num)
        result = ['Black' for i in range(black_count)]
        for i in range(white_count):
            result.append('White')
        for i in range(5 - len(result)):
            result.append('_')
        if len(incorrect_indices) == 0:
            self.correct = True
        self.num_of_guesses += 1
        return result

    def play_game(self):
        rules_answer = input(
            print('Welcome to this game of Mastermind! Type Y to see the rules.'))
        if rules_answer == 'Y':
            print('rules')
        easy_or_hard = ''
        while easy_or_hard != 'E' and easy_or_hard != 'H':
            easy_or_hard = input('Type E for easy mode or H for hard mode.')
            if easy_or_hard != 'E' and easy_or_hard != 'H':
                print('Please input E or H.')

        while self.num_of_guesses < 13 and self.correct == False:
            guess = self.ask_for_guess()
            if easy_or_hard == 'E':
                print(self.compare_guess_to_goal_easy(
                    self.goal_combination, guess))
            else:
                print(self.compare_guess_to_goal_hard(
                    self.goal_combination, guess))
        if self.correct:
            print(
                f'Congratulations! You got the combination in {self.num_of_guesses} attempts.')
        else:
            print(
                f'Unlucky, you used your 12 attempts. The correct combination was {self.goal_combination}.')


game = Mastermind()
# print(game.ask_for_guess())

# print(game.compare_guess_to_goal([1, 1, 1, 1, 5], [0, 1, 0, 0, 5]))
game.play_game()
