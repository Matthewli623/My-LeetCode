class Solution
{
public:
    int peakIndexInMountainArray(vector<int> &A)
    {
        int max = 0;
        int id = 0;
        for (int i = 0; i < A.size(); i++)
        {
            if (A[i] > max)
            {
                max = A[i];
                id = i;
            }
        }
        return id;
    }
};