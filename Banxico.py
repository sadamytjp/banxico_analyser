from mrjob.job import MRJob


class Word_count(MRJob):
    def mapper(self, _, line):
        for word in line.split():
            if word.lower() == "inflación":
                yield "inflacion", 1
            if word.lower()=="crecimiento":
                yield "crecimiento", 1
            if word.lower()=="apreciación":
                yield "apreciacion", 1
            if word.lower()=="depreciación":
                yield "depreciacion", 1
            if word.lower()=="moneda":
                yield "moneda", 1
            if word.lower()=="volatilidad":
                yield "volatilidad", 1
            if word.lower()=="holgura":
                yield "holgura", 1
            if word.lower()=="estable":
                yield "estable", 1
            if word.lower()=="disminuir":
                yield "disminuir", 1
            if word.lower()=="aumentar":
                yield "aumentar", 1
            if word.lower()=="mantener":
                yield "mantener", 1
            if word.lower()=="deterioro":
                yield "deterioro", 1
            if word.lower()=="lasitud":
                yield "lasitud", 1
             

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == "__main__":
    Word_count.run()
