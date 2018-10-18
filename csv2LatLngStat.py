import csv
import sys

args = sys.argv

num_lines = len(open(args[1]).readlines()) - 1

with open('outLatLngStat.txt', 'w') as f_out:
    with open(str(args[1]), 'r') as f_csv:
        reader = csv.reader(f_csv)
        header = next(reader)

        f_out.write("var markerData = [" + "\n")

        n = 1

        for row in reader:

            print(row)

            f_out.write(" " * 18)
            f_out.write("{" + "lat: " + row[1] + ", " + "lng: " + row[2] + ", " + "stat: " + row[0] + "}")
            if n != num_lines:
                f_out.write("," + "\n")
            else:
                f_out.write("\n")

            n += 1

    f_out.write(" " * 18)
    f_out.write("];")