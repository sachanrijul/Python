# ------------------- Python Date and Time Handling (Complete Notes) -------------------

"""
📆 Python provides powerful built-in and external libraries to work with:
- Dates
- Times
- Durations
- Formatting & parsing
- Calendars and Timezones
"""

# ------------------- 1. Getting Current Date and Time -------------------

from datetime import datetime

now = datetime.now()  # Returns current local date and time
print("Now:", now)
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

# ------------------- 2. datetime.date Class -------------------

from datetime import date

today = date.today()
print("Today:", today)
print("ISO format:", today.isoformat())

# Custom date
d = date(2024, 12, 25)
print("Custom date:", d)

# ------------------- 3. datetime.time Class -------------------

from datetime import time

t = time(14, 30, 45)
print("Custom time:", t)
print("Hour:", t.hour)

# ------------------- 4. datetime.timedelta (Date Arithmetic) -------------------

from datetime import timedelta

today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Tomorrow:", tomorrow)

# Time differences
delta = timedelta(days=5, hours=3)
print("Timedelta:", delta)

# ------------------- 5. datetime.combine() -------------------

d = date(2025, 1, 1)
t = time(12, 0)
combined = datetime.combine(d, t)
print("Combined:", combined)

# ------------------- 6. Formatting Dates with strftime() -------------------

"""
strftime() → Format datetime object as string
Common Directives:
%Y → Year, %m → Month, %d → Day
%H → Hour, %M → Minute, %S → Second
%A → Weekday name, %B → Month name
"""

now = datetime.now()
formatted = now.strftime("%A, %d %B %Y %I:%M:%S %p")
print("Formatted:", formatted)

# ------------------- 7. Parsing Strings with strptime() -------------------

date_str = "29-05-2025 14:30"
dt = datetime.strptime(date_str, "%d-%m-%Y %H:%M")
print("Parsed datetime:", dt)

# ------------------- 8. Timezones with pytz (External Module) -------------------

import pytz

utc_now = datetime.now(pytz.utc)
print("UTC Time:", utc_now)

# Convert to a specific timezone
india = pytz.timezone("Asia/Kolkata")
local_time = utc_now.astimezone(india)
print("India Time:", local_time)

# List of all available timezones
# print(pytz.all_timezones)

# ------------------- 9. Working with time Module -------------------

import time

print("Current epoch time (timestamp):", time.time())

# Sleep for 2 seconds
time.sleep(2)

# Convert timestamp to struct_time
t_struct = time.localtime()
print("Local time struct:", t_struct)

# Format struct_time
print("Formatted:", time.strftime("%Y-%m-%d %H:%M:%S", t_struct))

# ------------------- 10. Getting Timestamps -------------------

now = datetime.now()
timestamp = now.timestamp()
print("Timestamp:", timestamp)

# Convert back from timestamp
dt = datetime.fromtimestamp(timestamp)
print("Datetime from timestamp:", dt)

# ------------------- 11. Working with calendar Module -------------------

import calendar

# Print calendar of a month
print(calendar.month(2025, 5))

# Check if a year is leap
print("Is 2024 leap year?", calendar.isleap(2024))

# Print weekday of a date (0 = Monday)
print("Weekday (0=Mon):", calendar.weekday(2025, 5, 29))

# ------------------- 12. ISO Format and Parsing -------------------

now = datetime.now()
iso = now.isoformat()
print("ISO 8601 Format:", iso)

# Parse ISO string
parsed = datetime.fromisoformat(iso)
print("Parsed from ISO:", parsed)

# ------------------- 13. Creating UTC Datetime -------------------

utc_now = datetime.utcnow()
print("UTC Now:", utc_now)

# ------------------- Summary -------------------

"""
✔ datetime.now()        → Get current date and time
✔ date(), time(), timedelta() → Date/time/duration objects
✔ strftime(), strptime() → Formatting and parsing
✔ pytz → For timezone support
✔ time → System time & sleep
✔ calendar → Monthly/yearly calendars, leap year check
✔ timestamp → Epoch time
✔ datetime.combine(), fromisoformat(), etc. → Advanced usage
"""

# ------------------- End of Date and Time Notes -------------------
