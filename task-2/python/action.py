class Action(object):
    def generate_report(self):
        pass

class ActionWithTabularData(Action):

    _data_reader = None
    _report = None

    def set_report(report):
        """
        Method for action report object reset
        """
        self._report = report

    def generate_report():
        """
        Method for action report generation
        """
        data = self._data_reader.loadTabularData()
        self._report.drawTabularData(data)




class ActionWithTabularData(Action):

    _report = None

    def set_report(report):
        """
        Method for action report object reset
        """
        self._report = report

    def loadTabularData(self):
        """
        Abstract method for Action data loading
        """
        pass

    def generate_report():
        """
        Method for action report generation
        """
        data = self.loadTabularData()
        self._report.drawTabularData(data)

class D(ActionWithTabularData):

    _report = GraphReport()

    def _loadTabularData(self):
        """
        Implemenatation of data preprocessing for current action
        """

class ActionWithHeaderFooter(Action):

    def generate_report(self):
        """
        Implementation of report with headers and footers
        """


def main():
    #Example of report type modification
    graph = GraphReport()
    table = TableReport()
    diagram = DiagramReport()

    d_action = D()
    #get default "graph" report for D action
    d_action.generate_report()

    d_action.set_report(table)
    #get "table" report for D action
    d_action.generate_report()

    d_action.set_report(diagram)
    #get "diagram" report for D action
    d_action.generate_report()

    pass

if __name__ == '__main__':
    main()
