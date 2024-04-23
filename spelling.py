import os
import json


def fix_spelling(file: str):
    dirname = os.path.dirname(__file__)
    t = open(os.path.join(dirname, "corrections.json"))
    jsonF = json.load(t)
    with open(os.path.join(dirname, "current", file), "r") as f:
        content = f.read()
    for values in jsonF["correctionsNeeded"]:
        content = content.replace(values[0], values[1])
    with open(file, "w") as f:
        f.write(content)

    print(f"test {file}")
