tasks = []

def addTask():
  task = input("Enter a new Task: ")
  tasks.append(task)
  print("Task added Successfully!!!")

def viewTask():
  if len(tasks)==0:
    print("No Tasks in the list")
  else:
    for i,task in enumerate(tasks):
      print(f"{i+1}:{task}")

def delTask():
  if len(tasks)==0:
    print("No tasks to be deleted!!")
  else:
    for i,task in enumerate(tasks):
      print(f"{i+1}:{task}")
    choice = int(input("Enter the task number to be deleted: "))
    if 0<choice<=len(tasks):
      del tasks[choice-1]
      print("Task deleted Successfully!!!")
    else:
      print("Please provide correct task number")

def main():
  while True:
    print("********** TO-DO LIST ***********")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Task")
    print("4. Exit")

    choice = int(input("Enter your Choice: "))
    if choice==1:
      addTask()
    elif choice==2:
      delTask()
    elif choice==3:
      viewTask()
    elif choice==4:
      print("Thanks for using.Do try again!")
      break
    else:
      print("Invalid number!")


if __name__=="__main__":
  main()
