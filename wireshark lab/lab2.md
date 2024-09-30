## lab2_HTTP

### The Basic HTTP GET/response interaction

打开wireshark，过滤http

打开链接：http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file1.html

截获报文，打开报文

![image-20240930114733341](lab2/image-20240930114733341.png)

回答问题：

1. Is your browser running HTTP version 1.0 or 1.1?What version of HTTP is the  server running? 

查看请求行，均为1.1

2. What languages (if any) does your browser indicate that it can accept to the  server? 

查看accept_language 首部行：

![image-20240930115346620](lab2/image-20240930115346620.png)

3. What is the IP address of your computer? Of the gaia.cs.umass.edu server?

查看网络层，src代表我电脑的ip，dst代表gaia...：

![image-20240930115514209](lab2/image-20240930115514209.png)

4. What is the status code returned from the server to your browser?

200

When was the HTML file that you are retrieving last modified at the server?

![image-20240930115725623](lab2/image-20240930115725623.png)

5. How many bytes of content are being returned to your browser?

![image-20240930115744188](lab2/image-20240930115744188.png)

6. By inspecting the raw data in the packet content window, do you see any headers  within the data that are not displayed in the packet-listing window? If so, name  one

没有找到。

### The HTTP CONDITIONAL GET/response interaction

8. Inspect the contents of the first HTTP GET request from your browser to the  server. Do you see an “IF-MODIFIED-SINCE” line in the HTTP GET? 

没看到

8. Inspect the contents of the server response. Did the server explicitly return the  contents of the file? How can you tell? 

是的。有许多关于消息的首部行。并且status code为200。文件本身也被传输过来。

![image-20240930164629023](lab2/image-20240930164629023.png)

8.  Now inspect the contents of the second HTTP GET request from your browser to  the server. Do you see an “IF-MODIFIED-SINCE:” line in the HTTP GET? If  so, what information follows the “IF-MODIFIED-SINCE:” header?

是的。发送时间。

8.  What is the HTTP status code and phrase returned from the server in response to  this second HTTP GET? Did the server explicitly return the contents of the file?  Explain

304.没有，因为刷新时间没有超过一分钟。服务器一分钟修改一次文件。

![image-20240930165036603](lab2/image-20240930165036603.png)

###  Retrieving Long Documents

12. How many HTTP GET request messages did your browser send? Which packet  number in the trace contains the GET message for the Bill or Rights? 

一个。1352

12.  Which packet number in the trace contains the status code and phrase associated  with the response to the HTTP GET request? 

1594

12. What is the status code and phrase in the response?

200 

![image-20240930171715356](lab2/image-20240930171715356.png)

12.  How many data-containing TCP segments were needed to carry the single HTTP  response and the text of the Bill of Rights?

4个

![image-20240930172226690](lab2/image-20240930172226690.png)

### HTML Documents with Embedded Objects

16. How many HTTP GET request messages did your browser send? To which  Internet addresses were these GET requests sent? 

3个，其中10.199.129.41是源。

![image-20240930173603973](lab2/image-20240930173603973.png)

17. Can you tell whether your browser downloaded the two images serially, or  whether they were downloaded from the two web sites in parallel? Explain

不能。尽管收到response的日期不同，但是并不能判断是否顺序，因为照片在不同服务器，花费的时间不同。

###  HTTP Authentication

网址：http://gaia.cs.umass.edu/wireshark-labs/protected_pages/HTTP-wireshark-file5.html

用户名：wireshark-students

密码：network

http身份验证：[HTTP 身份验证 - HTTP | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Authentication)

18. What is the server’s response (status code and phrase) in response to the initial  HTTP GET message from your browser? 

HTTP/1.1 401 Unauthorized\r\n

18. When your browser’s sends the HTTP GET message for the second time, what  new field is included in the HTTP GET message?

Authorization: Basic d2lyZXNoYXJrLXN0dWRlbnRzOm5ldHdvcms=\r\n

解密：[Base64 Online - base64 decode and encode (motobit.com)](https://www.motobit.com/util/base64-decoder-encoder.asp)

![image-20240930194752033](lab2/image-20240930194752033.png)

说明基本的http不安全。