import csv

with open("data_banknote.csv","r") as csv_file:
    file_reader=csv.DictReader(csv_file)

    with open("new_names2.csv","w") as new_file:
        fieldnames=["DA","OK","SALUT","OLA","OUI"]
        csv_writer=csv.DictWriter(new_file,fieldnames=fieldnames,delimiter="\t")

        csv_writer.writeheader()
        for line in file_reader:
            csv_writer.writerow(line)











