#Break and continue:
#Break: breaks the whole block of code:
stds = ['rina', 'tina', 'mina', 'hina', 'lina', 'bina', 'dina']
for std in stds:
    if std == 'hina':
        break #Everything after hina along with hina will not be printed
    print(std)

for std in stds:
    if std == 'lina':
        continue #Only lina will be skipped rest of the elements will be printed
    print(std)