import sys,os,markdown

def isexist_mdfile(mdfile):
    if not os.path.exists(mdfile):
        sys.stdout.write(f"mdfile is not exists.\n" +
                         f"please create a mdfile.")
        sys.stdout.flush()

def convert(mdfile, htmlfile):
    if not os.path.exists(mdfile):
        isexist_mdfile(mdfile)
        return
    
    with open(mdfile, "r", encoding="utf-8") as md:
        read_md = md.read()
    
    content_html = markdown.markdown(read_md, extensions=["tables"])
    with open(htmlfile, "w") as html:
        html.write(content_html)
    pass

def main():
    if len(sys.argv) < 3:
        print("please check to command.")
        return

    operation = sys.argv[1]
    markdownfile = sys.argv[2]
    htmlfile = sys.argv[3]

    if operation == "markdown" and len(sys.argv) == 4:
        convert(markdownfile, htmlfile)
    else:
        print("invalid command or number of argument.")

if __name__ == "__main__":
    main()

# python3 file-converter.py markdown sample.md sample.html