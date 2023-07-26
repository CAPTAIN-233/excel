class Result_excel_file:
    def __init__(self):
        __file_path = os.path.dirname(os.path.realpath(__file__))
        __result_file_name = "result_%s.xlsx" % time.strftime('%Y-%m-%d-%H%M%S')
        self.result_file = os.path.join(__file_path, 'result', __result_file_name)
        shutil.copy("./templates/result_template.xlsx", self.result_file)
        self.workbook = load_workbook(self.result_file)

    def sort_result_to_resultsheet(self):
        sheet1 = self.workbook["tempsheet"]
        resultsheet = self.workbook["resultsheet"]
        # 获取tempsheet页的所有行，并去掉标题行, 并按照ip地址进行排序
        ws_rows = [i for i in list(sheet1.rows) if i[0].value != "主机IP"]
        ws_rows= sorted(ws_rows, key=lambda x: ''.join([i.rjust(3, '0') for i in x[0].value.split('.')]))
        # 将获取到的行，连同单元格样式，一起复制到resultsheet中
        for i, row in enumerate(ws_rows):
            for j, source_cell in enumerate(row):
                target_cell = resultsheet.cell(i+2, j+1)
                target_cell.value = source_cell.value
                if source_cell.has_style:
                    target_cell._style = copy(source_cell._style)
                    target_cell.font = copy(source_cell.font)
                    target_cell.border = copy(source_cell.border)
                    target_cell.fill = copy(source_cell.fill)
                    target_cell.number_format = copy(source_cell.number_format)
                    target_cell.protection = copy(source_cell.protection)
                    target_cell.alignment = copy(source_cell.alignment)
        # 给值加上框线
        border = Border(left=Side(border_style='thin', color='000000'),
                        right=Side(border_style='thin', color='000000'),
                        top=Side(border_style='thin', color='000000'),
                        bottom=Side(border_style='thin', color='000000'))
        for row in resultsheet.rows:
            for cell in row:
                cell.border = border
        # 保存表格
        self.save_workbook()

    def save_workbook(self):
        self.workbook.save(self.result_file)
