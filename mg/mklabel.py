
#!/usr/bin/python

import os

import sys

ct='/usr/atria/bin/cleartool '

aa='// _ /'

bb=’’

if len(sys.argv)==1:

    label = raw_input('Please input label name:')

    else:

        label=sys.argv[1]

	co_ret=os.popen('cd '+mgcvob+';'+ct+'lsco -all -cview').read()

if co_ret!='':

    print '\n**********  Please checkin your code first!   **********  \n'

    print co_ret

    sys.exit()

    mgc_ret=os.system('cd '+mgcvob+';'+ct+'lstype lbtype:'+label)

    mopot_ret=os.system('cd '+mopotvob+';'+ct+'lstype lbtype:'+label)

    a=''

    b=''

if a _ret==0:

    a=raw_input('Label already exists . Replace? (yes/no):')

if b_ret==0:

    b=raw_input('Label already exists vob. Replace? (yes/no):')

if a=='yes' or a=='y':

    os.system('cd '+mgcvob+';'+ct+'mklabel -r -replace '+label+' .')

if b=='yes' or b=='y':

   os.system('cd '+mopotvob+';'+ct+'mklabel -r -replace '+label+' .')

if a_ret!=0:

   os.system('cd '+aa +';'+ct+'mklbtype -nc '+label)

   os.system('cd '+bb+';'+ct+'mklabel -r '+label+' .')

if b_ret!=0:

   os.system('cd '+aa+';'+ct+bb -nc '+label)

   os.system('cd '+aa+';'+ct+'mklabel -r '+label+' .')

   dir ="//cs/"

   import commands

   build_num = commands.getoutput("echo $BUILD_NUMBER")

   fp=open( dir+"label"+build_num+".txt", "w+")

   fp.write("element * CHECKEDOUT\nelement * " + label + "\nload”)

   fp.close()
