# try converting 14.1 to DMS, you get 5' and 60" (ain't no 60 seconds) huh.

def to_degrees_minutes_seconds(decimal_degrees):
    """
    converts decimal degrees to degrees minutes seconds
    :param decimal_degrees: degrees latitude or longitude (assume non-negative numbers)
    :return: degrees, minutes as whole numbers and seconds rounded to 3 decimal places
    """
    degrees = int(decimal_degrees)  # decimal_degrees // 1 works too!
    leftover = decimal_degrees - degrees
    minutes = int(leftover * 60)
    seconds = round((leftover * 60 - minutes) * 60, 3)
    mnt, sec = divmod(abs(decimal_degrees) * 3600, 60)
    deg, mnt = divmod(mnt, 60)

    return degrees, minutes, seconds, deg, mnt, sec


if __name__ == '__main__':
    coords = [0, 12.5, 13.75, 14.1, 12 + 30 / 60 + 46 / 3600]

    for coord in coords:
        degrees, minutes, seconds, deg, mnt, sec = to_degrees_minutes_seconds(coord)
        """decimal_degrees = float(input("Enter a latitude or longitude in decimal degrees: "))

        print("Degrees: ",degrees)
        print("Minutes: ",minutes)
        print("Seconds: ",seconds)"""
        # print(f"{degrees}° {minutes}' {seconds}\"")
        print(f"({coord}, {degrees}, {minutes}, {seconds}),")
        print(f"({coord}, {deg}, {mnt}, {sec}),")
