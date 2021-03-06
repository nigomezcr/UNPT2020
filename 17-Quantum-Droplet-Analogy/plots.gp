set terminal pdf

set arrow from 60, graph 0 to 60, graph 1 nohead
set arrow from -60, graph 0 to -60, graph 1 nohead
set yrange [-110:110]
set xrange [-110:110]
set xlabel "x [mm]"
set ylabel "z [mm]"
set output "z-x.pdf"
p 'data.txt' u 2:4 t "Up view" w l lt 7, 60 t "" black , -60 t "" black 

unset arrow
set yrange [0:2]
set output "y-x.pdf"
set xlabel "x[mm]"
set ylabel "y[mm]"
p 'data.txt' u 2:3 t "Front view" w l lt 4

set xlabel "z [mm]"
set output "y-z.pdf"
p 'data.txt' u 4:3 t "Side view" w l lt 5

set output "x-t.pdf"
set xlabel "t [ms]"
set ylabel "x [mm]"
p 'data.txt' u 1:2 t "x-t" w l lt 1

set ylabel "y [mm]"
set output "y-t.pdf"
p 'data.txt' u 1:3 t "y-t" w l lt 2

set ylabel "z [mm]"
set output "z-t.pdf"
p 'data.txt' u 1:4 t "z-t" w l lt 3

