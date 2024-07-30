unconfirmed_users = ["John macey", "Steve erwin", "Bob dylan"]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop(0)
    print("Your account is being confirmed " + current_user.title())
    confirmed_users.append(current_user.title())
print(confirmed_users)
