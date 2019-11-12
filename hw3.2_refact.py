def main():    
    for page in pages:
        page_filename = page['filename']
        page_output = page["output"]

        page_content = read_file(page_filename)        
        finished_content_page = apply_template(page_content)
        # Write webpage
        write_page(finished_content_page, page_output)

def apply_template(page_content):
    template = open("templates/base.html").read()
    finished_content_page = template.replace("{{content}}", page_content)
    finished_content_page = template.replace("{{title}}", finished_content_page)

    return finished_content_page

def write_page(finished_content_page, page_output):
    open(page_output, "w+").write(finished_content_page)
    return 

def read_file(page_filename):
    page_content = open(page_filename).read()
    return page_content



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

main()  # testing output

if __name__ == "main":
    main()