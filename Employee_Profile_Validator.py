# Employee Profile Validator 
email = 'alice.johnson@company.com' #Employee's email 
print(f'Email: {email}') # output: Employee's email 

at_position = email.find('@') # Find the position of @ in employee email 
print(f'Position of @: {at_position}') # Output: position of @ sign in email  

username = email[:at_position] # Slicing employees email up to the @ position 
print(f'Username: {username}') # Output: Result of slicing employee email up to @ position to give username 

has_at = '@' in email # Checking employee email to see if @ is present 
print(f'Has @ symbol: {has_at}') # output: Returns true of false after checking for @ symbol in email 

has_com = '.com' in email # Checking employee email to see if .com is present
print(f'Has .com: {has_com}') #Output: Returns true of false after checking for .com symbol in email 

messy_name = '  sARaH dAVis  ' # Employees name untidy form 
print(f"Original name: '{messy_name}'") # Output: Employees name in untidy form 

clean_name = messy_name.strip().title() # Removing leading and trailing space and capitalising first letter of words 
print(f"Cleaned name: '{clean_name}'") # Employees name cleaned with leading and trailing space removed and first letter of words capitalised 

messy_email = '  SARAH.DAVIS@COMPANY.COM  ' #Employees email in untidy form 
clean_email = messy_email.strip().lower() #Removing leading and trailing space and lowercasing employee email 
print(f"Original email: '{messy_email}'") #Output: Employees email in untidy form 
print(f"Cleaned email: '{clean_email}'") #Output: Employees email clean with leading and trailing space removed and in lowercase 

name_badge = clean_name.upper() #Employees name badge all in upper case 
print(f'Name badge: {name_badge}') #Output: Employees name badge in uppercase 

at_pos = clean_email.find('@') #Find the position of @ in employee email 
email_user = clean_email[:at_pos] #Slicing employees email up to the @ position

print(f'Email: {clean_email}') #Output: Employee email 
print(f'Username: {email_user}') #Output: Result of slicing employee email up to @ to give employee user name 

display_name = email_user.replace('.', ' ').title() #Employee display name replacing the full stop with a space 
print(f'Display name: {display_name}') #Output: Employee display name with space rather than full stop

phone = '123-456-7890' #Storing phone number in variable 
phone_clean = phone.replace('-', '') # Replacing the dash in phone number so there is no space between numbers 
print(f'Phone with dashes: {phone}') #Output: Number with dashes 
print(f'Phone without dashes: {phone_clean}') #Output: Number without dashes 

full_address = '123 Main Street, Springfield, IL' #Storing address in variable 
address_parts = full_address.split(', ') #Splitting address by commas and spaces 
print(f'Address parts: {address_parts}') # Output: Address split with commas and spaces 

rejoined = ' | '.join(address_parts) #Rejoining the address by | symbol 
print(f'Rejoined: {rejoined}') #Output: Rejoined address by | symbol 

employee_code = 'EMP-2024-SD' #Storing employee code in variable 
starts_with_emp = employee_code.startswith('EMP') #Checking to see if the employee code starts with EMP 
ends_with_com = clean_email.endswith('.com') #Checking to see if the employee email ends with .com

print(f'Code: {employee_code}') #Output: Employee code 
print(f'Starts with EMP: {starts_with_emp}') #Output: Result of checking if employee code starts with emp as true of false 
print(f'Clean email: {clean_email}') #Output: Clean employee email 
print(f'Ends with .com: {ends_with_com}') #Output: Result of checking if employee emails ending with .com as true of false 

dot_count = clean_email.count('.') #Counting how many dots in email 
dash_count = employee_code.count('-')#Counting how many dashes in email 

print(f'Dots in email: {dot_count}') #Output: How many dots in email as a number 
print(f'Dashes in code: {dash_count}')#Output: how many dashes in email as a number 