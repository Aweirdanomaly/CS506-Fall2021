def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    X = []
    with open(csv_file_path, "r") as f:  # Open File
        data = f.readlines()  # Extract Readlines object
        for line in data:  # Iterate through each line, splitting entries by ','
            line = line.strip().replace('"', '').split(',')
            # Convert entries to ints, floats, or strings
            converted_line = []
            for el in line:
                if el.isdecimal():
                    converted_line.append(int(el))
                elif el.isdigit():
                    converted_line.append(float(el))
                else:
                    converted_line.append(str(el))

            X.append(converted_line)

    return X
