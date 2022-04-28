dictionary={}
poll = True

while poll:
    name=input('\tEnter your name\n')
    mountain=input('\tWhats your favorit mountain\n')
    dictionary[name]=mountain

    repit=input("\tSecond person?(Y/N)\n")
    if repit == 'n':
        poll=False

for name,mountain in dictionary.items():
    print(f'\t{name.title()} like to ride {mountain.title()}')