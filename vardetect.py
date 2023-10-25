import yaml
import sys

def read_yaml_file(file_path):
    with open(file_path, 'r') as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as exc:
            print(exc)
            return None

def read_var_list(task, key):
    if key in task:
        for var in task[key]:
            print(">>>> VAR:", var)
            print(task[key][var])

def read_task_list(task_list):
    for task in task_list:
        if "block" in task:
            read_task_list(task["block"])

        if "when" in task:
            if isinstance(task["when"], list):
                for line in task["when"]:
                    print(line)
            else:
                print(task["when"])

        if "debug" in task:
            if "msg" in task["debug"]:
                print(task["debug"]["msg"])
        if "fail" in task:
            if "msg" in task["fail"]:
                print(task["fail"]["msg"])

        read_var_list(task, "vars")
        read_var_list(task, "set_fact")

        if "environment" in task:
            for key in task["environment"]:
                print(task["environment"][key])

        if "command" in task:
            print(task["command"])
        if "shell" in task:
            print(task["shell"])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python <script_name>.py <path_to_yaml_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    data = read_yaml_file(file_path)
    
    if data:
        read_task_list(data)
    else:
        print("Failed to read the YAML file.")
