# 一个简单的微博爬虫

## 为什么写这个程序

  最近想谋求一份python相关的实习工作，苦于大学期间没做过相关项目，所以现学现卖做出一个小爬虫，证明一下我有这个学习能力

## 为什么是python
  大学期间接触了很多语言(c、c++、java、object-c、PHP)，我觉得这是多而不精，但老师说你不去尝试怎么知道哪一个适合自己。忘记了什么时候接触的python，感觉很上手，说不清为什么喜欢python，可能就是好用吧

## 关于这个程序

### 说明

  利用requests库爬取某个博主的所有微博(包括发微博的时间)，保存到xls表格里

  爬取微博PC端很有难度，所以这里爬取的是手机端

  这个程序只供学习，不然，小拳拳捶你胸口！

### 一些不足

  这个程序是单进程爬取，而一些大V的微博有好几千条甚至上万条，所以爬完大V的微博耗时很久很久...

### 以后的改进

  因为考虑到python没有真正的多线程这一说，改善耗时太久这一问题，我打算利用多进程爬取，因为在未来的时间我将会继续学习多进程的知识  
