#. Cut(slice) out the first word of Coding For All string.
company = "Coding For All"
# Find the index of the first space
first_space = company.find(" ")
# Slice everything after the first space
sliced_company = company[first_space+1:]
print(sliced_company)

