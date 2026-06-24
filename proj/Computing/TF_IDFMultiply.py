from Computing.TF_IDF import TF_IDF


class TF_IDFMultiply(TF_IDF):
    """
    calculates tf_idf by multiplying the tf and idf values
    """

    def calc_tf_idf(self, term: str, doc_id: str) -> float:
        tf_value = self.tf[term][doc_id]
        idf_value = self.idf[term]
        return tf_value * idf_value