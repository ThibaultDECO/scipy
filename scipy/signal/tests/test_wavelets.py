import numpy as N
from scipy.testing import *

from scipy.signal import wavelets


class TestWavelets(TestCase):
    def test_qmf(self):
        assert_array_equal(wavelets.qmf([1,1]),[1,-1])

    def test_daub(self):
        for i in xrange(1,15):
            assert_equal(len(wavelets.daub(i)),i*2)

    def test_cascade(self):
        for J in xrange(1,7):
            for i in xrange(1,5):
                lpcoef = wavelets.daub(i)
                k = len(lpcoef)
                x,phi,psi = wavelets.cascade(lpcoef,J)
                assert len(x) == len(phi) == len(psi)
                assert_equal(len(x),(k-1)*2**J)

    def test_morlet(self):
        x = wavelets.morlet(50,4.1,complete=True)
        y = wavelets.morlet(50,4.1,complete=False)
        assert_equal(len(x),len(y))

        x = wavelets.morlet(10,50,complete=False)
        y = wavelets.morlet(10,50,complete=True)
        assert_equal(x,y)

if __name__ == "__main__":
    nose.run(argv=['', __file__])
