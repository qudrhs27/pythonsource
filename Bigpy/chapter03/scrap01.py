import sys
import io
import urllib.request as dw

imgUrl = "htts://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDA3MTdfMTgw%2FMDAxNTk0oTYzOTUwOTYw.IKn6Jj8o-SoRTbZI3c9fwfqbRlxp8Kn6mm2mrUZj2Vcg.g-mWpamKt2jzpt0gw3B3je"
htmlURL = "http://google.com"

# 방법 1
# savePath1 = "C:/source/pythonsource/Bigpy/Py_scrap/imgtest1.jpg"
# savePath2 = "C:/source/pythonsource/Bigpy/Py_scrap/index.html"

# dw.urlretrieve(imgUrl, savePath1)
# dw.urlretrieve(htmlURL, savePath2)

f1 = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlURL).read()

savePath1 = "C:/source/pythonsource/Bigpy/Py_scrap/imgtest1.jpg"
savePath2 = "C:/source/pythonsource/Bigpy/Py_scrap/index.html"

# # 방법2
# saveFile1 = open(savePath1, 'wb')
# saveFile1.write(f1)
# saveFile1.close()

# 방법3
with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)

print("save 완료")