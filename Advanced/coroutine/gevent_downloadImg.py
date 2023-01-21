import urllib.request
import gevent
from gevent import monkey
import ssl

# 解决一个SSL证书验证错误，当请求一个https站点，但是证书验证错误时，就会报这样的错误。
ssl._create_default_https_context = ssl._create_unverified_context

monkey.patch_all()


def downloader(img_name, img_url):
    req = urllib.request.urlopen(img_url)
    img_content = req.read()
    with open(img_name, "wb") as f:
        f.write(img_content)


def main():
    gevent.joinall([
        gevent.spawn(downloader, "1.jpg",
                     "https://activity.hdslb.com/blackboard/activity19689/static/img/logo.24f657ed.png"),
        gevent.spawn(downloader, "2.jpg",
                     "https://activity.hdslb.com/blackboard/activity19689/static/img/t-judge.5fda1f3b.png")
    ])


if __name__ == '__main__':
    main()
