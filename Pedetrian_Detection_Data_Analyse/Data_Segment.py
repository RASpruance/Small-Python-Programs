import xlwt
import xlrd
f = open('Detected_pixels.txt')
txt = f.read()
txt_split_1st=txt.split('+')

workbook = xlwt.Workbook()
# http://xlwt.readthedocs.io/en/latest/
sheet1 = workbook.add_sheet('height',cell_overwrite_ok=True)
sheet2 = workbook.add_sheet('width',cell_overwrite_ok=True)
i=1
for line in txt_split_1st:
    if line !='' :
        result_of_a_bounding_box=line.split('|')
        TopLeftX=result_of_a_bounding_box[0]
        TopLeftY=result_of_a_bounding_box[1]
        BottumRightX=result_of_a_bounding_box[2]
        BottumRightY=result_of_a_bounding_box[3]
        height=(int(TopLeftY)-int(BottumRightY))*(-1)
        width=(int(TopLeftX)-int(BottumRightX))*(-1)
        print("height = ")
        print(str(height))
        print("width = ")
        print(str(width))
        sheet1.write(i,1,height)
        sheet2.write(i,2,width)
        i=i+1
    else:
        break




# data = xlrd.open_workbook('Ped_Detect.xlsx')
workbook.save('Ped_Detect.xlsx')
print("End of program")
