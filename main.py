from tabula.io import read_pdf

table = read_pdf("weather.pdf", pages=1)
# print(table)
table[0].to_csv("output.csv", index=None)