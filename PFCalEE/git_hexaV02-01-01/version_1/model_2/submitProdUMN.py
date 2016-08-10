#!/usr/bin/env python

import os,sys
import optparse
import commands
import math
import random
import subprocess

random.seed()

usage = 'usage: %prog [options]'
parser = optparse.OptionParser(usage)
parser.add_option('-E', '--energy'      ,    dest='energy'             , help='set energy'                   , default=1,      type=int)
parser.add_option('-m', '--model'       ,    dest='model'              , help='set model'                    , default=0,      type=int)
parser.add_option('-b', '--Bfield'      ,    dest='Bfield'             , help='B field value in Tesla'       , default=0,      type=float)
parser.add_option('-f', '--datafile'    ,    dest='datafile'           , help='full path to input file', default='/local/cms/hiltbran/standalone_sim/PFCalEE/neutron_events/myFile.lhe')
parser.add_option('-n', '--nevts'       ,    dest='nevts'              , help='number of events to generate' , default=15,    type=int)
parser.add_option('-o', '--out'         ,    dest='out'                , help='output directory'             , default=os.getcwd() )
parser.add_option('-e', '--eos'         ,    dest='eos'                , help='eos path to save root file to EOS',         default='')
parser.add_option('-g', '--gun'         ,    action="store_true",  dest='dogun'              , help='use particle gun.')
parser.add_option('-S', '--no-submit'   ,    action="store_true",  dest='nosubmit'           , help='Do not submit batch job.')
(opt, args) = parser.parse_args()

bval="BOFF"
if opt.Bfield>0 : bval="BON" 

outDir = os.getcwd()

#wrapper
scriptFile = open('%s/runJob.sh'%outDir, 'w')
scriptFile.write('#!/bin/bash\n')
scriptFile.write('source /data/cmszfs1/sw/HGCAL_SIM_A/setup.sh\n')
scriptFile.write('cp %s/g4steer.mac .\n'%outDir)
scriptFile.write('PFCalEE g4steer.mac | tee g4.log\n')
scriptFile.write('mv PFcal.root HGcal_%s.root\n'%(outTag))
scriptFile.write('localdir=`pwd`\n')
scriptFile.write('echo "--Local directory is " $localdir >> g4.log\n')
scriptFile.write('ls * >> g4.log\n')
if len(opt.eos)>0:
    scriptFile.write('grep "alias eos=" /afs/cern.ch/project/eos/installation/cms/etc/setup.sh | sed "s/alias /export my/" > eosenv.sh\n')
    scriptFile.write('source eosenv.sh\n')
    scriptFile.write('$myeos mkdir -p %s\n'%eosDir)
    scriptFile.write('cmsStage -f HGcal_%s.root %s/HGcal_%s.root\n'%(outTag,eosDir,outTag))
    scriptFile.write('if (( "$?" != "0" )); then\n')
    scriptFile.write('echo " --- Problem with copy of file PFcal.root to EOS. Keeping locally." >> g4.log\n')
    scriptFile.write('else\n')
    scriptFile.write('eossize=`$myeos ls -l %s/HGcal_%s.root | awk \'{print $5}\'`\n'%(eosDir,outTag))
    scriptFile.write('localsize=`ls -l HGcal_%s.root | awk \'{print $5}\'`\n'%(outTag))
    scriptFile.write('if (( "$eossize" != "$localsize" )); then\n')
    scriptFile.write('echo " --- Copy of sim file to eos failed. Localsize = $localsize, eossize = $eossize. Keeping locally..." >> g4.log\n')
    scriptFile.write('else\n')
    scriptFile.write('echo " --- Size check done: Localsize = $localsize, eossize = $eossize" >> g4.log\n')
    scriptFile.write('echo " --- File PFcal.root successfully copied to EOS: %s/HGcal_%s.root" >> g4.log\n'%(eosDir,outTag))
    scriptFile.write('rm HGcal_%s.root\n'%(outTag))
    scriptFile.write('fi\n')
    scriptFile.write('fi\n')

scriptFile.write('echo "--deleting core files: too heavy!!"\n')
scriptFile.write('rm core.*\n')
scriptFile.write('echo "All done"\n')
scriptFile.close()

#write geant 4 macro
g4Macro = open('%s/g4steer.mac'%(outDir), 'w')
g4Macro.write('/control/verbose 0\n')
g4Macro.write('/run/verbose 0\n')
g4Macro.write('/event/verbose 0\n')
g4Macro.write('/tracking/verbose 0\n')
g4Macro.write('/N03/det/setField %1.1f T\n'%opt.Bfield)
g4Macro.write('/N03/det/setModel %d\n'%opt.Model)
if opt.dogun: 
    g4Macro.write('/generator/select particleGun\n')
    g4Macro.write('/gun/energy %s GeV\n'%(opt.energy))
    g4Macro.write('/gun/particle %s\n'%(opt.datatype))
else :
    g4Macro.write('/filemode/inputFilename %s\n'%(opt.datafile))
    g4Macro.write('/run/initialize\n')
    g4Macro.write('/run/beamOn %d\n'%(opt.nevts))
g4Macro.close()

#submit
"""
condorSubmit = open('%s/condorSubmit'%(outDir), 'w')
condorSubmit.write('Executable          =  %s\n' % scriptFile.name)
condorSubmit.write('Universe            =  vanilla\n')
condorSubmit.write('Requirements        =  Arch=="X86_64"  &&  (Machine  !=  "zebra01.spa.umn.edu")  &&  (Machine  !=  "zebra02.spa.umn.edu")  &&  (Machine  !=  "zebra03.spa.umn.edu")  &&  (Machine  !=  "zebra04.spa.umn.edu")\n')
condorSubmit.write('+CondorGroup        =  "cmsfarm"\n')
condorSubmit.write('getenv              =  True\n')
condorSubmit.write('Log         =  %s.log\n' % outDir)
condorSubmit.write('Queue 1\n')
condorSubmit.close()

os.system('chmod u+rwx %s/runJob.sh'%outDir)
command = "condor_submit " + condorSubmit.name + '\n'
if opt.nosubmit : os.system('echo ' + command) 
else: subprocess.call(command.split())
"""
