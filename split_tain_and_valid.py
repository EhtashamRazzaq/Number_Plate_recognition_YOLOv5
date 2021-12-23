import os
import shutil
maindir = os.listdir('Annotated_data/')
try:
    os.mkdir('Dataset/')
except:
    pass
try:
    os.mkdir('Dataset/images/')
except:
    pass
try:
    os.mkdir('Dataset/labels/')
except:
    pass
try:
    os.mkdir('Dataset/images/Train/')
except:
    pass
try:
    os.mkdir('Dataset/images/Valid/')
except:
    pass
try:
    os.mkdir('Dataset/labels/Train/')
except:
    pass
try:
    os.mkdir('Dataset/labels/Valid/')
except:
    pass
j = 0
for i in maindir:
    OriginalName = os.path.splitext(i)[0]
    print(OriginalName)
    extensionsss = os.path.splitext(i)[1]
    print(extensionsss)
    if(extensionsss == '.jpg' or extensionsss == '.png' or extensionsss == '.PNG' or extensionsss == '.jpeg' ):
        print(OriginalName+extensionsss)
        try:
            if(j%5):
                shutil.copy2(f'Annotated_data/{OriginalName+extensionsss}',f'Dataset/images/Train/{OriginalName+extensionsss}')
                shutil.copy2(f'Annotated_data/{OriginalName}.txt',f'Dataset/labels/Train/{OriginalName}.txt')
            else:
                shutil.copy2(f'Annotated_data/{OriginalName+extensionsss}',f'Dataset/images/Valid/{OriginalName+extensionsss}')
                shutil.copy2(f'Annotated_data/{OriginalName}.txt',f'Dataset/labels/Valid/{OriginalName}.txt')
        except Exception as e:
            print(e)
            pass
    else:
        pass

    j+=1