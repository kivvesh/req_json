import requests as req

'''def get_json():
    url = 'https://chains.cosmos.directory/akash'
    json = req.get(url)
    with open('test.json','w',encoding='utf-8') as file:
        file.write(json.text)'''

def get_json(num_block):
    url = 'https://chains.cosmos.directory/akash'
    text = req.get(url)
    dic = dict(text.json())

    '''for key,value in dic.items():
        print(f'{key} - {value}')
    '''
    try:
        return(dic['chain'][num_block])
    except:
        return('не найдено')
    '''
    csv_data = generate_csv(dic)
    with open('1.csv','w',encoding='utf-8') as f:
        f.write(csv_data)
'''


'''def generate_csv(data):
    csv_columns = data.keys()

    csv_data = ",".join(csv_columns) + "\n"

    new_row = list()
    for col in csv_columns:
        new_row.append(str(data[col]))

    csv_data += ",".join(new_row) + "\n"

    return csv_data'''

if __name__ == '__main__':
    print(get_json(input('введите номер блока - ')))

