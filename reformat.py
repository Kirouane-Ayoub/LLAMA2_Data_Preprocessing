import pandas as pd

# Function to reformat and save data to a CSV file
def reformat_and_save(dataset_path, char_id):
    # Read the CSV dataset into a DataFrame using pandas
    df = pd.read_csv(dataset_path)

    text_col = []  # Initialize an empty list to store the reformatted text data

    # Loop through each row in the DataFrame using the iterrows() function
    for _, row in df.iterrows():
        prompt = "here we write our prompt.\n\n"  # Initial prompt text

        # Extract values from the row's columns
        instruction = str(row["instruction"])
        input_query = str(row["input"])
        response = str(row["output"])

        # Check if input_query is empty or not
        if len(input_query.strip()) == 0:
            # If input_query is empty, format text with only instruction and response
            text = prompt + "### Instruction\n" + instruction + "\n###Response:\n" + response
        else:
            # If input_query is not empty, format text with instruction, input, and response
            text = (
                prompt
                + "### Instruction\n"
                + instruction
                + "\n###Input\n"
                + input_query
                + "\n###Response:\n"
                + response
            )

        text_col.append(text)  # Append the reformatted text to the text_col list

    # Add the reformatted text data as a new column "text" to the DataFrame
    df["text"] = text_col

    # Save the DataFrame to a new CSV file with the given char_id as the filename
    df.to_csv(f"{char_id}.csv", index=False)

# Example usage of the reformat_and_save function
dataset_path = "example_dataset.csv"
char_id = "reformatted_data"
reformat_and_save(dataset_path, char_id)

