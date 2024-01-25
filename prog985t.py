class MergeSort:
    @staticmethod
    def sort(A:list):
        if len(A) > 1:
            middle = int(len(A) / 2)
            L = A[0:middle-1]
            R = A[middle:len(A)]
            L = MergeSort.sort(L)
            R = MergeSort.sort(R)
            A =MergeSort.Merge(A, L, R)
        return A

    @staticmethod
    def Merge(A, L, R):
        i = 0
        j = 0
        k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i = i + 1
            else:
                A[k] = R[j]
                j = j + 1
            k = k + 1
        while i < len(L):
            A[k] = L[i]
            i = i + 1
            k = k + 1
        while j < len(R):
            A[k] = R[j]
            j = j + 1
            k = k + 1
        return A