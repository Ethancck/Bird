import os
import concurrent.futures
from core.log import logger
import requests
import sys
from readability import Document
from core.banner import _init_stdout
from core.cmdline import args
from core.const import default_header
logger=logger()
flag=args.flag
def check(url):
    try:
        if flag:
            # print(flag)
            resp = requests.get(url.strip(), headers=default_header,allow_redirects=True,timeout=3)
            status = resp.status_code
            resp.encoding = 'utf-8'
            title = Document(resp.content).title()
            lan=resp.headers.get("X-Powered-By")
            server=resp.headers.get("Server")
            if title=='[no-title]':
                if len(resp.content)>60:
                    if "Whitelabel" in resp.text:
                        title='Whitelabel Error Page | Sprint Boot'
                    else:
                        title='[no-title]'
                else:
                    title=resp.content.decode('utf-8')
            if flag in resp.text or flag in title or flag in lan or flag in server:
                logger.INFO("url:{0}   title:{1} code: {2}".format(url, title, status))
                if args.report:
                    with open(args.report, "a+", encoding="utf-8") as r:
                        r.write("url:" + url + "\t"+"\t")
                        r.write("title:" + title + "\t")
                        r.write("\n")

        else:
            res= requests.get(url.strip(),headers=default_header,allow_redirects=True, timeout=3)
            status = res.status_code
            res.encoding = 'utf-8'
            title = Document(res.content).title()
            if title=='[no-title]':
                if len(res.content)>60:
                    if "Whitelabel" in res.text:
                        title='Whitelabel Error Page | Sprint Boot'
                    else:
                        title='[no-title]'
                else:
                    title=res.content.decode('utf-8')
            logger.INFO("url:{0}   title:{1} code: {2}".format(url,title,status))
            if args.report:
                with open(args.report, "a+",encoding="utf-8") as r:
                    r.write("url:"+url +"\t")
                    r.write("title:"+title + "\t")
                    r.write("\n")

    except Exception:
        pass
def main():
    _init_stdout()
    threadcount = args.threads
    urls = []
    if args.url_file:
        urlfile = args.url_file
        if not os.path.exists(urlfile):
            logger.ERROR("File: %s don't exists"% urlfile)
            sys.exit()
        with open(urlfile) as f:
            _urls = f.readlines()
        _urls = [i.strip() for i in _urls]
        urls.extend(_urls)
    with concurrent.futures.ThreadPoolExecutor(max_workers=int(threadcount)) as executor:
        checks = {executor.submit(check, url): url for url in urls}
        for future in concurrent.futures.as_completed(checks):
            url = checks[future]
            try:
                data = future.result()
            except Exception as exc:
                pass
if __name__ == '__main__':
    main()