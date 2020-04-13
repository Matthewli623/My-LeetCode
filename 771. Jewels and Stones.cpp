class Solution
{
public:
    int numJewelsInStones(string J, string S)
    {
        std::set<char> j_set;
        for (size_t i = 0, szi(J.length()); i < szi; ++i)
        {
            j_set.insert(J[i]);
        }
        int counter = 0;
        for (size_t i = 0, szi(S.length()); i < szi; ++i)
        {
            if (j_set.count(S[i]))
                counter++;
        }
        return counter;
    }
};