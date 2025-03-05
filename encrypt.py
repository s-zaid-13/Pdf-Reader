from PyPDF2 import PdfWriter
fileName=input("Enter a file name: ")
writer=PdfWriter()
try:
    writer.append(fileName)
except FileNotFoundError:
    print(f"Error! {fileName} not found.\nEnsure File must be in Current Working directory.")
    exit()
password=input("Enter a new password: ")
writer.encrypt(password)
with open("encrypt.pdf","wb") as file:
    writer.write(file)
print("Encryption successful. The file has been saved as 'encrypt.pdf.'")