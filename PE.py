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
            print "   MD5ֵ:",hashlib.md5(open(srcDir,'rb').read()).hexdigest()
            print "\n  SHA1ֵ:",hashlib.sha1(open(srcDir,'rb').read()).hexdigest()                         
            print "\nSHA224ֵ:",hashlib.sha224(open(srcDir,'rb').read()).hexdigest()
            print "\nSHA256ֵ:",hashlib.sha256(open(srcDir,'rb').read()).hexdigest()
            print "\nSHA384ֵ:",hashlib.sha384(open(srcDir,'rb').read()).hexdigest()
            print "\nSHA512ֵ:",hashlib.sha512(open(srcDir,'rb').read()).hexdigest()
            print "\n                                                           By: ����ˮ��"
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
            print "\n                                                           By: ����ˮ��"
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
            print "\n                                                           By: ����ˮ��"
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
                    print "PE�ļ�����"+i+" MD5ֵ��"+md5
                except pefile.PEFormatError:
                    #shutil.copy2(os.path.join(x,i),dstDir)
                    try:
                        os.chmod(os.path.join(x,i),stat.S_IWRITE) # ��Ϊ��дȨ��
                        os.remove(os.path.join(x,i))
                        print "ɾ����PE�ļ�..."+i
                    except:
                        sleep(0.1)
                        os.chmod(os.path.join(x,i),stat.S_IWRITE) # ��Ϊ��дȨ��
                        os.remove(os.path.join(x,i))
                        print "ɾ����PE�ļ�..."+i
                except WindowsError:
                    try:
                        os.chmod(os.path.join(x,i),stat.S_IWRITE) # ��Ϊ��дȨ��
                        os.remove(os.path.join(x,i))
                        print "ɾ�����ļ�..."+i
                    except:
                        sleep(0.1)
                        os.chmod(os.path.join(x,i),stat.S_IWRITE) # ��Ϊ��дȨ��
                        os.remove(os.path.join(x,i))
                        print "ɾ�����ļ�..."+i
                except:
                    continue     
        f.close()
        main()
        
def archives(srcDir,dstDir):
    
        if not os.path.isdir(dstDir):
            os.makedirs(dstDir)
        
        print "\n\t�������Զ����˷�PE���ļ����ļ��С�archives����\n"
  
        f=open("MD5.txt",'w')
        for x,y,z in os.walk(srcDir):
            for i in z:
                try:
                    pefile.PE(os.path.join(x,i))
                    md5=hashlib.md5(open(os.path.join(x,i),'rb').read()).hexdigest()
                    f.write(md5+'\n')
                    print "PE�ļ�����"+i+" MD5ֵ��"+md5
                except pefile.PEFormatError:
                    try:
                        os.chmod(os.path.join(x,i),stat.S_IWRITE)
                        shutil.copy2(os.path.join(x,i),dstDir)
                        print "���˷�PE�ļ�..."+i+"...��arvhices�ļ�����"
                    except:
                        pass
    
                except:
                    continue     
        f.close()
        main()
            
def main():
    raw=raw_input("ֱ����ҷ�ļ����˴�:")
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
    print "\n\t��������һ���Է�PE�ļ����й��˲�����MD5ֵ��С���򡣾��幦�����£�\n"
    print "\n\t1.֧�ֶԵ����ļ����жϣ��ж��Ƿ�ΪPE�ļ��������PE�ļ���HASHֵ��"
    print "\n\t2.֧�ֶ��ļ��е��жϣ�ɾ���ļ����ڵķ�PE�ļ��������PE�ļ���MD5ֵ�����浽��ǰĿ¼�¡�(�ļ���Ϊ:��MD5.txt��)"
    print "\n\t3.��Ҫ�Է�PE�ļ����б��棬�轫���������Ҫ���й��˵��ļ��еĸ�Ŀ¼�£�ֱ�Ӱ��س������й��ˣ����˳�����PE�ļ������浽ͬĿ¼�¡�(�ļ�����Ϊ:��archives��)"
    print "\n                                                             By: ����ˮ��"
    print "--------------------------------------------------------------------------------"
    main()
