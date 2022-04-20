# Number treasure

#copyright 

copyright = ('Copy right of this code has Abdirizak abdullahi hussein')

#User information
Name1 = input('Enter your name: ')
Pin = input('Enter a new pin: ')
print()
print('Welcome {} to numbers treasure enjoy!'.format(Name1))
print(':-Note that pin {} will ask you some places for  security purpose'.format(Pin))
print()

# Dictionary to store contacts
contact = {}

# function for slowprint()
import time
import sys

def slowprint(h):
	for v in h + '\n':
		sys.stdout.write(v)
		sys.stdout.flush()
		time.sleep(7./10)

#function for display contacts
def Display_contacts():
	print("Name \t\t Phone")
	for key in contact:
		print('{} \t\t {}'.format(key, contact.get(key)))

con = True 

while con == True:
	print('1.Add contact \n2.Search contact \n3.Edit exist contact \n4.Delete contact \n5.How many contact)s are there ? \n6.Display contacts \n7.Reset all (Delete all info)')
	choice = input()
	if choice == '1':
		print()
		Name = input('Enter the name of the contact: ')
		Phone = input('Enter the phone of the contact: ')
		contact[Name] = Phone
		print()
		print('Saved Succesfully')
		print(Name , ':', Phone)
	elif choice == '2':
		print()
		print('Search...........')
		sea = input('Enter the name of the contact: ')
		if not contact:
			print()
			print('Empty contact')
			print()
		elif sea in contact:
			print()
			print('view........')
			print(sea, ':',  contact.get(sea))
			print()
		else:
			print()
			print('Contact not found ')
			print()
	elif choice == '3':
		print()
		ed = input('Enter the name of the contact:')
		if not contact:
			print()
			print('Empty contact')
			print()
		elif ed in contact:
			new = input('Enter the new_number: ')
			contact[ed] = new
			print()
			print('Updated')
			print()
		else:
			print("contact not found !")
	elif choice == '4':
		print()
		Del = input('Enter the name of the contact')
		if not contact:
			print("Empty contact")
		elif Del in contact:
			contact.pop(Del)
			print('Deleted!')
		else:
			print('Contact not found!')
	elif choice == '5':
		if len(contact) == 1:
			print(len(contact), "contact")
		elif len(contact) > 1:
			print(len(contact), "contacts")
		else:
			print("Empty contact")
	elif choice == '6':
		Display_contacts()
	elif choice == '0':
		con = False
		print('See you later {} thank you for using my program'.format(Name1))
	elif choice == '7':
		print('To identify that you are {} Enter the pin'.format(Name1))
		pin = input('Enter the pin: ')
		slowprint('_____Reset all _____')
		slowprint('Satarting...................')
		slowprint('Refreshing-------------------------------------*')
		slowprint('Wait a second.......')
		print("Finished")
		contact.clear()
		print()
		#User information
		Name1 = input('Enter your name: ')
		Pin = input('Enter a new pin: ')
		print()
		print('Welcome {} to numbers treasure enjoy!'.format(Name1))
		print(':-Note that pin {} will ask you some places for  security purpose'.format(Pin))
		print()