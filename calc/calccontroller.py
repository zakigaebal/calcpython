class CalcController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        # self.view.btn_equal_slot(self.f)

    def f(self):
        sn1 = self.view.getNum1()
        sn2 = self.view.getNum2()
        sn = self.model.sum(sn1, sn2)
        self.view.setResult(sn)

