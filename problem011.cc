// 2019-09-04
//
// Implement an autocomplete system. That is, given a query string s and a set
// of all possible query strings, return all strings in the set that have s as
// a prefix.
// 
// For example, given the query string de and the set of strings [dog, deer,
// deal], return [deer, deal].
// 
// Hint: Try preprocessing the dictionary into a more efficient data structure
// to speed up queries.

#include <iostream>
#include <memory>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

class Index
{
public:
    void add_words(const vector<string> &words)
    {
        for (const auto &word : words)
        {
            shared_ptr<node_t> node = root;
            for (const auto letter : word)
            {
                if (!node->next.count(letter))
                {
                    node->next[letter] = shared_ptr<node_t>(new node_t);
                }
                node = node->next[letter];
            }

            node->words.push_back(word);
        }
    }

    void lookup_prefix(const string &prefix, vector<string> &matches) const
    {
        matches.clear();

        shared_ptr<node_t> node = root;
        for (const auto letter : prefix)
        {
            if (!node->next.count(letter))
            {
                return;
            }
            node = node->next[letter];
        }

        get_words(node, matches);
    }

private:
    struct node_t
    {
        vector<string> words;
        unordered_map<char, shared_ptr<node_t>> next;
    };

    void get_words(const shared_ptr<node_t> node, vector<string> &matches) const
    {
        for (const auto &word : node->words)
        {
            matches.push_back(word);
        }

        for (const auto &letter_node_pair : node->next)
        {
            const auto &next = letter_node_pair.second;
            get_words(next, matches);
        }
    }

    shared_ptr<node_t> root {new node_t};
};

int main()
{
    Index index;
    index.add_words({"deer", "deal", "dog", "cat", ""});

    for (const auto &prefix : vector<string>({"d", "de", "dea", "do", "x", ""}))
    {
        vector<string> matches;
        index.lookup_prefix(prefix, matches);

        cout << prefix << ":" << endl;
        for (const auto &m : matches) cout << "  " << m << endl;
    }

    return 0;
}
