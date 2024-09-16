l = ["raju","shrikant","shiva","anjali"]
for i in l:
    print(f"Inviting for dinner: {i}")
print("Shiva can't come")
l.update("shiva","sagar")
# l.insert(2,"sagar")
l.append("sagar")
print("Updated list:")
for i in l:
    print(f"Inviting for dinner: {i}")