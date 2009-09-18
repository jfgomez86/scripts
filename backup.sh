#!/bin/sh 
# directory to backup
BDIR=/home/josesito

# excludes file - this contains a wildcard pattern per line of files to exclude
INCLUDES=/home/josesito/system/config/include-in-backup.txt

########################################################################

BACKUPDIR="/home/josesito/backups/"
OPTS="--include-from=$INCLUDES --delete -av"

# now the actual transfer
echo "Running ... "
echo "rsync $OPTS $BDIR $BACKUPDIR"
rsync $OPTS $BDIR $BACKUPDIR

