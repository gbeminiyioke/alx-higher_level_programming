#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for def_names in dir(hidden_4):
        if def_names[0] != '_' and def_names[1] != '_':
            print(def_names)
