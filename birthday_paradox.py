"""
  Birthday paradox
"""

from random import randint

PEOPLE = 23
NUM_BIRTHDAYS = 365
TRIES = 100

def gen_birthdays(num_people):
    birthdays = []
    for i in range(num_people):
        birthday = randint(1, NUM_BIRTHDAYS)
        birthdays.append(birthday)
    return birthdays

def check_uniqueness(birthdays):
    unique_bir = set(birthdays)
    if (len(birthdays) != len(unique_bir)):
        return 0
    else:
        return 1


if __name__ == '__main__':
    count = 0
    for _ in range(TRIES):
        birthdays = gen_birthdays(PEOPLE)
        print(f"These are the birthdays of {PEOPLE} people: \n{birthdays}")
        unique = check_uniqueness(birthdays)
        if unique == 1:
            count = count + 1
            print("No one has the same birthday\n")
        else:
            print("Someone has the same birthday\n")
    prob_unique = (count/TRIES)*100
    prob_repeated = 100 - prob_unique
    print(f"The percentage of {PEOPLE} in a room having the same brithday is {prob_repeated}% (the percentage was calculated be doing {TRIES} trials).")
