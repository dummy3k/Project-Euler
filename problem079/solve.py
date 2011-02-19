logins = [
    "319", "680", "180", "690", "129", "620", "762", "689", "762", "318",
    "368", "710", "720", "710", "629", "168", "160", "689", "716", "731",
    "736", "729", "316", "729", "729", "710", "769", "290", "719", "680",
    "318", "389", "162", "289", "162", "718", "729", "319", "790", "680",
    "890", "362", "319", "760", "316", "729", "380", "319", "728", "716"
    ]

def get_predecessor(number):
    #~ number = "1"
    predecessor = set()
    for three_digits in logins:
        if three_digits[1] == number:
            predecessor.add(three_digits[0])

        if three_digits[2] == number:
            predecessor.add(three_digits[0])
            predecessor.add(three_digits[1])

    return predecessor

for n in range(10):
    print "%s: %s" % (n, get_predecessor(str(n)))

# 73162890
