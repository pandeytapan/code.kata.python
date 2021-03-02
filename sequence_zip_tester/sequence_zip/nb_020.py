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
