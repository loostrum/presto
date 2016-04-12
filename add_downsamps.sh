filebase=${1}_SAP0_BEAM0
file=${filebase}.singlepulse

tmpfile=downsamps

# backup infile
cp $file ${filebase}_old.singlepulse
# read DMs
DMlist=`grep -v \# $file | awk '{print $1}'`
# Get downsamps from DMs
get_downsamp.py $DMlist > $tmpfile
# Merge 
paste -d'\t' $file $tmpfile > ${filebase}_ex.singlepulse
mv ${filebase}_ex.singlepulse $file
rm $tmpfile

exit 0
