import pandas as pd
import os
import glob
import datetime

def combine_and_process_csv_files(directory, output_filename):
    """
    Combines CSV files in a directory, processes ctime and adds satisfaction labels.

    Args:
        directory: The path to the directory containing the CSV files.
        output_filename: The name of the combined and processed CSV file.
    """

    os.chdir(directory)
    all_filenames = [i for i in glob.glob('*.csv')]

    combined_data = pd.concat([pd.read_csv(f) for f in all_filenames])

    
    # Assuming 'ctime' and 'rating_star' columns exist in the combined DataFrame
    satisfaction_labels = {
        1: "Very Dissatisfied",
        2: "Dissatisfied",
        3: "Neutral",
        4: "Satisfied",
        5: "Very Satisfied",
    }

    # Convert ctime and add satisfaction labels
    for index, row in combined_data.iterrows():
        ctime_str = row['ctime']  
        ctime_str = row['ctime']  
        if pd.notna(ctime_str):  # Check if ctime is not missing
            try:
                ctime_dt = datetime.datetime.fromtimestamp(int(ctime_str))
                combined_data.at[index, 'ctime'] = ctime_dt.strftime("%Y-%m-%d %H:%M:%S")
            except ValueError:
                print(f"Warning: Invalid ctime value '{ctime_str}' in row {index + 1}. Skipping conversion.")
        else:
            print(f"Warning: Missing ctime value in row {index + 1}.")

        try:
            combined_data.at[index, 'satisfaction_label'] = satisfaction_labels[row['rating_star']]
        except KeyError:
            print(f"Warning: Invalid rating value '{row['rating_star']}' in row {index + 1}. Skipping label assignment.")

    # Drop specified columns, ignoring errors if they don't exist
    combined_data.drop(columns=['itemid', 'cmtid', 'rating', 'comment', 'skin_suitability', 'absorption', 'model_name'], inplace=True, errors='ignore')

    # Export to csv
    combined_data.to_csv(output_filename, index=False, encoding='utf-8-sig')
    print(f"Combined and processed CSV files saved as {output_filename} in {directory}")

# Example usage (modify these paths as needed):
directory_path = "D:\github files\machine-learning-thesis\pypypy" 
output_file = "combined_processed_data.csv"
combine_and_process_csv_files(directory_path, output_file)
