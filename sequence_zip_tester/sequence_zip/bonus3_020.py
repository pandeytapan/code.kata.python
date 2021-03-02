class SequenceZip:
    def __init__(self, *sequences):
        self.sequences = sequences
    def __len__(self):
        return min(len(s) for s in self.sequences)
    def __getitem__(self, index):
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self))
            if step < 0:
                stop = -(len(self) + 1 - stop)
            return SequenceZip(*(
                seq[start:stop:step]
                for seq in self.sequences
            ))
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
    def __repr__(self):
        sequences = ", ".join(repr(s) for s in self.sequences)
        return f"{type(self).__name__}({sequences})"
