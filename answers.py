import csv


file = open('books-en.csv')
reader = csv.DictReader(file, delimiter = ";")


result = {}
for row in reader:
    for key, info in row.items():
        result.setdefault(key, []).append(info)


file.close()


count = 0
for items in result['Book-Title']:
    if len(items) > 30:
        count += 1


print(f"Answer to first question: {count}")


author = input("Plese, type the author's name: ")
indexes = 0


for authors in result['Book-Author']:
    if authors == author:
        number = float(result['Price'][indexes].replace(",","."))
        if int(number) >= 150:
            print(
                result['Book-Title'][indexes], 
                f"({result['Year-Of-Publication'][indexes]})"
                )

    indexes += 1


with open('For answer 3.txt','a') as new_file:
    for num in range(20):
        new_file.write(f"{num+1}) {result['Book-Author'][num]}."
            f"{result['Book-Title'][num]} - {result['Year-Of-Publication'][num]}\n"
            )


print("\x1b[48;5;31m The Publishing houses \x1b[0m")
publisher = set(result['Publisher'])
print(*publisher, sep = ", ")


print("\x1b[48;5;31m Top 20 popular book \x1b[0m")
download = []

for load in result['Downloads']:
    download.append(int(load))


popular = max(download)
flag = 0
for ind_elem in range(len(download)):
    if flag == 20:
        break

    if  popular == download[ind_elem]:
        flag += 1
        print(result['Book-Title'][ind_elem])


