class SequenceZip:

    def __init__(self, *sequences):
        self.sequences = sequences

    def __repr__(self):
        sequences = ", ".join(repr(s) for s in self.sequences)
        return f"{type(self).__name__}({sequences})"

    def __len__(self):
        return min(len(s) for s in self.sequences)

    def __getitem__(self, index):
        if index < 0:
            index += len(self)
        return tuple(s[index] for s in self.sequences)

    def __eq__(self, other):
        if not isinstance(other, SequenceZip):
            return NotImplemented
        return all(
            a == b
            for a, b in zip(self, other)
        )
