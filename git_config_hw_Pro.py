# Импортируем библиотеку subprocess
import subprocess as sb

# Определяем функцию git_config_list, которая будет выполнять команду Git 
# (нужно в консоль вывести результат работы команды git: git config --global --list)
def git_config_list():
    # Используем subprocess.run для выполнения команды в переменной result
    result = sb.run(['git', 'config', '--global', '--list'])
    # Выводим результат выполнения команды result.stdout
    print (result.stdout)

# вызываем git_config_list()
git_config_list()
