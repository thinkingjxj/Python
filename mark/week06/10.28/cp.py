from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('e:/mysql.ini')   # 读完后，已经装到自己内部去了
print(cfg.sections())           # 字典section=option   而option中又是字典，字典套字典
for section in cfg.sections():
    for option in cfg.options(section):
        print(section, option)
    # for k, v in cfg.items(section):
    #     print(k, v)
print('@@@@@@@@@@@@@@')
if not cfg.has_section('test'):
    cfg.add_section('test')
cfg.set('test', 'test1', '123')
cfg.set('test', 'test2', 'abc')

# with open('e:/mysql.ini', 'w') as f:
#     cfg.write(f)
print('@@@@@@@@@@@@@@')
for x in cfg.items():
    print(x)             # （section,option）组成的二元组

print('@@@@@@@@@@@@@@')
for k, v in cfg.items():
    print(k, type(v))           # 解构
    print(k, v)

print('@@@@@@@@@@@@@@')
tmp = cfg.get('mysqld', 'port')
print(tmp, type(tmp))
print(cfg.get('mysqld', 'datadir'))
print(cfg.get('mysqld', 'a'))



# with open('e:/mysql.ini') as f:
#     print(f)
#     print(f.read())
