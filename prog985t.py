class Merge:
    @staticmethod
    def MergeSort(A):
        if len(A) > 1:
            middle = len(A) / 2
            L = A[0::middle-1]
            R = A[middle::len(A)]
            Merge.MergeSort(L)
            Merge.MergeSort(R)
            Merge(A, L, R)
