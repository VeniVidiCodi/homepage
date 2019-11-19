import glob
import os


pages = []



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



def create_pages():
    all_html_files = glob.glob("content/*.html")
    print(all_html_files)                               # lists all items in content directory

    for file in all_html_files:
        file_path = file
        file_name = os.path.basename(file_path)
        name_only, extension = os.path.splitext(file_name) 
        output_file = os.path.join('docs', file_name)
        pages.append({
        "filename": file_path,
        "title": name_only,
        "output": output_file,
        })
        print(pages)

# file_path = "content/blog.html"
# file_name = os.path.basename(file_path)             # outputs filename at base of path
# print(file_name)
# name_only, extension = os.path.splitext(file_name)    # outputs dict of associated 
# print(name_only)
# output_file = os.path.join('docs', file_name)


def main():    
    create_pages()
    for page in pages:
        filename = page["filename"]
        output = page["output"]
        title = page["title"] 

        content = read_file(filename) 
        template = apply_template(content, title)
        # Write webpage
        write_page(template, output)

    

if __name__ == "__main__":
    main()

