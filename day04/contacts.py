contacts =[]

while True:
    print('\n1. Add \n2. List \n3. Search \n4. Delete \n5. Exit')
    try:
        choice = int(input('Enter your choice:'))
    except ValueError:
        print('Error:Please enter a number between 1 and 5.')
        continue
    if choice == 1:
        name=input('Enter name: ')
        phone=input('Enter phone: ')
        email=input('Enter email: ')
        contacts.append({'name': name,'phone': phone,'email': email})
        print(f'Contact {name} & other details added successfully.')
    elif choice == 2:
        if contacts:
            print('List of contacts:')
            for i,n in enumerate(contacts,start=1):
                print(f'{i}. {n['name']} | {n['phone']} | {n['email']}')
        else:
            print('No contacts found.')
    elif choice == 3:
        search_val=input('Enter name to search: ')
        found=[c for c in contacts if search_val.lower() in c['name'].lower()]
        if found:
            print('search found:')
            for i,n in enumerate(found,start=1):
                print(f'{i}. {n['name']} | {n['phone']} | {n['email']}')
        else:
            print('No contacts found with that name.')
    elif choice == 4:
        delete_val=input('Enter name to delete: ')
        before=len(contacts)
        contacts =[c for c in contacts if delete_val.lower() != c['name'].lower()]
        if len(contacts)<before:
            print(f'Contact {delete_val} deleted successfully.')
        else:
            print('Contact not found.')
    elif choice == 5:
        print('Exiting the program.')
        break
