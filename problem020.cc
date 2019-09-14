// 2019-09-13
//
// Given two singly linked lists that intersect at some point, find the
// intersecting node. The lists are non-cyclical.
//
// For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return
// the node with value 8.
//
// In this example, assume nodes with the same value are the exact same node
// objects.
//
// Do this in O(M + N) time (where M and N are the lengths of the lists) and
// constant space.

#include <iostream>
#include <memory>

using namespace std;

struct node_t
{
    node_t(const int _value) : value(_value) {}

    int value {};
    shared_ptr<node_t> next {nullptr};
};

size_t get_length(shared_ptr<node_t> list)
{
    size_t len = 0;
    while (list)
    {
        list = list->next;
        len++;
    }

    return len;
}

shared_ptr<node_t> find_intersecting_node(shared_ptr<node_t> long_list,
                                          shared_ptr<node_t> short_list,
                                          const size_t len_diff)
{
    for (size_t i = 0; i < len_diff; i++)
    {
        long_list = long_list->next;
    }

    while (long_list != short_list)
    {
        long_list = long_list->next;
        short_list = short_list->next;
    }

    return long_list;
}

shared_ptr<node_t> find_intersecting_node(shared_ptr<node_t> list1,
                                          shared_ptr<node_t> list2)
{
    const size_t len_list1 = get_length(list1);
    const size_t len_list2 = get_length(list2);

    if (len_list2 > len_list1)
    {
        return find_intersecting_node(list2, list1, len_list2 - len_list1);
    }
    else
    {
        return find_intersecting_node(list1, list2, len_list1 - len_list2);
    }
}

int main()
{
    shared_ptr<node_t> list1_head(new node_t(0));
    shared_ptr<node_t> list2_head(new node_t(100));

    {
        shared_ptr<node_t> list1 = list1_head;
        for (size_t i = 1; i < 10; i++)
        {
            list1->next = shared_ptr<node_t>(new node_t(i));
            list1 = list1->next;
        }

        shared_ptr<node_t> list2 = list2_head;
        for (size_t i = 101; i < 120; i++)
        {
            list2->next = shared_ptr<node_t>(new node_t(i));
            list2 = list2->next;
        }

        list1->next = list2;

        for (size_t i = 120; i < 130; i++)
        {
            list2->next = shared_ptr<node_t>(new node_t(i));
            list2 = list2->next;
        }
    }

    cout << find_intersecting_node(list1_head, list2_head)->value << endl;
    cout << find_intersecting_node(list2_head, list1_head)->value << endl;
    cout << find_intersecting_node(list1_head, list1_head)->value << endl;
    cout << find_intersecting_node(list2_head, list2_head)->value << endl;

    return 0;
}
