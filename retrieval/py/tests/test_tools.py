from src.tools import Tools
import numpy.testing as npt
import numpy as np

vocab = ['a', 'able', 'accepted', 'always', 'and', 'annoyances', 'are', 'as', 'avoided',
         'be', 'beguiled', 'being', 'belongs', 'best', 'blame', 'blinded', 'bound', 'business',
         'but', 'by', 'cannot', 'cases', 'certain', 'charms', 'choice', 'circumstances', 'claims',
         'demoralized', 'denounce', 'desire', 'dislike', 'distinguish', 'do', 'duty', 'easy',
         'ensue', 'equal', 'every', 'fail', 'foresee', 'free', 'frequently', 'from', 'greater',
         'hand', 'have', 'he', 'holds', 'hour', 'in', 'indignation', 'is', 'it', 'like', 'man',
         'matters', 'men', 'moment', 'nothing', 'obligations', 'occur','of', 'on', 'or', 'other',
         'our', 'owing', 'pain', 'perfectly', 'pleasure', 'pleasures', 'power', 'prevents',
         'principle', 'rejects', 'repudiated', 'righteous', 'same', 'saying', 'secure', 'selection',
         'shrinking', 'simple', 'so', 'that', 'the', 'their', 'therefore', 'these', 'they', 'this',
         'those', 'through', 'to', 'toil', 'trouble', 'untrammelled', 'we', 'weakness', 'welcomed',
         'what', 'when', 'which', 'who', 'will', 'wise', 'with']

docs = ["on the other hand we denounce with righteous indignation and dislike men who are so beguiled",
    "and demoralized by the charms of pleasure of the moment so blinded by desire that they cannot",
    "foresee the pain and trouble that are bound to ensue and equal blame belongs to those who fail",
    "in their duty through weakness of will which is the same as saying through shrinking from toil",
    "and pain these cases are perfectly simple and easy to distinguish in a free hour",
    "when our power of choice is untrammelled and when nothing prevents",
    "our being able to do what we like best every pleasure is to be welcomed and every pain avoided",
    "but in certain circumstances and owing to the claims of duty or the obligations of business",
    "it will frequently occur that pleasures have to be repudiated and annoyances accepted",
    "the wise man therefore always holds in these matters to this principle of selection"
    ]

class TestTools(object):
    def test_idf(self):
        t = Tools()
        idf_doc = t.idf(docs, vocab)
        npt.assert_almost_equal(idf_doc[0], -0.09531018, decimal=5)

    def test_tf(self):
        t = Tools()
        tf = t.tf(docs, vocab)
        assert(tf[0] == 1)