How to get parentdirectory address?
this is app_directory:
```python
app_directory = os.path.dirname(os.path.abspath(__file__))
```
Output is:
```
/home/oem/dev/my_project/app
```

```
dir1 = os.path.dirname(app_directory)
dir2 = os.path.dirname(dir1)
dir3 = os.path.dirname(dir2)
print(dir1)
print(dir2)
print(dir3)
```
Ouitput:
```
/home/oem/dev/my_project
/home/oem/dev
/home/oem
```
