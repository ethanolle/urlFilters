import re
import os
import psutil




lines_seen = set()
urlCounter = 0;
lastUrl = ""
url = ""

#dl files from the repository
#point to them
#how do we send it in array?, in lines?


with open("cdx-00200") as file:
    for line in file:
        urls = re.findall(r'https?://\S*?\.il\b', line)
        if lastUrl != urls:
             if urlCounter > 100:
                 lines_seen.clear()
                 # send url_extract.txt to the db
                 os.remove("url_extract.txt")
                 urlCounter = 0



        with open("url_extract.txt", "a") as fw:
            for url in urls:
                if lastUrl != url:
                    lastUrl = url
                    if lastUrl not in lines_seen:
                        lines_seen.add(lastUrl)
                        fw.write("%s\n" % lastUrl)
                        urlCounter +=1
                        print(lastUrl)
                        print(urlCounter)





process = psutil.Process(os.getpid())
print(process.memory_info().rss)
