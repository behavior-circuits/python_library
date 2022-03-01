from tabnanny import check
import behavior_circuits as bc
import unittest


def check_truthtable(gate, truthtable):
    follows_truthable = True
    for row in truthtable:
        follows_truthable = follows_truthable and gate(
            float(row[0]), float(row[1])) == row[2]
    return follows_truthable


class TestGates(unittest.TestCase):
    def test_or_gate(self):
        truthtable = [[0, 0, 0],
                      [0, 1, 1],
                      [1, 0, 1],
                      [1, 1, 1],
                      [0, -1, -1],
                      [-1, 0, -1],
                      [-1, -1, -1],
                      [-1, 1, 0],
                      [1, -1, 0]]

        assert check_truthtable(bc.or_gate, truthtable)

    def test_and_gate(self):
        truthtable = [[0, 0, 0],
                      [0, 1, 0],
                      [1, 0, 0],
                      [1, 1, 1],
                      [0, -1, 0],
                      [-1, 0, 0],
                      [-1, -1, -1],
                      [-1, 1, 0],
                      [1, -1, 0]]

        assert check_truthtable(bc.and_gate, truthtable)

    def test_amp_gate(self):
        truthtable = [[0, 0, 0],
                      [0, 1, 0],
                      [1, 0, 0],
                      [1, 1, 1],
                      [0, -1, 0],
                      [-1, 0, 0],
                      [-1, -1, 1],
                      [-1, 1, -1],
                      [1, -1, -1]]

        assert check_truthtable(bc.amp_gate, truthtable)

    def test_prevail_gate(self):
        truthtable = [[0, 0, 0],
                      [0, 1, 1],
                      [1, 0, 1],
                      [1, 1, 1],
                      [0, -1, -1],
                      [-1, 0, -1],
                      [-1, -1, -1],
                      [-1, 1, -1],
                      [1, -1, 1]]

        assert check_truthtable(bc.prevail_gate, truthtable)

    def test_invoke_gate(self):
        truthtable = [[0, 0, 0],
                      [0, 1, 0],
                      [1, 0, 1],
                      [1, 1, 1],
                      [0, -1, 0],
                      [-1, 0, -1],
                      [-1, -1, -1],
                      [-1, 1, 0],
                      [1, -1, 0]]

        assert check_truthtable(bc.invoke_gate, truthtable)

    def test_compare_gate(self):
        truthtable = [[0, 0, 0],
                      [0, 1, -1],
                      [1, 0, 1],
                      [1, 1, 0],
                      [0, -1, 1],
                      [-1, 0, -1],
                      [-1, -1, 0],
                      [-1, 1, -1],
                      [1, -1, 1]]

        assert check_truthtable(bc.compare_gate, truthtable)

    def test_xor_gate(self):
        truthtable = [[0, 0, 0],
                      [0, 1, 1],
                      [1, 0, 1],
                      [1, 1, 0],
                      [0, -1, -1],
                      [-1, 0, -1],
                      [-1, -1, 0],
                      [-1, 1, 0],
                      [1, -1, 0]]

        assert check_truthtable(bc.xor_gate, truthtable)


if __name__ == '__main__':
    unittest.main()
