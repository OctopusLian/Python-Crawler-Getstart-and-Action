# python文件操作  

## 读写文本文件  

### 第一种方式  

```python
f = open('文件路径','文件操作方式',encoding='utf-8')

#对文件进行操作

f.close()

```

### 第二种方式，使用`python`的上下文管理器  

```python
with open('文件路径','文件操作方式',encoding='utf-8') as f

#对文件进行操作
```

推荐使用第二种方式。