from __future__ import absolute_import, unicode_literals
from YAQueueProject.tasks import inc

if __name__ == '__main__':
    for i in range(100):
        r = inc.delay(i)
        print(r.get())
