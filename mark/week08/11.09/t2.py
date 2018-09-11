def get_score(self):
    print(self.__class__.__name__)
    return dict(name=self.__class__.__name__, English=88, Chinese=90, History=85)


# gt = get_score('Person')
# print(gt)
