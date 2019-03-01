def main():
    #List with dictionary for information on site pages
pages = [    
        {   'filename': 'content/index.html',
            'output': 'docs/index.html',
            'title': 'About Me',   
        },
        {
            'filename': 'content/resume.html',
            'output': 'docs/resume.html',
            'title': 'Resume',
        },
        {
            'filename': 'content/education.html',
            'output': 'docs/education.html',
            'title': 'Education',
        },
        {
            'filename': 'content/interests.html',
            'output': 'docs/interests.html',
            'title': 'Interests',
        },
        {  
            'filename': 'content/blog.html',
            'output': 'docs/blog.html',
            'title': 'Coding Journey Blog',
        },
       ]




    for page in pages:
          
        def apply_template(content): #Read in template, do string replacing and return result 
                template = open('templates/base.html').read() #reads entire template
                index_content = open(page['filename']).read() #reads in content of each page 
                finished_index_page = template.replace('{{content}}', index_content) #use string replace for content
                finished_index_page = finished_index_page.replace('{{title}}', page['title']) #use string replace for title 
                return finished_index_page #return results 
            
                
        def output_file():
                content = open(page['output']).read()
                finished_html = apply_template(content) #invoke apply_template function and write into files in 'docs' 

if __name__ == "__main__": 
    main()
