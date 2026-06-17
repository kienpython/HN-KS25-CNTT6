from datetime import datetime
def evaluate_flex_time(attendance_book):
    for attendance in attendance_book:
        if not attendance['times'][1]:
            continue 
        clock_in = datetime.strptime(attendance['times'][0],"%H:%M")
        clock_out = datetime.strptime(attendance['times'][1],"%H:%M")
        limit_time = datetime.strptime("10:00","%H:%M")
        if clock_in > limit_time :
            print(f"{attendance['id']} - Vi phạm: Đến muộn quá 90 phút.")
            continue
        if (clock_out - clock_in).total_seconds()/3600 < 9:
            print(f"{attendance['id']} - Vi phạm: Về sớm, chưa hoàn thành đủ 9 tiếng bù giờ.")
        # clock_in = attendance['times'][0]
        # clock_in_seconds = int(clock_in.split(":")[0])*60*60 +  int(clock_in.split(":")[1])*60 #[hour, phut]
        # clock_out = attendance['times'][1]
        # clock_out_seconds = int(clock_out.split(":")[0])*60*60 +  int(clock_out.split(":")[1])*60 #[hour, phut]
        # if (clock_out_seconds - clock_in_seconds)/3600 <9 :
        #     print(f"{attendance['id']} - Vi phạm: Về sớm, chưa hoàn thành đủ 9 tiếng bù giờ.")  
        else:
            print(f"{attendance['id']} - Hợp lệ: Hoàn thành ca làm việc.")