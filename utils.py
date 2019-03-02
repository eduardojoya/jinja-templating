def content_files(): 
    import glob
    all_html_files = glob.glob('content/*.html')
    pages = [] 
    import os  
    for content in all_html_files: 
        file_path = content  
        file_name = os.path.basename(file_path) 
        name_only, extension = os.path.splitext(file_name) 
        pages.append({ 
        'filename': 'content/' + name_only + extension, 
        'title': name_only.title(), 
        'output': 'docs/' + name_only + extension,
        'links': name_only + extension
    })
    return pages 

def apply_template(template_html, file_name, page_title):
    from jinja2 import Template
    pages = content_files()
    content_html = open(file_name).read()
    template_html = open('templates/base.html').read()
    template = Template(template_html)
    return template.render(
    title= page_title,  
    content=content_html,
    pages = pages)

def output_page(template_html,page):
    file_name = page['filename']
    page_output = page['output']
    page_title = page['title']
    
    output_html = apply_template(template_html, file_name, page_title)
    open(page_output, 'w+').write(output_html)        

def main():
    pages = content_files()
    template_html = open('templates/base.html').read() 
    for page in pages:    
        output_page(template_html, page)

