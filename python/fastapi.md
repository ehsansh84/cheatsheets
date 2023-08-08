How to serve README.md as /readme?
Create `project_dir/docs/README.md`:
```
### Hello world!
```

Create a template to render markdown as html `project_dir/templates/readme.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Readme</title>
</head>
<body>
    {{ content | safe }}
</body>
</html>
```

```python
app_dir = os.path.dirname(__file__)
project_dir = os.path.dirname(app_dir)


def read_readme():
    with open(readme_path, "r", encoding="utf-8") as file:
        markdown_content = file.read()
        html_content = markdown2.markdown(markdown_content)
        # print(html_content)
        return html_content

from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory=os.path.join(project_dir, "templates"))

@app.get("/readme")
async def get_readme(request: Request):
    html_content = read_readme()
    print(templates)
    return templates.TemplateResponse("readme.html", {"request": request, "content": html_content})
```
