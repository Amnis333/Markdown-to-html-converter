import markdown
import sys


def convert_md_to_html():
    if len(sys.argv) < 4:
        print("Some argument might be lost. Input [.py file] [.md file] [.html file]")
        return 
    
    if len(sys.argv) > 4:
        print("Too many argument is given. Input [.py file] [.md file] [.html file]")
        return

    if sys.argv[1] != "markdown":
        print(f'\'{sys.argv[1]}\' is not supported command. Input \'markdown\' instead of \'{sys.argv[1]}\'.')
        return 

    if sys.argv[2][sys.argv[2].find('.') : ] != ".md":
        print(f'\'{sys.argv[2]}\' is not \'.md\' file.')
        return 
    
    if sys.argv[3][sys.argv[3].find('.') : ] != ".html":
        print(f'\'{sys.argv[3]}\' is not \'.html\' file.')
        return 
    
    md_file = open(sys.argv[2])
    md_content = md_file.read()
    md_file.close()

    html_content = markdown.markdown(md_content)
    with open(sys.argv[3], "w") as f:
        f.write(html_content)


convert_md_to_html()