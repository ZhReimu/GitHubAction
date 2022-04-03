# GitHubAction

GitHub Actions 就是类似于腾讯云的云函数功能

GitHub 的设置比较繁琐，但能用就行嘛，白嫖的东西谁不喜欢呢？

二者各有优劣不予比较。

~~关于玩法，暂时只能想到自动签到了~~

值得注意的是：GitHub 设置了并发工作数，也就是说：

免费账户最多同时进行 `20` 个 WorkFlows ~~对我来说足够了就是~~

# 启用步骤
## ~~1.  创建一个仓库~~

## 2.  点击上方的**Actions**，按照提示新建一个**.yml**文件。

然后就会得到类似于下边这样的一个文件，大部分都做了注释

这是一个在 `Ubuntu 18.04` 环境下运行 `Python 3.8`  的 `yml` 文件例子

由于每次触发 `Action` 都是一个新的环境，因此需要每次重新安装Python库

``` yml
# Action 名
name: 测试
# 触发方式
on:
    # 允许手动触发
    workflow_dispatch:
    # 提交代码时触发
    push:
    # 定时任务触发
    schedule:
        # 默认是UTC时间，中国是 UTC+8 时间 
        - cron: "00 04 * * *"
jobs:
    build:
        # 指定运行环境，最新版Ubuntu：ubuntu-latest
        runs-on: ubuntu-18.04
        # Action的执行步骤
        steps:
            # 将本仓库下载到 runner 里
            - name: Checkout
              uses: actions/checkout@v2
            # name为步骤名
            - name: "设置 python3.8 环境"
              uses: actions/setup-python@v1
              with:
                python-version: 3.8
            - name: "安装依赖包"
            # run为要执行的命令
              run: pip install -r ./requirements.txt
            - name: "开始运行指定文件"
              run: python3 test.py
            # env是用来设置环境变量的
              env:
            # 设置一个环境变量，名为 MY_PARAM 值为secret里的MY_PARAM的内容
                  MY_PARAM: ${{ secrets.MY_PARAM }}
            - name: "上传执行结果"
              run: |
                # 设置git的用户名、邮箱
                git config --global user.name "ZhReimu"
                git config --global user.email "1725338233@qq.com"
                git add result.txt
                git commit -m '上传执行结果'
                git push -u origin main
```
## 3. 设置  Secrets

点击上方的 `Settings` 在左侧找到 `Secrets`

点击 `Secrets` 再点击右上角的 `New repository secret` 

输入 `Secret` 名和它的值就设置好了一个 `Secret`

需要注意的是，`Secrets` 正如其名是用来存放密钥之类的东西的变量

因此 即使你用 `print` 尝试将其打印出来也会显示 ```***``` 但它确实有值的，可以在程序里使用的值

## 4. 使用 Secrets

经过了下边的操作，`Secrets` 已经被设置进了 `Actions` 的环境变量

因此想要调用 `Secrets` 的内容就需要设法取出环境变量中的Secrets

`Python` 的实现方法如下

``` Python3
import os
PARAM = os.environ['MY_PARAM']
```
## 5.  保存执行结果到本仓库，本质上是曲线救国辣，将结果文件通过 git 上传到本仓库

咱也是抄的别人的，不明觉厉。

`cd` 到指定目录中去然后 `git add.` 表示上传该目录中所有文件，这样这部分就可以通用了，不管程序保存的文件名是什么。

```yml
            - name: "上传执行结果"
              run: |
                git config --global user.name "ZhReimu"
                git config --global user.email "1725338233@qq.com"
                cd 执行结果
                git add .
                git commit -m '上传执行结果'
                git push -u origin main
```
## 6.使用 WebHook 手动触发

需要先创建一个带有 ```repo``` 权限的 [Personal access token](https://github.com/settings/tokens)

然后将触发方式设置为 ```repository_dispatch```

类似于下边的

```yml
# Action 名
name: WebHook
# 触发方式
on: repository_dispatch
jobs:
  run:
    runs-on: ubuntu-18.04
    steps:
    - name: 开始执行命令
      run: |
        echo Hello World!
```

## 最后向  ```api.github.com``` 以一种神奇的方式 post 一下就可以了，Python 代码如下：

```python
import requests


user_name='【填入你的用户名】'
user_token='【填入之前生成的Personal access token】'
repo_name='【填入仓库名】'
cmd_name='【填入WebHook事件名】'

headers = {
    'Accept': 'application/vnd.github.everest-preview+json',
    'Authorization': f'token {user_token}',
}
data = '{"event_type": '+f'"cmd_name"}'
url=f'https://api.github.com/repos/{user_name}/{repo_name}/dispatches'
requests.post(url=url, headers=headers, data=data)
```
# 以上内容搜集于网络，如有雷同，纯属巧合。