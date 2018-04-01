def get_definition(word):
    if word == 'sentence':
        return ['set', 'of', 'words']
    if word == 'difficult':
        return ['not', 'easy']
    if word == 'extraordinary':
        return ['better', 'than', 'ordinary']
    if word == 'ordinary':
        return ['normal']
    if word == 'discover':
        return ['come', 'by']
    if word == 'mitochondria':
        return ['cells', 'in', 'cytoplasm','that','convert','energy']
    if word == 'cytoplasm':
        return ['gel', 'outside', 'a','nucleus']
    if word == 'powerhouse':
        return ['main', 'source', 'of','power']

##should print: this set of words is not easy to read
read_sentence(['this','sentence','is','difficult', 'to', 'read'],7)
print()
##should print: better than normal people are not easy to come by
read_sentence(['extraordinary', 'people', 'are', 'difficult', 'to', 'discover'], 7)
print()
##should print: better than ordinary people are not easy to discover 
read_sentence(['extraordinary', 'people', 'are', 'difficult', 'to', 'discover'], 8)
print()
##should print: cells in gell outside a nucleus that convert energy are the main source of power of the cell
read_sentence(['mitochondria', 'are', 'the', 'powerhouse', 'of', 'the', 'cell'], 7)
print()
##should print: mitochondria are the powerhouse of the call
read_sentence(['mitochondria', 'are', 'the', 'powerhouse', 'of', 'the', 'cell'], 20)
