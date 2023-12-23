import json
from tabulate import tabulate

def build_head_to_head_matrix(data):
    teams = list(data.keys())
    matrix = [[' ' for _ in range(len(teams) + 1)] for _ in range(len(teams) + 1)]

    # Fill the first row and first column with team names
    for i in range(1, len(teams) + 1):
        matrix[0][i] = matrix[i][0] = teams[i - 1]

    # Fill the matrix with head-to-head records
    for i in range(1, len(teams) + 1):
        for j in range(1, len(teams) + 1):
            team1 = teams[i - 1]
            team2 = teams[j - 1]

            if team1 == team2:
                matrix[i][j] = '--'
            else:
                matrix[i][j] = data[team1][team2]["W"]

    return matrix

def print_matrix(matrix):
    headers = matrix[0][1:]
    rows = [[matrix[i][0]] + matrix[i][1:] for i in range(1, len(matrix))]
    # Adjust the table format
    print(tabulate(rows, headers, tablefmt="fancy_grid"))

if __name__ == "__main__":
    # Replace 'your_file_path.json' with the actual file path containing your JSON data
    with open('your_file_path.json') as json_file:
        data = json.load(json_file)

    matrix = build_head_to_head_matrix(data)
    print_matrix(matrix)
