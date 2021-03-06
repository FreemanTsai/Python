''' 保持順序 '''
#!/usr/bin/python
import ConfigParser
config_one = ConfigParser.RawConfigParser()
config_one.read('/tmp/test.ini')
config_two = ConfigParser.RawConfigParser()
order_list=['a','b','c','d','e']

config_two.add_section('global')
for i in order_list:
    config_two.set('global', i, config_one.get('global',i))
with open('/tmp/test.ini','w+') as fd:
    config_two.write(fd)

    
### you can create a file "/tmp/test.ini" as following: ###
[global]
b = 2
a = 1
c = 3
e = 5
d = 4
