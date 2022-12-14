# Adding file variables to easily test against other inputs.
# Can easily be hard-coded to make it truly one line.
q = {
    1 : 'day1.txt',
    2 : 'day2.txt',
    3 : 'day3.txt',
    4 : 'day4.txt',
    5 : 'day5.txt',
    6 : 'day6.txt',
    7 : 'day7.txt',
    8 : 'day8.txt',
}

# I'm sorry.
print('\nDay 01 Part 1:',max([sum([int(x) for x in g]) for g in [k.split('\n') for k in open(q[1]).read().split('\n\n')]]),
      '\nDay 01 Part 2:',sum(sorted([sum([int(x) for x in g]) for g in [k.split('\n') for k in open(q[1]).read().split('\n\n')]],reverse=True)[0:3]),
      
      '\nDay 02 Part 1:',sum([{'A X':4,'A Y':8,'A Z':3,'B X':1,'B Y':5,'B Z':9,'C X':7,'C Y':2,'C Z':6}[x] for x in open(q[2]).read().split('\n')]),
      '\nDay 02 Part 2:',sum([{'A X':3,'A Y':4,'A Z':8,'B X':1,'B Y':5,'B Z':9,'C X':2,'C Y':6,'C Z':7}[x] for x in open(q[2]).read().split('\n')]),
      
      '\nDay 03 Part 1:',sum([ord(x)-96 if x.islower() else ord(x)-38 for x in [set(x).intersection(y).pop() for x,y in [[i[:len(i)//2],i[len(i)//2:]] 
                                                                                                            for i in open(q[3]).read().split('\n')]]]),
      '\nDay 03 Part 2:',sum([ord(x)-96 if x.islower() else ord(x)-38 for x in [set(open(q[3]).read().split('\n')[i]).intersection(open(q[3]).read().split('\n')[i+1]).
                                                                                intersection(open(q[3]).read().split('\n')[i+2]).pop() for i in range(0,len(open(q[3]).read().split('\n')),3)]]),
      
      '\nDay 04 Part 1:',sum([(n[0][0]>=n[1][0] and n[0][1]<=n[1][1]) or (n[0][0]<=n[1][0] and n[0][1]>=n[1][1]) for n in [[[int(x) for x in a.split('-')],
                                                                                                        [int(y) for y in b.split('-')]] for a,b in [x.split(',') for x in open(q[4]).read().split('\n')]]]),
      '\nDay 04 Part 2:',sum([n[0][0]<=n[1][1] and n[0][1]>=n[1][0] for n in [[[int(x) for x in a.split('-')],[int(y) for y in b.split('-')]] for a,b in [x.split(',') for x in open(q[4]).read().split('\n')]]]),
      
      '\nDay 05 Part 1:',''.join([c[0] for c in k] if not (f:=open(q[5]).read().split('\n')) or not (t:=[[int(x[1]),int(x[3]),int(x[5])] 
                            for x in [y.split(' ') for y in f[10:]]]) or not (k:=[[] for i in range(9)]) or not [k[j//4].append(l[j]) for l in f[:8] for j in range(1,len(l),4) if l[j].isalpha()] or 
                                                                                                                        [k[p[2]-1].insert(0,k[p[1]-1].pop(0)) for p in t for n in range(p[0])] else ''),
      '\nDay 05 Part 2:',''.join([c[0] for c in k] if not (f:=open(q[5]).read().split('\n')) or not (t:=[[int(x[1]),int(x[3]),int(x[5])] for x in [y.split(' ') for y in f[10:]]]) or not (k:=[[] for i in range(9)]) or 
                                 not [k[j//4].append(l[j]) for l in f[:8] for j in range(1,len(l),4) if l[j].isalpha()] or [k[p[2]-1].insert(0,e) for p in t for e in reversed([k[p[1]-1].pop(0) for n in range(p[0])])] else ''),
      
      '\nDay 06 Part 1:',[i+1 for x in [open(q[6]).read()] for i in range(3,len(x)) if len(set(x[i-3:i+1]))==4][0],
      '\nDay 06 Part 2:',[i+1 for x in [open(q[6]).read()] for i in range(13,len(x)) if len(set(x[i-13:i+1]))==14][0],
     
      '\nDay 07 Part 1:',sum([x for x in u.values() if x<=100000] if not (u:={}) and not (g:=[]) and [((l[0]=='$' and l[1]=='cd') and (((l[2]=='/') and (g:=['//']) and not (u.update({'//':0}))) or (l[2]=='..' and g.pop()) or 
                                                                                                        ((h:='/'.join(g)+'/'+l[2]) and not g.append(h) and (not u.get(h) and not u.update({h:0}))))) or (l[0].isdigit() and 
                                                                                                            [u.update({d:u[d]+int(l[0])}) for d in g]) for l in [c.split(' ') for c in open(q[7]).read().split('\n')]] else ''),
      '\nDay 07 Part 2:',min([x for x in u.values() if x>u['//']-40000000]) if not (u:={}) and not (g:=[]) and [((l[0]=='$' and l[1]=='cd') and (((l[2]=='/') and (g:=['//']) and not (u.update({'//':0}))) or 
                                                                                                        (l[2]=='..' and g.pop()) or ((h:='/'.join(g)+'/'+l[2]) and not g.append(h) and (not u.get(h) and not u.update({h:0}))))) or
                                                                                                            (l[0].isdigit() and [u.update({d:u[d]+int(l[0])}) for d in g]) for l in [c.split(' ') for c in open(q[7]).read().split('\n')]] else '',
      
      '\nDay 08 Part 1:',sum([not bool([x for x in t[r][:c] if x>=t[r][c]] and [x for x in t[r][c+1:] if x>=t[r][c]] and [x[c] for i,x in enumerate(t) if x[c]>=t[r][c] and i<r] and [x[c] for i,x in enumerate(t) if x[c]>=t[r][c] and i>r])
                                                                                                                    for t in [[[int(y) for y in x] for x in open(q[8]).read().split('\n')]] for r in range(len(t)) for c in range(len(t[r]))]),
      '\nDay 08 Part 2:',max([sum([(x<t[r][c]) or (e:=True) for x in t[r][:c][::-1] if not e] if not (e:=False) else '')*sum([(x<t[r][c]) or (e:=True) for x in t[r][c+1:] if not e] if not (e:=False) else '')*sum([(x[c]<t[r][c]) or (e:=True) 
                                                                                                                    for i,x in reversed(list(enumerate(t))) if not e and i<r] if not (e:=False) else '')*sum([(x[c]<t[r][c]) or (e:=True) 
                                                                                                                    for i,x in enumerate(t) if not e and i>r] if not (e:=False) else '') for t in [[[int(y) for y in x] for x in open(q[8]).read().split('\n')]] 
                                                                                                                    for r in range(len(t)) for c in range(len(t[r]))]))
