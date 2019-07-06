import requests
default_name = 'Иванов Иван Иванович'
name = input('Enter a name to find in list (default name is {}): '.format(default_name))
default_link = 'https://cabinet.spbu.ru/Lists/1k_EntryLists/list_a26329cf-20a7-4899-9f25-0c4ef0d1dcaa.html'
link = input('Enter a link to list(default link is {}): '.format(default_link))
if name == '':
    name = default_name
if link == '':
    link = default_link
response = requests.get(link)


original_attestat_count = 0
copy_attestat_count = 0

for i in response.content.decode().replace('<td>', '').replace('</td>', '').split('\n'):
    if 'Направление' in i:
        print('Direction: {}'.format(i[i.find('/b>')+3:-7]))
    if 'Количество поданных заявлений' in i:
        print('All peple: {}'.format(i[i.find('/b>')+3:-7]))
    if 'КЦП по конкурсу' in i:
        print('Budget places: {}'.format(i[i.find('/b>')+3:-7]))
    if 'Время последнего обновления' in i:
        print('Last list update time: {}'.format(i[31:-5:]))
    if 'Да'==i.strip():
        original_attestat_count+=1
    if 'Нет'==i.strip():
        copy_attestat_count+=1
    if name in i:
        print(i[i.find('/a>')+3:])
        print('Original attesttats before you: {}'.format(original_attestat_count))
        print('Copy of attesttats before you: {}'.format(copy_attestat_count))
        print('People before you: {}'.format(original_attestat_count+copy_attestat_count))


print('Total original attestats: {}'.format(original_attestat_count))
print('Total people finded (for check): {}'.format(original_attestat_count+copy_attestat_count))
