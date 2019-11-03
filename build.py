# Templates top and bottom
top = open('templates/top.html').read()
bottom = open('templates/bottom.html').read()

# Contents 
index_content = open('content/index_part.html').read()
art_content = open('content/art_part.html').read()
blog_content = open('content/blog_part.html').read()



# Creates html files with "top" + "content" + "bottom"
open('new_site/index.html', 'w+').write(top + index_content + bottom)
open('new_site/art.html', 'w+').write(top + art_content + bottom)
open('new_site/blog.html', 'w+').write(top + blog_content + bottom)