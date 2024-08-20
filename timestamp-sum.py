import re
import argparse

def extract_and_sum_timestamps(file_path):
    # Define the regex pattern for timestamps
    pattern = r'\b\d{1,2}:\d{2}\b'
    
    # Initialize the total number of seconds
    total_seconds = 0
    
    # Open and read the file
    with open(file_path, 'r') as file:
        content = file.read()
        
        # Find all timestamps in the file
        timestamps = re.findall(pattern, content)
        
        # Convert each timestamp to total seconds and sum them up
        for timestamp in timestamps:
            minutes, seconds = map(int, timestamp.split(':'))
            total_seconds += minutes * 60 + seconds
    
    # Convert total seconds back to minutes:seconds
    total_minutes, remaining_seconds = divmod(total_seconds, 60)
    
    # Convert total seconds to hours:minutes:seconds
    total_hours, remaining_minutes = divmod(total_minutes, 60)
    
    # Print results
    print(f"Total time: {total_minutes}:{remaining_seconds:02}")
    print(f"Total time: {total_hours} hours, {remaining_minutes} minutes, and {remaining_seconds} seconds")

def main():
    # Argument parsing
    parser = argparse.ArgumentParser(description='Extract and sum timestamps from a file.')
    parser.add_argument('file', type=str, help='Path to the file containing timestamps')
    
    args = parser.parse_args()
    
    # Call the function with the provided file path
    extract_and_sum_timestamps(args.file)

if __name__ == '__main__':
    main()
