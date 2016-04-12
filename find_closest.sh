if [[ ! "$#" -eq "1" ]]; then
    echo "Please provide folder containing subbands"
    exit 1
fi

DATADIR=$1

SUBDMS=$(ls ${DATADIR}/*.sub000 | awk -F DM '{print $2}' | awk -F.sub000 '{print $1}' | sort -n)

echo $SUBDMS | gawk --use-lc-numeric -v target=$1 '
    function abs(val) { return (val < 0 ? -1*val : val) }

{
 min = abs($1 - target)
 min_idx = 1
 for (i=2; i<NF; i++) {
  diff = abs($i - target)
  if (diff < min) {
   min = diff
   min_idx = i
  }
 }
 print $min_idx
}'
