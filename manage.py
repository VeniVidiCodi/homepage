# course: Kickstart Coding
# date: 11/19/19
# name: Victor Sanchez
# description: Templating for a static-site generator

from utils import main
import sys
from slugify import slugify




if len(sys.argv) < 3 and len(sys.argv) > 1:
    command = sys.argv[1]

    if command == "build":
        print("Build was specified")
        main()
    elif command == "new":
        print("New page was specified")
        new_name = slugify(input("New file name: "))
        print('New file created:', (new_name + '.html'))
        new_filename = ('content/' + new_name + '.html')
        new_content = open('templates/new_content_temp.html').read()
        open(new_filename, "w+").write(new_content)
        
else:
    print("\nPlease specify 'build' or 'new'\n"
        'Usage:\n'
        '   Rebuild site: python manage.py build\n'
        '   Create new page: python manage.py new')



