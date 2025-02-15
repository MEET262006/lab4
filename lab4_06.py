def print_24_hours():
    for hour in range(24):
        if hour == 0:
            print(f"12:00 {hour}:00 - Midnight")
        elif hour < 12:
            print(f"{hour}:00 {hour}:00 - AM")
        elif hour == 12:
            print(f"{hour}:00 {hour}:00 - Noon")
        else:
            print(f"{hour-12 if hour != 12 else hour}:00 {hour}:00 - PM")

print_24_hours()
