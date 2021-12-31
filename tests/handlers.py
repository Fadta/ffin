import unittest as ut
import ffin
import ffin.handlers as fh


class TestFileIO(ut.TestCase):

    def test_verify_filename(self):
        handler = fh.TickerIOHandler(ffin.HOME_DIR)

        self.assertFalse(handler.verify_filename('.'))

        self.assertTrue(handler.verify_filename('something.csv'))
        self.assertTrue(handler.verify_filename('something2.csv'))
        self.assertTrue(handler.verify_filename('something_3.csv'))
        self.assertTrue(handler.verify_filename('something'))
        self.assertTrue(handler.verify_filename('2something'))
        self.assertTrue(handler.verify_filename('3_something'))
        self.assertTrue(handler.verify_filename('/subfolder/'))
        self.assertTrue(handler.verify_filename('/subfolder/filename.som'))
        self.assertTrue(handler.verify_filename('/subfolder/filename'))


if __name__ == '__main__':
    ut.main()
