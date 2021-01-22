import json
# Can make user input
# start = 9801
# end = 3801
#
# while end < 10000:
#     end = end - 1
#     start = start - 1
#     with open("otp_list_"+ str(start+1)+"_"+str(end)+".txt", "w") as f:
#         start = start + 1
#         end = end + 1
#         f.write("\n".join(['{0:04}'.format(num) for num in range(start, end)]))
#         start = start + 200
#         end = end + 200

number = ['{0:04}'.format(num) for num in range(0000, 10000)]

with open("otp_list_0000_9999", "w") as f:
    json.dump(number, f) 
    #f.write("\n".join(['{0:04}'.format(num) for num in range(0000, 10000)]))
