from configparser import ConfigParser

# .ini配置文件

cfg = ConfigParser()
cfg.read('e:/mysql.ini')
print(cfg.sections())
print(cfg.has_section('mysqld'))

print(cfg.items('mysqld'))
for k, v in cfg.items():
    print(k, type(v))

tmp = cfg.get('mysqld', 'port')
print(type(tmp), tmp)
print(cfg.get('mysqld', 'a'))
print(cfg.get('mysqld', 'magedu', fallback='python'))

tmp = cfg.getint('mysqld', 'port')
print(type(tmp), tmp)

if cfg.has_section('test'):
    cfg.remove_section('test')

cfg.add_section('test')
cfg.set('test', 'test1', '1')
cfg.set('test', 'test2', '2')

with open('e:/mysql.ini', 'w') as f:
    cfg.write(f)

print(cfg.getint('test', 'test2'))

cfg.remove_option('test', 'test2')
