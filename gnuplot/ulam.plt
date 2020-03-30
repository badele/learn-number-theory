set terminal pngcairo size width,width enhanced font 'Verdana,10'
set output filename

# Reset figure
reset
set size 1,1
set margins 0,0,0,0
set border linewidth 0
unset border
unset key
unset colorbox
unset tics

#set palette gray negative
set palette model RGB
#set palette model RGB defined (0 "#000000", 1 "#FF00FF", 2 "#FF0000", 3 "#FFFF00", 5 "#00FF00" , 99 "#888888" )
set palette model RGB defined (0 "#000000", 1 "#FF00FF", 2 "#888888", 3 "#808000", 4 "#FFFF00" )
#set palette model RGB defined (0 "#000000", 1 "#FF00FF",  9999999 "#FFFF00" )

# Plot
plot "/tmp/ulam.txt" using (-$1):($2):($3) matrix with image notitle

# [Optional] show matrix numbers
#plot "/tmp/ulam.txt" using (-$1):($2):($3) matrix with image notitle,'' matrix using (-$1):($2):(sprintf('%d', $3)) with labels notitle font ',6'
