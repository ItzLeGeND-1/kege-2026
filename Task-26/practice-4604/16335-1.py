with open(r'../files/26_16335.txt') as file:
    N=int(file.readline())
    forms=[int(i)for i in file]
forms=sorted(forms,reverse=True)
all_forms=[forms[0]]
for form in forms:
    if all_forms[-1]-form>=4:
        all_forms.append(form)
print(len(all_forms),all_forms[-1])