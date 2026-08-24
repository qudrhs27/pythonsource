import sys
import io
import urllib.request as dw

imgUrl = "htts://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDA3MTdfMTgw%2FMDAxNTk0oTYzOTUwOTYw.IKn6Jj8o-SoRTbZI3c9fwfqbRlxp8Kn6mm2mrUZj2Vcg.g-mWpamKt2jzpt0gw3B3je"
htmlURL = "http://google.com"

savePath1 = "C:/source/pythonsource/Bigpy/Py_scrap/imgtest1.jpg"
savePath2 = "C:/source/pythonsource/Bigpy/Py_scrap/index.html"

dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlURL, savePath2)