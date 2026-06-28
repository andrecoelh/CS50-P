months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip()

    try:
        parts = date.split('/')

        n_month = int(parts[0])
        n_day = int(parts[1])
        year = parts[2]

        if 1 <= n_month <= 12 and 1 <= n_day <= 31:
            print(f"{year}-{n_month:02}-{n_day:02}")
            break

    except (IndexError, ValueError):
        try:
            monthday, year = date.split(",")
            month, day = monthday.split()

            n_month = months.index(month) + 1
            n_day = int(day)

            if 1 <= n_day <= 31:
                print(f"{year.strip()}-{n_month:02}-{n_day:02}")
                break

        except (ValueError, IndexError):
            pass