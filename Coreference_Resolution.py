from allennlp.predictors.predictor import Predictor
predictor = Predictor.from_path("coref-model-2018.02.05.tar.gz")
dict = (predictor.predict(document="Paul Allen was born on January 21, 1953, in Seattle, Washington, to Kenneth Sam Allen and Edna Faye Allen. Allen attended Lakeside School, a private school in Seattle, where he befriended Bill Gates, two years younger, with whom he shared an enthusiasm for computers. Paul and Bill used a teletype terminal at their high school, Lakeside, to develop their programming skills on several time-sharing computer systems."))


def coreference_resolution():
    for k, v in dict.items():
        if k == 'document':
            token_Sent = v
            for i, item in enumerate(token_Sent, start=0):
                print(i, item)

        if k == 'clusters':
            dict_list = {}
            for list in v:
                key =(list[0])
                value = (list[1:])
                dict_list[tuple(key)]= value
    dict_list["words"] = token_Sent
    print(dict_list)


if __name__ == '__main__':
    coreference_resolution()

