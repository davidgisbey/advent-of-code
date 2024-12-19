from app.data.day_two_reports import DayTwoReports

class DayTwo:
    def format_report_data(self):
      lines = DayTwoReports.REPORT_DATA.strip().split("\n")
      return [[int(element) for element in line.split()] for line in lines]

    def calculate_safe_reports(self, reports):
        count = 0

        for report in reports:
            if self.__is_safe_report(report):
                count += 1
            else:
                if self.__can_be_safe_with_removal(report):
                    count += 1

        return count

    def __is_safe_report(self, report):
        return self.__check_report_safe(report, mode="ascending") or \
               self.__check_report_safe(report, mode="descending")

    def __check_report_safe(self, report, mode="ascending"):

        for i in range(len(report) - 1):
            current_int = report[i]
            next_int = report[i + 1]
            if (mode == "ascending" and (next_int <= current_int or next_int > current_int + 3)) or \
               (mode == "descending" and (next_int >= current_int or next_int < current_int - 3)):
                return False

        return True

    def __can_be_safe_with_removal(self, report):
        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1:]
            if self.__is_safe_report(modified_report):
                return True
        return False
