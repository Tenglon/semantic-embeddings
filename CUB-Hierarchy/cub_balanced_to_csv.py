
mode = "flat"

class_names = []
with open(f"./classes_{mode}.txt", "r") as fp:
    lines = fp.readlines()
    for line in lines:
        class_name = line.strip().split(" ")[1:]
        class_name = " ".join(class_name)
        class_names.append(class_name)

son2parent = {}

with open(f"./cub_{mode}.parent-child.txt", "r") as p2c_file:
    lines = p2c_file.readlines()
    for line in lines:
        parent, child = line.strip().split(" ")
        # parent = class_names[int(parent) - 1]
        # child = class_names[int(child) - 1]
        son2parent[child] = parent

with open(f"./cub_{mode}.csv", "w") as csv_file:

    for son, parent in son2parent.items():

        if int(son) > 200:
            continue
        output_line = f"{class_names[int(son) - 1]},{class_names[int(parent) - 1]},"
        cur = parent
        while cur in son2parent:
            cur = son2parent[cur]
            if mode == "flat":
                if cur == "367":
                    break
            elif mode == "balanced":
                if cur == "420":
                    break
            output_line += f"{class_names[int(cur) - 1]},"
        output_line += "Root,1"
        print(output_line)
        csv_file.write(output_line + "\n")

