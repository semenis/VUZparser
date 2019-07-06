import config
import requests
import json

default_name = config.name
name = input('Enter a name to find in list (name in config is {}): '.format(default_name))
if name == '':
    name = default_name

default_links = config.miet_links
links = [input('Enter links to find (links in config is {}): '.format(' '.join(default_links))).split(' ')]
if links == [['']]:
    links = default_links

for link in links:
    print(link)
    #stud = dict() #Костыль переводить json в dict, но мы фильтруенм данные, так что норм
    stud = []
    response = requests.get(link)
    spis = json.loads(response.text)
    for i in spis[0]['students']:
        #print(i['name'], i['surname'], i['mname'], i['sum'], i['original_doc'], i['priority'])
        stud.append(([i['surname']+' '+i['name']+' '+i['mname']],[i['sum'], i['original_doc'], i['priority']]))
    stud.sort(key=lambda i: (i[1][0], i[1][2], i[1][1]), reverse=True)
    print('All people: {}'.format(len(stud)))

    original_attestat_count = 0
    copy_attestat_count = 0
    f_prior_count = 0
    s_prior_count = 0
    t_prior_count = 0
    orig_and_f_prior_count = 0
    for i, j in enumerate(stud):
        if j[0][0] == name:
            print("You are {}'st in list".format(str(i)))
            print("Original attestats before you: {}".format(original_attestat_count))
            print("Copy of attestat before you: {}".format(copy_attestat_count))
            print("With first prioretet before you: {}".format(f_prior_count))
            print("With second prioretet before you: {}".format(s_prior_count))
            print("With third prioretet before you: {}".format(t_prior_count))
            print("Original attestat and 1'st prior: {}".format(orig_and_f_prior_count))
        if j[1][1]:
            original_attestat_count+=1
            if j[1][2]==1:
                orig_and_f_prior_count+=1
        elif not j[1][1]:
            copy_attestat_count+=1
        if j[1][2]==1:
            f_prior_count+=1
        elif j[1][2]==2:
            s_prior_count+=1
        elif j[1][2]==3:
            t_prior_count+=1
    print("In all list:")
    print("Original attestats: {}".format(original_attestat_count))
    print("Copy of attestat: {}".format(copy_attestat_count))
    print("With first prioretet: {}".format(f_prior_count))
    print("With second prioretet: {}".format(s_prior_count))
    print("With third prioretet: {}".format(t_prior_count))
    print("Original attestat: {}".format(orig_and_f_prior_count))