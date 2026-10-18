import subprocess


def greet_user(name):
    query = "Hello, " + name
    print(query)


def run_command(command):
    subprocess.run(command, shell=True)


if __name__ == "__main__":
    greet_user("Student")