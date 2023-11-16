import json
import os


def get_todo_list():
  with open('todo.json', 'r') as f:
    return json.load(f)

def updateTodo(task, add=True):
  todo_list = get_todo_list()
  
  if add:
    todo_list.append(task)
  else:
    del todo_list[task-1]
  
  with open('todo.json', 'w') as f:
    json.dump(todo_list, f)


def main():
  quit_list = ['q', 'quit', 'end', 'exit', 'end']

  while True:
    os.system('cls')
    todo_list = get_todo_list()
    for index, item in enumerate(todo_list, start=1):
      print('{0} {1}'.format(index, item))

    print('\ncommands:')
    print('add <task>')
    print('rm<#>\n')

    prompt = input('>  ').strip().lower()
    
    if prompt in quit_list:
      break
    
    elif prompt.startswith('add '):
      task = prompt[4:]
      updateTodo(task)

if __name__ == '__main__':
  main()