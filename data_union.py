import os

def uniondata():
    filedir = os.getcwd()+'//aspath'
    filenames=os.listdir(filedir)
    f=open('rib.txt','w')
    i=0
    for filename in filenames:
        i+=1
        print(i)
        if i>0:
            filepath = filedir+'//'+filename
            for line in open(filepath,encoding='gbk', errors='ignore'):
                data=str(line)
                if '{' in data:
                    continue
                newline=data.replace(' ','|')
                f.writelines(newline)
            f.write('\n')
    f.close()

def line_to_space(filename):
    f=open('aspath_asrank.txt','w')
    for line in open(filename,encoding='gbk', errors='ignore'):
        newline=line.replace('|',' ')
        f.writelines(newline)
    f.close()

if __name__ == '__main__':
    line_to_space("/home/zed/src/ProbLink-master/sanitized_rib.txt")
    
    