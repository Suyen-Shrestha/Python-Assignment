
def add_tags(tag_name, word):
    """
        Function to create html string with tags around the word.
    """
    starting_tag = f'<{tag_name}>'
    closing_tag = f'</{tag_name}>'
    html_string = starting_tag + word + closing_tag
    return html_string


sample_string = input('Enter a sample string: ')
sample_tag = input('Enter a sample html tag without angular brackets: ').strip('<').strip('>')
final_result = add_tags(sample_tag,sample_string)    
   

print(f'The final resulting html sting: {final_result}')
