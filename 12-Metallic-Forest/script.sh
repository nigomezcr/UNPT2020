dir="Images/"

for i in $dir*; do
    ./x.read_image $i
    gnuplot -e "filename='Data_FD/"${i:7:-4}"'" plot.gp > data.csv
done 
