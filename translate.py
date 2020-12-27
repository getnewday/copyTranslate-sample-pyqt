# https://translate.google.cn/?sl=en&tl=zh-CN&text=believer&op=translate
# https://translate.google.cn/_/TranslateWebserverUi/data/batchexecute?rpcids=MkEWBc&f.sid=6944461514335076575&bl=boq_translate-webserver_20201220.16_p1&hl=zh-CN&soc-app=1&soc-platform=1&soc-device=1&_reqid=3059410&rt=c

import requests
import re
import time


class Translate():
    def __init__(self):
        self.curTime = time.localtime(time.time())
        self.curTimeFormat = str(self.curTime.tm_year) + str(self.curTime.tm_mon) + str(self.curTime.tm_mday)+'.'+str(self.curTime.tm_hour)
        self.headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            # "accept-language": "en,zh-CN;q=0.9,zh;q=0.8",
            "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
        }
        # 请求url
        self.url = "https://translate.google.cn/_/TranslateWebserverUi/data/batchexecute?rpcids=MkEWBc&f.sid=6944461514335076575&bl=boq_translate-webserver_{}_p1&hl=zh-CN&soc-app=1&soc-platform=1&soc-device=1&_reqid=3059410&rt=c".format(
            self.curTimeFormat)

    def translated_content(self,text,target_language):
        from_data = {
            "f.req": r"""[[["MkEWBc","[[\"{}\",\"auto\",\"{}\",true],[null]]",null,"generic"]]]""".format(text,target_language)
        }
        try:
            print(text)
            r = requests.post(self.url, headers=self.headers, data=from_data, timeout=60)
            print(r.text)
            if r.status_code == 200:
                # 正则匹配结果
                response = re.findall(r',\[\[\\"(.*?)\\",\[\\', r.text)
                if response:
                    response = response[0]
                else:
                    response = re.findall(r',\[\[\\"(.*?)\\"]', r.text)
                    if response:
                        response = response[0]
                return response
        except Exception as e:
            print(e)
            return False

# # for i in ['en', 'zh', 'fr', 'ja', 'de']:
if __name__ == '__main__':
    t = Translate()
    for i in ['zh']:
        response = t.translated_content("who are you", i)
        print(response)