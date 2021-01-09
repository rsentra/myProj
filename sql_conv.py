# main script
import os,re,sys
def toLower(s):
    str=s.group()
    return str.lower()

def main(dName,fName):
    justCmnt=True 
    f=open(os.path.join(dName,fName),'r',encoding='utf-8')

    wName=fName.split('.')[0]+'_my'+'.'+fName.split('.')[1]
    fw=open(os.path.join(dName,wName), "w")
    p=re.compile('AND\s*LIMIT', re.I)
    pCmt=re.compile('^\s--[\d\s\w\W]*')          #--주석만 있는라인
    pCmt2=re.compile('--[\d\s\w\W]*')            #라인내 --주석
    pChar=re.compile("\w*TO_CHAR\([\s\S]+\)")    #to_char안에 number formatting
    pNum=re.compile("999,999,999")               #to_char안에 number formatting

    sv=""
    inlines=f.readlines()
    lists=[]
    for i,line in enumerate(inlines):
        if not line: break
        line=re.sub(pCmt,'',line)    #주석만 있는라인 제거 [필요할 경우 사용]
        if len(line.strip())==0: continue
            
        line.replace('\t','    ')     #tab -> space(4)
        if line.strip().endswith('AND'):                #sqlines에 의한 limit전환오류 보정
            sv=line.rstrip()+" "
            continue
        else:
            line=sv+line
            line=re.sub(p,"limit",line)
            sv=""
            
        line=re.sub("SQLINES DEMO \*{3}","",line,re.I)   #주석제거
        line=re.sub("/\*\s*\/","/* */",line)             #sqlines에 의해 깨진 주석 보정
        if re.search('PAD\(TO_CHAR\(*',line):            #pad(to_char)
            line=re.sub('PAD\(TO_CHAR\(*','PAD(',line).replace(')','',1) 
        if re.search("TO_CHAR\([^\(,]+\)",line):          #to_char()
            line=re.sub("TO_CHAR\([^\(,]+\)","cast("+line[line.find('(')+1:line.find(')')]+" as char)" ,line)
        if re.search(pChar,line) and re.search(pNum,line): #to_char안에 number formatting
            line= line.replace('TO_CHAR','format').replace('999,999,999','0')
        
        converted= re.sub("(?<!\%)[\w]+[^'+\w+']",toLower,line) #소문자변환(' '제외)
    
        if len(converted.strip())>0:
            lists.append(converted)

    if justCmnt:    #주석라인 정렬
        dt=list(map(lambda x: x.replace('\t','    ').rstrip(),lists))
        sqlMax=max(map(lambda x: min(len(x.split('--')[0].rstrip()),
                                    len(x.split('/*')[0].rstrip())), dt)) #주석직전까지 max
        for i,val in enumerate(dt):
            mx=max(val.find('--'),val.find('/*'))
            if  mx>sqlMax: mx=sqlMax
            if  mx>=0:
    #             val=val[0:mx].ljust(sqlMax)+val[mx:].lstrip()  #뒤에 맞춤
                val=val[0:mx]+'  '+val[mx:].lstrip()   #sql + 공백2 뒤에 맞춤
            dt[i]=val.rstrip()
    else: dt=lists
        
    del lists,inlines          
    fw.write('\n'.join(str(val) for val in dt))
    f.close()
    fw.close()
    print(wName,' Created')
        
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('사용법 오류입니다')
        print('Usage:  python sql_conv.py path filename')
        sys.exit()
    js= os.path.join(sys.argv[1],sys.argv[2])
    if not os.path.isfile(js):
        print(sys.argv[1]+sys.argv[2] , 'file not found')
        sys.exit()
    
    main(sys.argv[1],sys.argv[2])
    print("Finished")
