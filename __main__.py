from belissa.Controller import Controller

if __name__ == '__main__':
    program = Controller()
    program.main()

# file_name = 'files/config.json'
# data_json = None
# with open(file_name, 'r', encoding='utf8') as archivo:
#     data_json = json.load(archivo)
#
# print(data_json)
# data_json['ip'] = 411
#
# print(data_json)
#
#
# with open(file_name, 'w', encoding='utf8') as archivo:
#     write_json = json.dumps(data_json, indent=4)
#     archivo.write(write_json)