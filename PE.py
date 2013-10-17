#coding=gbk
import pefile
import os,sys
import shutil
import stat
import hashlib
from time import *


def archive(srcDir):
    if os.path.isfile(srcDir):
        try:
            pefile.PE(srcDir)
            print "\n================================================================================"
            print "@Author: xuzhijian17 2011 PE File Filter command Tool"
            print "Copyright (c) 1990 - 2011 Qianyun Technologies"
            print "Program version 10.0.1388, engine 10.0.1516"
            print "Version 1516/3730 ",strftime("%Y-%m-%d %H:%M:%S")
            print "================================================================================\n"
            print "\t-----------------------------------------------------------"
            print "\tThis is a PE file,The following is a HASH value of the file"
            print "\t-----------------------------------------------------------\n"
            print "   MD5值:",hashlib.md5(open(srcDir,'rb').read()).hexdigest()
            print "\n  SHA1值:",hashlib.sha1(open(srcDir,'rb').read()).hexdigest()                         
            print "\nSHA224值:",hashlib.sha224(open(srcDir,'rb').read()).hexdigest()
            print "\nSHA256值:",hashlib.sha256(open(srcDir,'rb').read()).hexdigest()
            print "\nSHA384值:",hashlib.sha384(open(srcDir,'rb').read()).hexdigest()
            print "\nSHA512值:",hashlib.sha512(open(srcDir,'rb').read()).hexdigest()
            print "\n                                                           By: 林中水滴"
            print "--------------------------------------------------------------------------------"
            main()
        except pefile.PEFormatError:
            print "\n================================================================================"
            print "@Author: xuzhijian17 2011 PE File Filter command Tool"
            print "Copyright (c) 1990 - 2011 Qianyun Technologies"
            print "Program version 10.0.1388, engine 10.0.1516"
            print "Version 1516/3730 ",strftime("%Y-%m-%d %H:%M:%S") 
            print "================================================================================\n"
            print "\t\t------------------------------------"
            print "\t\t\tThis is not a PE file!"
            print "\t\t------------------------------------"
            print "\n                                                           By: 林中水滴"
            print "--------------------------------------------------------------------------------"
            main()
        except WindowsError:
            print "\n================================================================================"
            print "@Author: xuzhijian17 2011 PE File Filter command Tool"
            print "Copyright (c) 1990 - 2011 Qianyun Technologies"
            print "Program version 10.0.1388, engine 10.0.1516"
            print "Version 1516/3730 ",strftime("%Y-%m-%d %H:%M:%S") 
            print "================================================================================\n"
            print "\t\t------------------------------------"
            print "\t\t\tThis File is Empty!"
            print "\t\t------------------------------------"
            print "\n                                                           By: 林中水滴"
            print "--------------------------------------------------------------------------------"
            main()
    
    else:
        f=open("MD5.txt",'w')
        '''
        if not os.path.isdir(dstDir):
            os.makedirs(dstDir)
        '''
        for x,y,z in os.walk(srcDir):
            for i in z:
                try:
                    pefile.PE(os.path.join(x,i))
                    md5=hashlib.md5(open(os.path.join(x,i),'rb').read()).hexdigest()
                    f.write(md5+'\n')
                    print "PE文件名："+i+" MD5值："+md5
                except pefile.PEFormatError:
                    #shutil.copy2(os.path.join(x,i),dstDir)
                    try:
                        os.chmod(os.path.join(x,i),stat.S_IWRITE) # 改为可写权限
                        os.remove(os.path.join(x,i))
                        print "删除非PE文件..."+i
                    except:
                        sleep(0.1)
                        os.chmod(os.path.join(x,i),stat.S_IWRITE) # 改为可写权限
                        os.remove(os.path.join(x,i))
                        print "删除非PE文件..."+i
                except WindowsError:
                    try:
                        os.chmod(os.path.join(x,i),stat.S_IWRITE) # 改为可写权限
                        os.remove(os.path.join(x,i))
                        print "删除空文件..."+i
                    except:
                        sleep(0.1)
                        os.chmod(os.path.join(x,i),stat.S_IWRITE) # 改为可写权限
                        os.remove(os.path.join(x,i))
                        print "删除空文件..."+i
                except:
                    continue     
        f.close()
        main()
        
def archives(srcDir,dstDir):
    
        if not os.path.isdir(dstDir):
            os.makedirs(dstDir)
        
        print "\n\t本程序将自动过滤非PE的文件到文件夹‘archives’下\n"
  
        f=open("MD5.txt",'w')
        for x,y,z in os.walk(srcDir):
            for i in z:
                try:
                    pefile.PE(os.path.join(x,i))
                    md5=hashlib.md5(open(os.path.join(x,i),'rb').read()).hexdigest()
                    f.write(md5+'\n')
                    print "PE文件名："+i+" MD5值："+md5
                except pefile.PEFormatError:
                    try:
                        os.chmod(os.path.join(x,i),stat.S_IWRITE)
                        shutil.copy2(os.path.join(x,i),dstDir)
                        print "过滤非PE文件..."+i+"...到arvhices文件夹下"
                    except:
                        pass
    
                except:
                    continue     
        f.close()
        main()
            
def main():
    raw=raw_input("直接拖曳文件到此处:")
    cwd=os.getcwd()
    if raw=='':
        archives(cwd,'archives')
    else:
        archive(raw)
        
if __name__=='__main__':
    print "================================================================================"
    print "@Author: xuzhijian17 2011 PE File Filter command Tool"
    print "Copyright (c) 1990 - 2011 Qianyun Technologies"
    print "Program version 10.0.1388, engine 10.0.1516"
    print "Version 1516/3730 ",strftime("%Y-%m-%d %H:%M:%S") 
    print "================================================================================"
    print "                  This is a PE File Filter command Tool"
    print "\n\t本程序是一个对非PE文件进行过滤并计算MD5值的小程序。具体功能如下：\n"
    print "\n\t1.支持对单个文件的判断，判断是否为PE文件。并求出PE文件的HASH值。"
    print "\n\t2.支持对文件夹的判断，删除文件夹内的非PE文件，并求出PE文件的MD5值，保存到当前目录下。(文件名为:‘MD5.txt’)"
    print "\n\t3.如要对非PE文件进行保存，需将本程序放在要进行过滤的文件夹的根目录下，直接按回车键进行过滤，过滤出来非PE文件将保存到同目录下。(文件夹名为:‘archives’)"
    print "\n                                                             By: 林中水滴"
    print "--------------------------------------------------------------------------------"
    main()
