# Bird
Bird是一款用于HTTP探测的工具，支持多线程，特征搜索，可用于SRC资产梳理。
![Jietu20200516-184214](./pic/tools2.png)

## 声明

使用Bird前请遵守当地法律,Bird仅提供给教育行为使用。

## 使用

### 安装
安装Bird需要依赖Python3.6 以上环境.
```bash
git clone https://github.com/Ethancck/Bird.git
cd Bird # 进入git目录
pip3 install -r requirements.txt
python3 Bird.py -h
```
### HTTP探测

```
python3 Bird.py -f url.txt --output http.txt -t 30 #使用output参数输出到文件 -t 指定线程数目
```
### 特征搜索
这里搜索Spring Boot的报错页面
```
python3 Bird.py -f url.txt --output http.txt -t 30 --search "Whitelabel" 
```
![Jietu20200516-184214](./pic/tools1.png)

## TODO
- [x] CMS指纹识别
## 贡献&感谢
- Ethan
