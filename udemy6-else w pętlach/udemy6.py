instruction = ['say hello','say how are you','abort','ask for money','say thank you','say bye']
instructionApproved = []

for instr in instruction:
    print('Adding instuction:', instr)
    instructionApproved.append(instr)
    if instr == 'abort':
        print("Aborting!!!")
        instructionApproved.clear()
        break
else:
    print('Following actions will be taken:', instructionApproved)
print('-----------------------------')
instructionApproved.clear()
i=0
while i < len(instruction):
    print('Adding instuction:', instruction[i])
    instructionApproved.append(instruction[i])
    if instruction[i] == 'abort':
        print("Aborting!!!")
        instructionApproved.clear()
        break
    i+=1
else:
    print('Following actions will be taken:', instructionApproved)
print('---------------------------------------------------------------')
import urllib.request
import os

data_dir = 'c:/temp'
pages = [
    {'name': 'mobilo', 'url': 'http://www.mobilo24.eu/'},
    {'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/'},
    {'name': 'kursy', 'url': 'http://www.kursyonline24.eu/'}]

for page in pages:

    try:
        file_name = "{}.html".format(page["name"])
        path = os.path.join(data_dir, file_name)

        print("Processing: {}  => {} ...".format(page["url"], file_name))
        urllib.request.urlretrieve(page["url"], path)
        print('...done')

    except:
        print('FAILURE processing web page: {}'.format(page["name"]))
        print('Stopping the process!')
        break

else:
    print('All pages downloaded successfully!!!')