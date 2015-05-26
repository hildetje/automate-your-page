# Generates the HTML for each section
def generate_section_HTML(section_title, section_description):
    html_text_1 = '''
<div class="section">
    <h2>
        ''' + str(section_title)
    html_text_2 = '''
    </h2>
    <p>
        ''' + section_description
    html_text_3 = '''
    </p>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

# Defines each section title and description
def make_HTML(section):
    section_title = section[0]
    section_description = section[1]
    return generate_section_HTML(section_title, section_description)

# Example list of sections
EXAMPLE_LIST_OF_SECTIONS = [ ['Python', 'Python is a Programming Language'],
                             ['For Loop', 'For Loops allow you to iterate over lists'],
                             ['Lists', 'Lists are sequences of data'] ]

# Creates the HTML for each section, using the make_HTML function described above
def make_HTML_for_many_sections(list_of_sections):
    HTML = ""
    for section in list_of_sections:
        section_HTML = make_HTML(section)
        HTML = HTML + section_HTML
    return HTML    
    
print make_HTML_for_many_sections(EXAMPLE_LIST_OF_SECTIONS)
# The previous line of code should print the following
"""
<div class="concept">
    <div class="concept-title">
        Python
    </div>
    <div class="concept-description">
        Python is a Programming Language
    </div>
</div>
<div class="concept">
    <div class="concept-title">
        For Loop
    </div>
    <div class="concept-description">
        For Loops allow you to iterate over lists
    </div>
</div>
<div class="concept">
    <div class="concept-title">
        Lists
    </div>
    <div class="concept-description">
        Lists are sequences of data
    </div>
</div>
"""