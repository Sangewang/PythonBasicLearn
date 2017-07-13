sentence = raw_input("Sentence: ")

screen_width = 80
text_width   = len(sentence)
box_width    = text_width + 6
left_margin  = (screen_width - box_width) // 2


#print text_width
#print box_width
#print left_margin

print
print ' '*left_margin + '+' + '-'*(box_width-2) + '+'
print ' '*(left_margin+2) + '|' + ' '*text_width    + '|'
print ' '*(left_margin+2) + '|' +     sentence      + '|'
print ' '*(left_margin+2) + '|' + ' '*text_width    + '|'
print ' '*left_margin + '+' + '-'*(box_width-2) + '+'
print 
