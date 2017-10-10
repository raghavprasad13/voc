from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class BytearrayTests(TranspileTestCase):
    def test_setattr(self):
        self.assertCodeExecution("""
            x = bytearray([1,2,3])
            try:
                x.attr = 42
            except AttributeError as err:
                print(err)
            """)

    def test_getattr(self):
        self.assertCodeExecution("""
            x = bytearray([1,2,3])
            try:
                print(x.attr)
            except AttributeError as err:
                print(err)
            """)

    def test_capitalize(self):
        self.assertCodeExecution("""
            print(bytearray(b"abc").capitalize())
            print(bytearray().capitalize())
            """)

    def test_islower(self):
        self.assertCodeExecution("""
            print(bytearray(b'abc').islower())
            print(bytearray(b'').islower())
            print(bytearray(b'Abccc').islower())
            print(bytearray(b'HELLO WORD').islower())
            print(bytearray(b'@#$%!').islower())
            print(bytearray(b'hello world').islower())
            print(bytearray(b'hello world   ').islower())
            # TODO: uncomment when adding support for literal hex bytes
            #print(b'\xf0'.islower())
        """)
        # self.assertCodeExecution("""""")

    def test_isupper(self):
        self.assertCodeExecution("""
            print(bytearray(b'abc').isupper())
            print(bytearray(b'ABC').isupper())
            print(bytearray(b'').isupper())
            print(bytearray(b'Abccc').isupper())
            print(bytearray(b'HELLO WORD').isupper())
            print(bytearray(b'@#$%!').isupper())
            print(bytearray(b'hello world').isupper())
            print(bytearray(b'hello world   ').isupper())
            # TODO: uncomment when adding support for literal hex bytes
            #print(b'\xf0'.isupper())
        """)
        # self.assertCodeExecution("""""")

    def test_lower(self):
        self.assertCodeExecution("""
            print(bytearray(b"abc").lower())
            print(bytearray(b"HELLO WORLD!").lower())
            print(bytearray(b"hElLO wOrLd").lower())
            print(bytearray(b"[Hello] World").lower())
            """)


class UnaryBytearrayOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'bytearray'

    not_implemented = [
    ]


class BinaryBytearrayOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'bytearray'

    not_implemented = [
    ]

    not_implemented_versions = {
        'test_modulo_complex': (3.4, ),
    }


class InplaceBytearrayOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'bytearray'

    not_implemented = [
    ]

    not_implemented_versions = {
        'test_modulo_complex': (3.4, ),
    }
