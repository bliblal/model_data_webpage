import csv

rows=list()

fname='output.csv'
hfhandle = open("htmloutput.html", 'a+')

strttag="<html> <head><style>table, th, td {border: 1px solid black;td {table-layout: fixed; width: 200px; height: 50px;vertical-align: bottom;}</style></head><body><table><tr><th>Sr.</th><th>File</th><th>Truth</th><th>Inference</th></tr>"
endtag = "</table></html>"

hfhandle.write(strttag)


with open(fname,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    fields = next(csvreader)
    for row in csvreader:
        img="<img src=\"./"+row[1]+"\" width=\"70%\" height=\"70%\" >"
        htmlwrt= "<tr><td>"+row[0]+"</td><td>"+img +"</td><td>"+row[2]+"</td><td>"+row[3]+"</td></tr>"
        hfhandle.write(htmlwrt)
        hfhandle.write("\n")
    

    
    hfhandle.write(htmlwrt)
    
hfhandle.write(endtag)
hfhandle.close()
print(row[1])
print(img)