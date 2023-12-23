# Sports-Reference-Summer-Intern-Engineering_Prompt


# Head-to-Head Matrix Generator

This Python script generates a head-to-head matrix from the given JSON data, displaying the win records of each team against opponents. The resulting matrix is printed in a tabular format using the `tabulate` library.

## Prerequisites

- Python 3.x
- `tabulate` library (install using `pip install tabulate`)

## Usage

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/head-to-head-matrix.git
    cd Sports-Reference-Summer-Intern-Engineering_Prompt
    ```

2. **Run the Script:**

    Replace 'your_file_path.json' in the script with the actual file path containing your JSON data. Then, run the script:

    ```bash
    python head_to_head_matrix.py
    ```
    The script will generate and print the head-to-head matrix in the console.

## Algorithm Explanation:

## Algorithm Explanation

The algorithm begins by extracting the list of teams from the supplied JSON data and initializes a 2D matrix to represent head-to-head win records. It iterates through each team, populating the first row and column of the matrix with team names. A nested loop then fills the matrix with head-to-head win records, using '--' for diagonal elements where team names match. The algorithm efficiently processes the JSON data, constructs the matrix, and leverages the `tabulate` library for a clear presentation of the head-to-head record table. With a time complexity of O(n^2), where n is the number of teams in the dataset, the algorithm effectively captures and visualizes inter-team win records.

