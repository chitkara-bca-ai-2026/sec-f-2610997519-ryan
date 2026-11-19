
print("=" * 40)
print("      CALENDAR VERIFICATION SYSTEM")
print("=" * 40)

year = int(input("Enter year: "))

if year <= 0:
    print("Error: Year must be a positive integer.")

else:
    # Check whether the year is a leap year
    if year % 400 == 0:
        is_leap = True
        reason = "Century year divisible by 400"
    elif year % 100 == 0:
        is_leap = False
        reason = "Century year not divisible by 400"
    elif year % 4 == 0:
        is_leap = True
        reason = "Divisible by 4 and not a century year"
    else:
        is_leap = False
        reason = "Not divisible by 4"

    # Determine calendar details
    if is_leap:
        status = "LEAP YEAR"
        february_days = 29
        total_days = 366
    else:
        status = "COMMON YEAR"
        february_days = 28
        total_days = 365

    # Display results
    print("\n" + "-" * 40)
    print(f"Year: {year}")
    print(f"Status: {status}")
    print(f"Days in Year: {total_days} days")
    print(f"Days in February: {february_days} days")
    print(f"Reason: {reason}")
    print("-" * 40)