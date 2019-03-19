import yaml

with open("../data/data.yaml", "r", encoding="utf-8") as file:

    print(yaml.load(file))