url = input("Paste a URL: ")
clean_url = url.lower().strip()
# print if the URL starts with https
#print("Starts with https:", clean_url.startswith("https"))
# print the domain of the URL
print("Domain:", clean_url.split("//")[-1].split("/")[0])

