import numpy as np


def normalize_landmarks_dual(hand1, hand2=None):
    """Normalize up to two 21-point hands into a 126-feature vector."""

    def process(hand):
        hand = np.array(hand, dtype=np.float32)
        origin = hand[0]
        hand = hand - origin
        max_val = np.max(np.abs(hand))
        if max_val < 1e-6:
            return None
        return (hand / max_val).flatten()

    f1 = process(hand1)
    if f1 is None:
        return None

    if hand2 is not None:
        f2 = process(hand2)
        if f2 is None:
            return None
    else:
        f2 = np.zeros(63, dtype=np.float32)

    return np.concatenate([f1, f2])
