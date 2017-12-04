# 使用Django开发企业资讯类网站
### 项目内容为**企业信息发布网站**，适用于所有需要展现企业信息，宣传企业形象的需求者

* 初次使用Django来进行Web开发，有很多需要改进的地方。下一步的改进计划是将django自带后台改进为自定义后台操作管理，实现全面定制化
* 部署使用了linux（centos7） + passanger + nginx + django，并实现了错误重连以及开机自启动

> 此项目为我初次使用Django来进行web开发，功能实现了
> 1. 基本的数据库数据的增删查改
> 2. 对路由做了优化
> 3. 后台界面的集成，傻瓜式管理数据的显现形式

### 关于部署我想说
0. 科普一下：
> wsgi：一种实现python解析的通用接口标准/协议，是一种通用的接口标准或者接口协议，实现了python web程序与服务器之间交互的通用性。 
> 利用它，web.py或bottle或者django等等的python web开发框架，就可以轻松地部署在不同的web server上了；

> uwsgi:同WSGI一样是一种通信协议 
> uwsgi协议是一个uWSGI服务器自有的协议，它用于定义传输信息的类型，它与WSGI相比是两样东西。

> uWSGI :一种python web server或称为Server/Gateway 
> uWSGI类似tornadoweb或者flup，是一种python web server，uWSGI是实现了uwsgi和WSGI两种协议的Web服务器，负责响应python 的web请求。 
> 因为apache、nginx等，它们自己都没有解析动态语言如php的功能，而是分派给其他模块来做，比如apache就可以说内置了php模块，让人感觉好像apache就支持php一> > 样。 


> uWSGI实现了wsgi协议、uwsgi协议、http等协议。 Nginx中HttpUwsgiModule的作用是与uWSGI服务器进行交换。

1. 使用centos + nginx + uwsgi进行搭建
2. 搭建流程
>  基本python3与django环境部署
>  django的setting.py的开发环境到生产环境的一系列切换
>  uwsgi安装与配置
>  nginx代理设置
3. 一句话描述搭建:每一个Django项目都自带一个wsgi文件接口，一般都在项目的manager.py层下的子目录，根据这个接口我们在manager.py层配置他的配置文件（demo.ini）.配置完毕后，使用最基本的启动命令进行启动 uwsgi --ini demo.ini(__一定得注意开头的[uwsgi]声明，缺失此文件会导致配置文件识别失败__)。接在来再到nginx里配置相应的location根的uwsgi代理(nginx conf目录的uwsgi_params文件)与静态文件 location /static的代理,配置完保存重启即可完成最简单的部署上线。
