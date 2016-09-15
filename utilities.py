def dateParse(date):
    dateStr = str(date)
    dateArray = dateStr.split('-')
    if (len(dateArray) != 3):
        return date
    else:
        return dateArray[1]+"\\" + dateArray[2] + "\\" + dateArray[0]