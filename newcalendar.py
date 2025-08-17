import calendar
from rich.console import Console
from rich.table import Table
from datetime import datetime

# Create console object
console = Console()

# Get current date
now = datetime.now()
current_day = now.day
current_month = now.month
current_year = now.year

# User input for month and year
year = int(input(f"Enter year [{current_year}]: ") or current_year)
month = int(input(f"Enter month (1-12) [{current_month}]: ") or current_month)

# Get month calendar
cal = calendar.monthcalendar(year, month)
month_name = calendar.month_name[month]

# Create a table
table = Table(title=f"[bold cyan]{month_name} {year}[/bold cyan]", show_lines=True)

# Add days of the week
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for day in days:
    style = "bold magenta" if day in ["Sat", "Sun"] else "bold"
    table.add_column(day, justify="center", style=style)

# Add calendar rows
for week in cal:
    row = []
    for day in week:
        if day == 0:
            row.append("")
        elif day == current_day and month == current_month and year == current_year:
            row.append(f"[reverse bold red]{day}[/reverse bold red]")
        else:
            row.append(str(day))
    table.add_row(*row)

# Print the calendar
console.print(table)
