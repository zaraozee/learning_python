huruf = input("Masukkan sebuah huruf dari A-Z: ")
huruf = huruf.lower()

# Menentukan huruf termasuk vokal, konsonan, atau bukan huruf
if huruf.isalpha():  
    if huruf in ['a', 'e', 'i', 'o', 'u']:
        print("Huruf yang diinput adalah vokal.")
    else:
        print("Huruf yang diinput adalah konsonan.")
else:
    print("Input bukan berupa huruf.")

kalimat = """Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Maecenas porttitor congue massa. Fusce 
posuere, magna sed pulvinar ultricies, purus lectus malesuada libero, sit amet commodo magna eros 
quis urna. 
Nunc viverra imperdiet enim. Fusce est. Vivamus a tellus. 
Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin 
pharetra nonummy pede. Mauris et orci."""
print(kalimat)
