#!/usr/bin/python

'''Produce LaTeX source from custom comment-response markup.
'''

import argparse
argp = argparse.ArgumentParser()
argp.add_argument("--input", help="input file name")
argp.add_argument("--output", help="output file name")
args = argp.parse_args()

with open(args.input, 'r') as ifh, open(args.output, 'w') as ofh:
    cell_lines, cell_comments, cell_response = '','',''
    part = 0
    first = True
    lines = ifh.readlines()
    lines.append(None)
    for line in lines:
        if line != None: line = line.strip()
        if line==None or line.startswith('c '):
            if not first:
                if cell_response == '':
                    cell_response = 'Done.'
                ofh.write('\\raggedright\\it ' + cell_lines + ' &\n')
                ofh.write(cell_comments + '&\n')
                ofh.write(cell_response + ' \\\\\n')
                cell_lines, cell_comments, cell_response = '','',''
            if line != None:
                cell_lines = line[2:]
                part = 1
        elif part == 1:
            if line.startswith('r '):
                cell_response = line[2:]
                part = 2
            else:
                cell_comments += ' ' + line
        elif part == 2:
            cell_response += ' ' + line
        first = False
