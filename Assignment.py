import pandas as pd
from datetime import timedelta


def parse_timedelta(timedelta_str):
    """
    Parse a timedelta string in the format 'hours:minutes' into a timedelta object.
    """
    try:
        hours, minutes = map(int, timedelta_str.split(':'))
        return timedelta(hours=hours, minutes=minutes)
    except (ValueError, TypeError):
        return None


def format_timedelta(td):
    """
    Format a timedelta object into a string in the format 'X hours Y minutes'.
    """
    hours, remainder = divmod(td.seconds, 3600)
    minutes = remainder // 60
    return f"{hours} hours {minutes} minutes"


def analyze_file(file_path, output_file_path):
    """
    Analyze the CSV file for employee shifts and write the results to an output file.

    Parameters:
    - file_path: str, path to the CSV file
    - output_file_path: str, path to the output text file
    """
    # Read CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Check if 'Position ID' column exists
    if 'Position ID' not in df.columns:
        print("Error: 'Position ID' column not found in the dataset.")
        return

    current_employee = None
    shift_start_time = None
    last_shift_end_time = None

    # Lists to store information about employees who meet conditions
    employees_less_than_10_hours = []
    employees_more_than_14_hours = []

    with open(output_file_path, 'w') as output_file:
        for i, row in df.iterrows():
            if current_employee is None or current_employee != row['Employee Name']:
                # Reset shift information when encountering a new employee
                shift_start_time = None
                last_shift_end_time = None
                current_employee = row['Employee Name']

            if not pd.isna(row['Timecard Hours (as Time)']):
                shift_duration = parse_timedelta(row['Timecard Hours (as Time)']).total_seconds() / 3600

                # Convert 'Time' to datetime
                row_time = pd.to_datetime(row['Time'])

                # Check shift gap
                if shift_start_time and (row_time - shift_start_time).total_seconds() / 3600 < 10 and \
                        (row_time - shift_start_time).total_seconds() / 3600 > 1:
                    employees_less_than_10_hours.append(
                        (current_employee, row['Position ID'], shift_start_time, last_shift_end_time))

                # Check long shift
                if shift_duration > 14:
                    employees_more_than_14_hours.append(
                        (current_employee, row['Position ID'], shift_start_time, last_shift_end_time))

                # Update shift information for the next iteration
                shift_start_time = row_time
                last_shift_end_time = row_time + timedelta(hours=shift_duration)

        # Write results to the file
        output_file.write("\nEmployees who have less than 10 hours between shifts but greater than 1 hour:\n")
        for employee, position_id, start_time, end_time in employees_less_than_10_hours:
            time_worked = format_timedelta(end_time - start_time)
            output_file.write(f"Employee Name: {employee}, Position ID: {position_id}, Time Worked: {time_worked}\n")

        output_file.write("\nEmployees who have worked for more than 14 hours in a single shift:\n")
        for employee, position_id, start_time, end_time in employees_more_than_14_hours:
            time_worked = format_timedelta(end_time - start_time)
            output_file.write(f"Employee Name: {employee}, Position ID: {position_id}, Time Worked: {time_worked}\n")


if __name__ == "__main__":
    # Assumption: The CSV file has the same structure as the original Excel file.
    file_path = "Assignment Timecard.csv"
    output_file_path = "output/output.txt"
    analyze_file(file_path, output_file_path)
