def count_words(b):
    words = b.split()
    print(len(words))
    
def count_characters(b):
    characters_dict = {}
    for c in b:
        if c.lower() not in characters_dict:
            characters_dict[c.lower()] = 1
        else:
            characters_dict[c.lower()] += 1
    print(characters_dict)
    return characters_dict
    
def generate_report(b):
    character_counts = count_characters(b)
    report_statements = ["---- Character report from frankenstien.txt ----","---- END REPORT ----"]
    for c in character_counts:
        if c.isalpha():
            report_statements.insert(len(report_statements)-1, f"The '{c}' was used '{character_counts[c]}' times.")
    
    for s in report_statements:
        print(s)
        
with open('books/frankenstien.txt') as f:
    file_contents = f.read()
    count_words(file_contents)
    count_characters(str(file_contents))
    generate_report(str(file_contents))
    
