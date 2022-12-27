import pandas as pd
import numpy as np
import string
import functools
import uuid
uuid.uuid4()
# Set the seed for the random number generator
np.random.seed(42)

# Set the number of rows and columns in the CSV file
num_timestamps = int(1e4)
num_ids =  int(1e2)
num_rows = num_timestamps * num_ids
# Set the names and data types of the columns in a dictionary
columns = {
    'time': 'time',
    'id': 'uuid',
    'col1': 'float',
    'col2': 'float',
    'col3': 'float',
    'col4': 'float',
    'col5': 'float',
    'col6': 'float',
    'col7': 'float',
    'col8': 'float',
    'col9': 'float',
    'col10': 'float'
}

# Create an empty DataFrame with the specified columns
df = pd.DataFrame(columns=columns.keys())

# Define a dictionary that maps data types to functions for generating random data
data_generators = {
    'time': lambda: np.repeat(pd.date_range(start = "1970-01-01", periods=num_timestamps, freq="h"), num_ids),
    'uuid': lambda:  [uuid.uuid4() for x in range(num_ids)] * num_timestamps,    
    'int': functools.partial(np.random.randint, 0, 100, num_rows),
    'float': functools.partial(np.random.uniform, low = 0, high = 100, size  = num_rows),
    'str': lambda: [''.join(np.random.choice(list(string.ascii_letters + string.digits), size=10)) for _ in range(num_rows)]
}

# Generate random data for each column
for col_name, col_type in columns.items():
    df[col_name] = data_generators[col_type]()

df.to_csv("test_data.csv", index = False, header = False)
