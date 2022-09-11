gallons = 45000
if gallons > 25000 and gallons < 50000:
    print("$", 25000 * (2.35/1000) + (50000 - gallons) * (6.60/1000))
elif gallons > 50000:
    print("$", 25000 * (2.35/1000) + 25000 * (6.60/1000) + (gallons - 50000) * (8.84/1000))
elif gallons < 25000:
    print("$", (25000 - gallons) * (2.35/1000))
gallons = 125000
if gallons > 25000 and gallons < 50000:
    print("$", 25000 * (2.35/1000) + (50000 - gallons) * (6.60/1000))
elif gallons > 50000:
    print("$", 25000 * (2.35/1000) + 25000 * (6.60/1000) + (gallons - 50000) * (8.84/1000))
elif gallons < 25000:
    print("$", (25000 - gallons) * (2.35/1000))
