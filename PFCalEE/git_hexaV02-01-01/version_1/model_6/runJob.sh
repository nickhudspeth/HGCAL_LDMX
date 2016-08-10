#!/bin/bash
source /afs/cern.ch/user/n/nmorrow/HGCAL_LDMX/PFCalEE/g4env.sh
cp /afs/cern.ch/user/n/nmorrow/HGCAL_LDMX/PFCalEE/git_hexaV02-01-01/version_1/model_6//g4steer.mac .
PFCalEE g4steer.mac 1 6 0.000000 /afs/cern.ch/user/o/ocolegro/HGCAL_LDMX/PFCalEE/data/mom.txt| tee g4.log
mv PFcal.root HGcal__version1_model6.root
localdir=`pwd`
echo "--Local directory is " $localdir >> g4.log
ls * >> g4.log
echo "--deleting core files: too heavy!!"
rm core.*
cp * /afs/cern.ch/user/n/nmorrow/HGCAL_LDMX/PFCalEE/git_hexaV02-01-01/version_1/model_6//
echo "All done"
