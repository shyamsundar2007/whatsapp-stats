import unittest 
import whatsappStats

class WhatsappExportTypeTestCase(unittest.TestCase):
    def test_export_sample_1(self):
        whatsappStats.main('export_sample_1.txt')
        self.assertEqual(len(whatsappStats.messageList), 50)

    def test_export_sample_2(self):
        whatsappStats.main('export_sample_2.txt')
        self.assertEqual(len(whatsappStats.messageList), 50)

    def test_export_sample_3(self):
        whatsappStats.main('export_sample_3.txt')
        self.assertEqual(len(whatsappStats.messageList), 50)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(WhatsappExportTypeTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
