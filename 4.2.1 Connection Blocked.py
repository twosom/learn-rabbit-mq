import rabbitpy
from rabbitpy import Connection

connection: Connection = rabbitpy.Connection()
print('Channel is Blocked? %s' % connection.blocked)
