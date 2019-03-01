print('Phase 1- Function to auto-create list')
def content_files(): #auto-generates the list 
    import glob
    all_html_files = glob.glob('content/*.html') #creates a list for all files in content
    pages = [] #create empty list
    import os  
    for content in all_html_files: 
        file_path = content #file_path defined as individual content files 
        file_name = os.path.basename(file_path) #os to extract files 
        name_only, extension = os.path.splitext(file_name) #to get file name and extension
        pages.append({ #add to list 
        'filename': 'content/' + name_only + extension, 
        'title': name_only.title(), 
        'output': 'docs/' + name_only + extension,
        'links': name_only + extension
    })
    return pages 

print('Phase 2 - Jinja2')
def apply_template(template_html, file_name, page_title,page_links):
    from jinja2 import Template
    pages = content_files()
    content_html = open(file_name).read()
    template_html = open('templates/base.html').read()
    template = Template(template_html)
    return template.render(
    title= page_title, #page_title taken from the list from the content_files function 
    content=content_html, #content_html from the files in pages list 
    navigation_links=page_links,
    pages = pages)

print('Phase 2 & 3 Complete!')
    
def output_page(template_html,page):
    file_name = page['filename']
    page_output = page['output']
    page_title = page['title']
    page_links = page['links']
    
    output_html = apply_template(template_html, file_name, page_title, page_links)
    open(page_output, 'w+').write(output_html)        

    
def main():
    pages = content_files()
    template_html = open('templates/base.html').read() 
    for page in pages:    
        output_page(template_html, page)

if __name__ == "__main__": 
    main()

