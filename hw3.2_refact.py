def main():    
    for page in pages:
        filename = page["filename"]
        output = page["output"]
        title = page["title"] 

        content = read_file(filename) 
        template = apply_template(content, title)
        # Write webpage
        write_page(template, output)

# Generates individual pages, inserting page content and title
def apply_template(content, title):
    template = open("templates/base.html").read()
    template = template.replace("{{content}}", content)
    template = template.replace("{{title}}", title)
    return template


# Writes generated pages into end files
def write_page(template, output):
    open(output, "w+").write(template)
    return 

def read_file(filename):
    content = open(filename).read()
    return content


pages = [
    {
    "filename": "content/about.html",
    "output": "docs/about.html",
    "title": "About Me",
    },
    {
    "filename": "content/projects.html",
    "output": "docs/projects.html",
    "title": "My Projects",
    },
    {
    "filename": "content/index.html",
    "output": "docs/index.html",
    "title": "My programming blog",
    },
]

if __name__ == "__main__":
    main()

