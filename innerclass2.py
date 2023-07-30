class ai:
    def __init__(self):
        self.ml="algorithms"
        self.nlp="sentiments"
        self.dl="understanding"
        self.structure=self.ds()
        
    def show(self):
        print(self.ml,self.nlp,self.dl)
        self.structure.show()
        
    class ds:
        def __init__(self):
            self.math="statics"
            self.code="python"
            self.visualize ="ms-excel"
        
        def show(self):
            print(self.math,self.code,self.visualize )
s1=ai()
s2=ai()
s1.show() 
s2.show()          