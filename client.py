from tkinter import *
from tkinter import messagebox
import requests
import json

def namesValid(fname, lname):
	return (all([1 if ch.isalpha() else 0 for ch in fname+lname]) and len(fname) > 0 and len(lname) > 0)

def phoneNumberValid(phoneNumber):
	return (all([1 if num.isdigit() else 0 for num in phoneNumber]) and len(phoneNumber) == 10)

def emailAddressValid(emailAddress):
	arr = emailAddress.split('@')
	if len(arr) == 2:
		arr2 = arr[1].split('.')
		if len(arr2) == 2:
			if all([1 if ch.isalnum() else 0 for ch in arr[0]]):
				if all([1 if ch.isalpha() else 0 for ch in arr2[1]]):
					return True
	return False

def submit():
	valid = namesValid(firstNameEntry.get(), lastNameEntry.get())
	valid = valid and phoneNumberValid(phoneNumberEntry.get())
	valid = valid and emailAddressValid(emailEntry.get())
	valid = valid and (emailPrefState.get() != phonePrefState.get())
	valid = valid and optionMenuSelection.get()

	if valid:
		obj = {}
		for u, v in zip(("First Name", "Last Name", "Email", "Phone Number"), 
			(firstNameEntry.get(), lastNameEntry.get(), 
				emailEntry.get(), phoneNumberEntry.get())):
			obj[u] = v

		obj["Preferred"] = "Email" if emailPrefState.get() else "Phone"
		obj["Supervisor"] = optionMenuSelection.get()

		response = requests.post("http://localhost:8000/api/submit", data=obj)
		print(response)
	else:
		messagebox.showerror(title="Error", message="Error in form")


top = Tk()
top.geometry("600x800")
top.title("Register For Notifications")
Label(text="Notification Form").pack()
Label(text="First Name").pack()
firstNameEntry = Entry()
firstNameEntry.pack()

Label(text="Last Name").pack()
lastNameEntry = Entry()
lastNameEntry.pack()

Label(text="Email").pack()
emailEntry = Entry()
emailEntry.pack()

Label(text="Phone Number").pack()
phoneNumberEntry = Entry()
phoneNumberEntry.pack()

emailPrefState = IntVar()
emailPref = Checkbutton(text="I prefer to be notified by email", variable=emailPrefState)
emailPref.pack()

phonePrefState = IntVar()
phonePref = Checkbutton(text="I prefer to be notified by phone", variable=phonePrefState)
phonePref.pack()

Label(text="Supervisor").pack()
data = requests.get("http://localhost:8000/api/supervisors")
data = data.json()
supervisorList = [data[str(i)] for i in range(0, len(data))]
optionMenuSelection = StringVar()
optionMenu = OptionMenu(top, optionMenuSelection, *supervisorList)
optionMenu.pack()

submitButton = Button(text="SUBMIT", command=submit)
submitButton.pack()

top.mainloop()
