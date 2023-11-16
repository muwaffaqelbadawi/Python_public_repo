list_of_items = ["mobile", "power bank", "headphone", "battery"]

url = "<ul>\n"
for stuff in list_of_items:
    url += f"\t<li>{stuff}</li>\n"

url += "</ul>"

print(url)
