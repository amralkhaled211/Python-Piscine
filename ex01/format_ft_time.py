import time
import datetime

# Get the current time in seconds since the epoch
current_time = time.time()

# Format the current time in seconds and scientific notation
formatted_time = f"Seconds since January 1, 1970: {current_time:,.4f} or {current_time:.2e} in scientific notation"

# Get the current date
current_date = datetime.datetime.now().strftime("%b %d %Y")

# Print the formatted time and date
print(formatted_time)
print(current_date)