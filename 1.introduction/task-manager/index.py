tasks = []

def add_task(tasks, task_name):
    new_task = {"tarefa": task_name, "completed": False}
    tasks.append(new_task)
    print(f"Tarefa '{tasks}' adicionada com sucesso!")
    return

def list_tasks(tasks):
    print("Tarefas:")
    for index, task in enumerate(tasks):
        status = "✅" if task["completed"] else "❌"
        print(f"{index + 1}. {task['tarefa']} - {status}")
    return

def update_task(tasks, task_index, task_name):
    if task_index < 0 or task_index >= len(tasks):
        print("Índice inválido!")
        return

    tasks[task_index]["tarefa"] = task_name
    print(f"Tarefa '{tasks[task_index]['tarefa']}' atualizada com sucesso!")
    return

def mark_task_as_completed(tasks, task_index):
    tasks[task_index]["completed"] = True
    print(f"Tarefa '{tasks[task_index]['tarefa']}' marcada como concluída com sucesso!")
    return

def delete_task(tasks, task_index):
    del tasks[task_index]
    print(f"Tarefa '{tasks[task_index]['tarefa']}' deletada com sucesso!")
    return

while True:
    print("Menu do gerenciador de tarefas:")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Atualizar tarefa")
    print("4. Marcar tarefa como concluída")
    print("5. Deletar tarefa")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        task_name = input("Digite o nome da tarefa: ")
        add_task(tasks, task_name)

    elif opcao == "2":
        list_tasks(tasks)

    elif opcao == "3":
        list_tasks(tasks)
        task_index = int(input("Informe o índice da tarefa que você deseja atualizar: "))
        task_name = input("Digite o novo nome da tarefa: ")
        update_task(tasks, task_index, task_name)

    elif opcao == "4":
        list_tasks(tasks)
        task_index = int(input("Informe o índice da tarefa que você deseja marcar como concluída: "))
        mark_task_as_completed(tasks, task_index)
        list_tasks(tasks)

    elif opcao == "6":
        break