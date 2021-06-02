class Call1:
    def __call__(self, *args, **kwargs):
        print("누가 날 불렀네")
ob = Call1()
ob()