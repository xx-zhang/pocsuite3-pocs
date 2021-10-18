import requests

import re

category_text = """<ul class="list-unstyled" id="category-list">
                        
                            <li><a href="/category/http-parameter-pollution">
                                
                                    HTTP 参数污染</a></li>
                        
                            <li><a href="/category/backdoor">
                                
                                    后门</a></li>
                        
                            <li><a href="/category/insecure-cookie-handling">
                                
                                    Cookie 验证错误</a></li>
                        
                            <li><a href="/category/csrf">
                                
                                    跨站请求伪造</a></li>
                        
                            <li><a href="/category/shellcode">
                                
                                    ShellCode</a></li>
                        
                            <li><a href="/category/sql-injection">
                                
                                    SQL 注入</a></li>
                        
                            <li><a href="/category/arbitrary-file-download">
                                
                                    任意文件下载</a></li>
                        
                            <li><a href="/category/arbitrary-file-creation">
                                
                                    任意文件创建</a></li>
                        
                            <li><a href="/category/arbitrary-file-deletion">
                                
                                    任意文件删除</a></li>
                        
                            <li><a href="/category/arbitrary-file-read">
                                
                                    任意文件读取</a></li>
                        
                            <li><a href="/category/other">
                                
                                    其他类型</a></li>
                        
                            <li><a href="/category/variable-coverage">
                                
                                    变量覆盖</a></li>
                        
                            <li><a href="/category/command-execution">
                                
                                    命令执行</a></li>
                        
                            <li><a href="/category/injecting-malware-codes">
                                
                                    嵌入恶意代码</a></li>
                        
                            <li><a href="/category/weak-password">
                                
                                    弱密码</a></li>
                        
                            <li><a href="/category/denial-of-service">
                                
                                    拒绝服务</a></li>
                        
                            <li><a href="/category/database-found">
                                
                                    数据库发现</a></li>
                        
                            <li><a href="/category/upload-files">
                                
                                    文件上传</a></li>
                        
                            <li><a href="/category/remote-file-inclusion">
                                
                                    远程文件包含</a></li>
                        
                            <li><a href="/category/local-overflow">
                                
                                    本地溢出</a></li>
                        
                            <li><a href="/category/privilege-escalation">
                                
                                    权限提升</a></li>
                        
                            <li><a href="/category/information-disclosure">
                                
                                    信息泄漏</a></li>
                        
                            <li><a href="/category/login-bypass">
                                
                                    登录绕过</a></li>
                        
                            <li><a href="/category/path-traversal">
                                
                                    目录穿越</a></li>
                        
                            <li><a href="/category/resolve-error">
                                
                                    解析错误</a></li>
                        
                            <li><a href="/category/unauthorized-access">
                                
                                    越权访问</a></li>
                        
                            <li><a href="/category/xss">
                                
                                    跨站脚本</a></li>
                        
                            <li><a href="/category/path-disclosure">
                                
                                    路径泄漏</a></li>
                        
                            <li><a href="/category/code-execution">
                                
                                    代码执行</a></li>
                        
                            <li><a href="/category/remote-password-change">
                                
                                    远程密码修改</a></li>
                        
                            <li><a href="/category/remote-overflow">
                                
                                    远程溢出</a></li>
                        
                            <li><a href="/category/directory-listing">
                                
                                    目录遍历</a></li>
                        
                            <li><a href="/category/null-byte-injection">
                                
                                    空字节注入</a></li>
                        
                            <li><a href="/category/man-in-the-middle">
                                
                                    中间人攻击</a></li>
                        
                            <li><a href="/category/format-string">
                                
                                    格式化字符串</a></li>
                        
                            <li><a href="/category/buffer-overflow">
                                
                                    缓冲区溢出</a></li>
                        
                            <li><a href="/category/http-request-splitting">
                                
                                    HTTP 请求拆分</a></li>
                        
                            <li><a href="/category/crlf-injection">
                                
                                    CRLF 注入</a></li>
                        
                            <li><a href="/category/xml-injection">
                                
                                    XML 注入</a></li>
                        
                            <li><a href="/category/local-file-inclusion">
                                
                                    本地文件包含</a></li>
                        
                            <li><a href="/category/credential-prediction">
                                
                                    证书预测</a></li>
                        
                            <li><a href="/category/http-response-splitting">
                                
                                    HTTP 响应拆分</a></li>
                        
                            <li><a href="/category/ssi-injection">
                                
                                    SSI 注入</a></li>
                        
                            <li><a href="/category/out-of-memory">
                                
                                    内存溢出</a></li>
                        
                            <li><a href="/category/integer-overflows">
                                
                                    整数溢出</a></li>
                        
                            <li><a href="/category/http-response-smuggling">
                                
                                    HTTP 响应伪造</a></li>
                        
                            <li><a href="/category/http-request-smuggling">
                                
                                    HTTP 请求伪造</a></li>
                        
                            <li><a href="/category/content-spoofing">
                                
                                    内容欺骗</a></li>
                        
                            <li><a href="/category/xquery-injection">
                                
                                    XQuery 注入</a></li>
                        
                            <li><a href="/category/buffer-over-read">
                                
                                    缓存区过读</a></li>
                        
                            <li><a href="/category/brute-force">
                                
                                    暴力破解</a></li>
                        
                            <li><a href="/category/ldap-injection">
                                
                                    LDAP 注入</a></li>
                        
                            <li><a href="/category/security-mode-bypass">
                                
                                    安全模式绕过</a></li>
                        
                            <li><a href="/category/backup-file-found">
                                
                                    备份文件发现</a></li>
                        
                            <li><a href="/category/xpath-injection">
                                
                                    XPath 注入</a></li>
                        
                            <li><a href="/category/url-redirector-abuse">
                                
                                    URL 重定向</a></li>
                        
                            <li><a href="/category/code-disclosure">
                                
                                    代码泄漏</a></li>
                        
                            <li><a href="/category/use-after-free">
                                
                                    释放后重用</a></li>
                        
                            <li><a href="/category/dns-hijacking">
                                
                                    DNS 劫持</a></li>
                        
                            <li><a href="/category/improper-input-validation">
                                
                                    错误的输入验证</a></li>
                        
                            <li><a href="/category/uxss">
                                
                                    通用跨站脚本</a></li>
                        
                            <li><a href="/category/ssrf">
                                
                                    服务器端请求伪造</a></li>
                        
                            <li><a href="/category/cross-domain-vulnerability">
                                
                                    跨域漏洞</a></li>
                        
                            <li><a href="/category/improper-certificate-validation">
                                
                                    错误的证书验证</a></li>
                        
                            <li><a href="/category/cache-poisoning">
                                
                                    缓存投毒</a></li>
                        
                            <li><a href="/category/request-smuggling">
                                
                                    HTTP请求走私</a></li>
                        
                            <li><a href="/category/command-injection">
                                
                                    命令注入</a></li>
                        
                    </ul>"""

def test():
    response = requests.get(url='https://www.seebug.org/category/')
    print(response.content.decode())
    if response.status_code < 400:
        print(response.content.decode())
        datas = re.findall("<li><a href=\"/category/(.*)\">(.*)</a></li>", response.content.decode())

def test2():
    # print(category_text)
    datas = re.findall('<li><a href="/category/(.*?)">(.*?)</a></li>', category_text.replace("\n", ""))
    # print(datas)
    result = []
    for x in datas:
        _tmp = {"short_name": x[0], "cn_name": x[1].strip()}
        result.append(_tmp)
    print(result)


if __name__ == '__main__':
    test2()
