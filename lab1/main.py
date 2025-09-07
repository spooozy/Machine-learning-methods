from part1 import task1_1, task1_2, task1_3, task1_4, task1_5, task1_6
from part2 import task2_1, task2_2, task2_3, task2_4
from part3 import task3_1, task3_2, task3_3, task3_4

def main():
    exit_flag = False
    current_task = 0
    tasks_list = [task1_1, task1_2, task1_3, task1_4, task1_5, task1_6, task2_1, task2_2, task2_3, task2_4, task3_1, task3_2, task3_3, task3_4]
    while not exit_flag:
        print("-" * 36)
        choice = int(input("- 1. Move to the next task\n- 2. Return to the previous one\n- 3. Repeate current task\n- 4. Select a task\n- 5. Exit\n- Option: "))
        print("-" * 36)
        match choice:
            case 1:
                current_task = min(current_task + 1, len(tasks_list))
                tasks_list[current_task]()
            case 2:
                current_task = max(current_task - 1, 0)
                tasks_list[current_task]()
            case 3:
                exit_flag = False
            case 4:
                task_number = 1
                for task in tasks_list:
                    print(f"{task_number}. {task.__name__}")
                    task_number += 1
                task_number = int(input("Select a task: "))
                print("-" * 36)
                if 1 <= task_number <= len(tasks_list):
                    current_task = task_number - 1
                    tasks_list[current_task]()
            case 5:
                exit_flag = True
            case _:
                print("Wrong input")

if __name__ == "__main__":
    main()