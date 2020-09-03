from collections.abc import Sequence


class SequenceZip(Sequence):

    """Like zip, but just for sequences and fancier."""

    def __init__(self, *sequences):
        self.sequences = sequences

    def __len__(self):
        return min(
            len(seq)
            for seq in self.sequences
        )

    def __getitem__(self, index):
        if index < 0:
            index += len(self)
        return tuple(
            seq[index]
            for seq in self.sequences
        )

    def __eq__(self, other):
        if not isinstance(other, SequenceZip):
            return NotImplemented
        
        a = tuple(s[:len(self)] for s in self.sequences)
        b = tuple(s[:len(self)] for s in other.sequences)
        return a == b


Sequence.register(SequenceZip)
# seq1 = SequenceZip([1], [4, 6, 6], [7, 8, 9])
# seq2 = SequenceZip([1, 2, 3], [4, 5, 7], [7, 8, 9, 0])

seq1 = SequenceZip(['a', 'b'], 'de')
seq2 = SequenceZip('ab', ['d', 'e'])
x = seq1 == seq2
print(x)