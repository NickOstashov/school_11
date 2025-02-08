from plan_text import *

def start_add_task(week: dict) -> None:
    choice_day = input(CHOICE_DAY_TO_ADD_TASK)
    if choice_day in week:
        task = input(INPUT_TASK_TEXT)
        week[choice_day].add(task)
    else:
        print(NO_SEARCH_DAY)

def start_output_task(week: dict) -> None:
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