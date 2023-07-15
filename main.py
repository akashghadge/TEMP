import os
import datetime
import subprocess

# Get the current directory
directory = os.getcwd()

# Get the desired day in June 2023
variable_day = 15

# Function to change the date of a file and perform Git operations
def change_date_commit(file_path, new_date):
    # Change the date of the file
    os.utime(file_path, (new_date.timestamp(), new_date.timestamp()))

    # Set the commit timestamp
    os.environ["GIT_AUTHOR_DATE"] = new_date.strftime("%Y-%m-%d %H:%M:%S")
    os.environ["GIT_COMMITTER_DATE"] = new_date.strftime("%Y-%m-%d %H:%M:%S")

    # Add and commit the file
    subprocess.run(["git", "add", file_path])
    subprocess.run(["git", "commit", "-m", f"LC Daily Done"])

# Iterate over the files in the directory
for file_name in os.listdir(directory):
    file_path = os.path.join(directory, file_name)
    if os.path.isfile(file_path):
        # Get the first two characters of the file name as day
        file_day = file_name[:2]

        # Create the desired date in June 2023
        new_date = datetime.datetime(2023, 6, 1, 10, int(file_day))
        new_date += datetime.timedelta(days=(int(file_day)-1))

        # Change the date, add, commit, and move to the next file
        change_date_commit(file_path, new_date)
