sampleDict = {'car':10,'bike':20,'taxi':30, 'bus': 40}

print(f'The sample dictionary: {sampleDict}')

key = input('Enter a key you want to remove from dictionary: ')

if key in sampleDict: 
    del sampleDict[key]
    print(f"The key '{key}' has been removed!!")
else:
    print('The provided key is not found!!')    

print(f'The dictionary after key removal: {sampleDict}')