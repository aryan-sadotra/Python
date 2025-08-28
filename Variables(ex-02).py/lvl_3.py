#. Compare the length of your first name and your last name
first_name = 'Aryan'
last_name = 'Sadotra'
print("the length of first_name: ", len(first_name))
print("the length of last_name: ", len(last_name))
if len(first_name) > len(last_name) :
    print("first is larger: ", len(first_name))
elif len(first_name) < len(last_name) :
     print("last is larger: ", len(last_name))
else :
     print("they are equal")