import threading
global_data=threading.local()
x = 10
def app():
    global x
    x+=global_data.num
def action():
    global_data.num=0
    for i in range(1000000):
        global_data.num += 1
        global_data.num -= 1
    app()

x = int(input())
thread = []
for i in range(10):
    thread.append(threading.Thread(target = action))
    thread[i].start()
for i in range(10):
    thread[i].join()
print(x)
