# course: Kickstart Coding
# date: 11/19/19
# name: Victor Sanchez
# description: This is the main body of functions needed for
#              running manage.py static-site generator template

import glob
import os
from jinja2 import Template
import pprint




pages = []

def apply_template(content, title):
    template = open("templates/base.html").read()
    template = template.replace("{{content}}", content)
    template = template.replace("{{title}}", title)
    return template

def read_file(filename):
    content = open(filename).read()
    return content

def write_page(content, output):
    open(output, "w+").write(content)


def create_page_list():
    # Gathers and lists files in the 'content' directory
    all_html_files = glob.glob("content/*.html")
    print("\nContent files:")
    print(all_html_files)

    # Filters and reassembles filenames into variables
    print("\nPages index:")
    for file in all_html_files:
        file_path = file
        file_name = os.path.basename(file_path)
        name_only, extension = os.path.splitext(file_name)
        output_file = os.path.join('docs', file_name)

        pages.append({                                       
        "file_path": file_path,
        "title": name_only,
        "output": output_file,
        "file_name": file_name
        })
        
    pprint.pprint(pages)


def main():    
    create_page_list()
    for page in pages: 
        filename = page["file_path"]  
        output = page["output"]
        title = page["title"] 

        content_html = open(filename).read()
        template_html = open("templates/base.html").read()   
        template = Template(template_html)

        result_page = template.render(
            pages = pages,
            title = title,
            content = content_html,
            output_file = page['file_name'],
        )

        write_page(result_page, output)


if __name__ == "__main__":
    main()