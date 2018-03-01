start_time = int(raw_input())
final_time = start_time + int(raw_input())
other_start = int(raw_input())
other_final = other_start + int(raw_input())
if (other_start > start_time and other_start < final_time or
        other_final > start_time and other_final < final_time):
    print "True"
else:
    print "False"