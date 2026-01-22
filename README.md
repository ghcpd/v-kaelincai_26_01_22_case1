# Fake UserAgent - Issue #40 Demonstration

这个项目演示了 [Issue #40](https://github.com/fake-useragent/fake-useragent/issues/40) 的修复。

## Issue 描述

用户希望添加 `__version__` 属性，以便能够检查库的版本。

## 问题

在修复前，库只提供了 `VERSION` 常量，而没有标准的 `__version__` 属性。

## Before Fix (修复前)

```python
import fake_useragent

# 只能使用 VERSION
print(fake_useragent.VERSION)  # 可以工作

# 无法使用 __version__
try:
    print(fake_useragent.__version__)  # 会报错 AttributeError
except AttributeError:
    print("没有 __version__ 属性")
```

## After Fix (修复后)

```python
import fake_useragent

# 可以使用标准的 __version__
print(fake_useragent.__version__)  # 可以工作

# 为了兼容性，VERSION 仍然可用
print(fake_useragent.VERSION)  # 也可以工作
```

## 测试

运行测试脚本：
```bash
python test_version.py
```
