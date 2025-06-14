class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> result;
        if (s.empty() || words.empty()) return result;

        int wordLen = words[0].size();        // length of each word
        int wordCount = words.size();         // number of words
        int totalLen = wordLen * wordCount;   // total length to check each time

        if (s.length() < totalLen) return result;

        // 1. Store frequency of each word in words[]
        unordered_map<string, int> wordMap;
        for (string w : words) wordMap[w]++;

        // 2. Try every offset (0 to wordLen - 1) — helps align word boundaries
        for (int i = 0; i < wordLen; i++) {
            int left = i;                             // window start
            int count = 0;                            // number of words matched
            unordered_map<string, int> windowMap;     // frequency of words in window

            // 3. Slide through string in steps of wordLen
            for (int j = i; j + wordLen <= s.length(); j += wordLen) {
                string word = s.substr(j, wordLen);   // get one word

                // If it's a valid word
                if (wordMap.find(word) != wordMap.end()) {
                    windowMap[word]++;
                    count++;

                    // If it appears too many times, move left forward
                    while (windowMap[word] > wordMap[word]) {
                        string leftWord = s.substr(left, wordLen);
                        windowMap[leftWord]--;
                        count--;
                        left += wordLen;
                    }

                    // If all words matched
                    if (count == wordCount) {
                        result.push_back(left);
                    }
                }
                // Invalid word: reset window
                else {
                    windowMap.clear();
                    count = 0;
                    left = j + wordLen;
                }
            }
        }

        return result;
    }
};
