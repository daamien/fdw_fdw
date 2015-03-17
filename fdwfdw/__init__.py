"""

"""

from multicorn import ForeignDataWrapper
import urllib
import re

class FDWFDW(ForeignDataWrapper):

    def __init__(self,options,columns):
        super(FDWFDW,self).__init__(options,columns)
        self.url='https://wiki.postgresql.org/index.php?title=Foreign_data_wrappers&action=raw'
        self.columns=columns

    # remove wiki syntax
    def clean(self,code):
        # first char is a pipe
        # remove useless white space
        # lower characters
        value = code[1:].strip().lower()

        # if the code contains a link, remove it and  
        value = re.sub(r'\[(.+?)( +)(.+?)\]', r'\3', value)

        return value

    def execute(self, quals, columns):

        response = urllib.urlopen(self.url)
        wiki_code = response.read().split("\n")

        # Parse the raw mediawiki code
        i=0 
        wrappers=[]

        while i < len(wiki_code) :
            if ( wiki_code[i] == '|-' and wiki_code[i+1][0] == '|') :
                # we found a FDW description
                # let's parse it
                w={}
                w['source'] = self.clean(wiki_code[i+1])
                w['type']   = self.clean(wiki_code[i+2])
                w['licence']   = self.clean(wiki_code[i+3])
                w['code']   = self.clean(wiki_code[i+4])
                w['install']   = self.clean(wiki_code[i+5])
                w['doc']   = self.clean(wiki_code[i+6])
                w['notes']   = self.clean(wiki_code[i+7])
                wrappers.append(w)
                # shift the cursor the next line to be parsed
                i+=7

            # next line
            i+=1

        # Rturn the proper columns
        for w in wrappers:
            line = {}
            for column_name in self.columns:
                line[column_name] = w[column_name]
            yield line
