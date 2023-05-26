import openpyxl

test_column = 4 # 设成2是测原始SentiStrength，4是测tool列
all_count = 4423
pos_intersection = 0
neg_intersection = 0
neu_intersection = 0

wb = openpyxl.load_workbook("test.xlsx")
ws = wb["sof4423"]
ws = list(ws.values)

for line in ws:
    if line[3] == line[test_column]:
        if line[3] == 1:
            pos_intersection += 1
        elif line[3] == 0:
            neu_intersection += 1
        elif line[3] == -1:
            neg_intersection += 1

print("overall_accuracy : " + str((pos_intersection + neg_intersection + neu_intersection) / all_count))



