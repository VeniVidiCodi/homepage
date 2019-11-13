def main():    
    for page in pages:
        filename = page["filename"]
        output = page["output"]
        title = page["title"]  

        content = read_file(filename)  
        finished_content_page = apply_template(content, title)
        # Write webpage
        write_page(finished_content_page, output)

# def write_title(title, finished_content_page):
#     finished_content_page = finished_content_page.replace("{{title}}", title)
#     return finished_content_page

# Generates individual pages with content and title
def apply_template(content, title):
    template = open("templates/base.html").read()
    finished_content_page = template.replace("{{content}}", content).replace("{{title}}", title)
    # finished_content_page = template.replace("{{title}}", finished_content_page)
    return finished_content_page

# Writes generated pages into end files
def write_page(finished_content_page, output):
    open(output, "w+").write(finished_content_page)
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

if __name__ == "main":
    main()