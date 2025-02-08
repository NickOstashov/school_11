from plan_text import *

def start_add_task(week: dict) -> None:
    choice_day = input(CHOICE_DAY_TO_ADD_TASK)
    if choice_day in week:
        task = input(INPUT_TASK_TEXT)
        week[choice_day].add(task)
    else:
        print(NO_SEARCH_DAY)


def start_output_task(week: dict) -> None:
    day_or_week = input(DAY_OR_WEEK)
    if day_or_week == '1':
        choice_day = input(CHOICE_DAY_TO_ADD_TASK)
        if choice_day in week:
            print_day(week, choice_day)
        else:
            print(NO_SEARCH_DAY)
    elif day_or_week == '2':
        print_week(week)
    else:
        print(NO_SEARCH_COMMAND)


def get_max_len(tasks : list) -> int:
    max_len = len(tasks[0])
    for task in tasks:
        if len(task) > max_len:
            max_len = len(task)

    return max_len


def print_day(week: dict, day: str) -> None:
    max_len = get_max_len(week[day]) + 2
    print('+', '-'*max_len, '+')
    print('|',' ')


def print_week(week: dict) -> None:
    pass


def start_remove_task(week: dict) -> None:
    pass


def main():
    week = {
        'пн': [],
        'вт': [],
        'ср': [],
        'чт': [],
        'пт': [],
        'сб': [],
        'вс': []
    }

    print(HELLO_PLAN_TEXT)
    print(FUNCTIONS_PRINT)
    choice = input(CHOICE_PRINT)
    while choice != '4':
        if choice == '1':
            start_add_task(week)
        elif choice == '2':
            start_output_task(week)
        elif choice == '3':
            start_remove_task(week)
        else:
            print(NO_SEARCH_COMMAND)

        print(FUNCTIONS_PRINT)
        choice = input(CHOICE_PRINT)