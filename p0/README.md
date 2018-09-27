# p0

> 欢迎大家来到 PSU CUSA 大家庭，宏仔十分期待之后在 CUSA 的日子里能跟大家一起学习，一起进步，一起成长！
> Work Hard, Play Hard! 

### 目的

- 学习 git 命令 (clone, branch, add, commit, push)
- 学习 bash shell 命令 (cd, ls, mkdir, touch, rm)

### 任务

> 预计耗时：40min

1. 在你自己的电脑上配置好本地 git 环境
   * Configuring your local git environment
     `$ git config --global user.name "Your Username"`
     `$ git config --global user.email "Your Email"`

   * Adding SSH key 
     `$ ssh-keygen -t rsa -b 4096 -C "your@email.com"`
     复制`∼/.ssh/id_rsa.pub`里的 public key 到 GitHub Account 里

2. 创建一个 branch 来准备开始你加下来的任务 (e.g. task_p0_yourName) 

    `$ git branch < your-branch-name >  # to create your branch` 
    `$ git checkout < your-branch-name >  # to switch to your new branch` 
    `$ git push origin < your-branch-name # to push your new branch>` 
    `$ git branch -a # to list all branches`

3. 创建一个用跟你自己 GitHub username 一样名字的文件夹 (e.g. v1siuol/)

4. 把你自己修改过的分支提交到 repo 上并进行 pull request 

5. 恭喜你已完成 p0 的所有任务啦！！！


### Reference

- [Git Handbook](https://guides.github.com/introduction/git-handbook/)

- [Git 教程 - 廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)

