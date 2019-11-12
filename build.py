# Templates top and bottom
top = open('templates/top.html').read()
bottom = open('templates/bottom.html').read()

# Contents 
about_content = open('content/about.html').read()
projects_content = open('content/projects.html').read()
index_content = open('content/index.html').read()



# Creates html files with "top" + "content" + "bottom"
open('docs/about.html', 'w+').write(top + about_content + bottom)
open('docs/projects.html', 'w+').write(top + projects_content + bottom)
open('docs/index.html', 'w+').write(top + index_content + bottom)