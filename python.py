#coding=utf-8
import httplib
import threading


def jb51():
	url = "http://www.jb51.net/article/66763.htm"
	conn = httplib.HTTPConnection("www.jb51.net")
	conn.request(method="GET",url=url) 
	response = conn.getresponse()
	res= response.status
	print res
	
threads=[]
for i in range(10):
	t=threading.Thread(target=jb51,args=())
     #�Ѵ������̼߳����߳���	 
	threads.append(t)  

     
if __name__ == '__main__':
   #�����߳�  
   for i in threads:  
        i.start()  
   #keep thread  
   for i in threads:  
        i.join()