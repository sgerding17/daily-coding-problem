// 2019-08-30
//
// An XOR linked list is a more memory efficient doubly linked list. Instead of
// each node holding next and prev fields, it holds a field named both, which
// is an XOR of the next node and the previous node. Implement an XOR linked
// list; it has an add(element) which adds the element to the end, and a
// get(index) which returns the node at index.

#include <assert.h>
#include <iostream>
#include <memory>

using namespace std;

struct node_t
{
    int element {0};
    node_t *both {nullptr};
};

node_t *x(node_t *a, node_t *b)
{
    return reinterpret_cast<node_t*>(
               reinterpret_cast<uint64_t>(a) ^
               reinterpret_cast<uint64_t>(b));
}

class node_itr
{
public:
    node_itr() {}

    static node_itr create_from_prev(node_t *self, node_t *prev)
    {
        return node_itr(self,
                        prev,
                        self ? x(self->both, prev) : nullptr);
    }
    static node_itr create_from_next(node_t *self, node_t *next)
    {
        return node_itr(self,
                        self ? x(self->both, next) : nullptr,
                        next);
    }

    operator bool()
    {
        return self != nullptr;
    }

    bool operator==(const node_itr &other)
    {
        return self == other.self;
    }

    int get_element()
    {
        return self->element;
    }

    node_itr get_next()
    {
        return node_itr::create_from_prev(next, self);
    }

    node_itr get_prev()
    {
        return node_itr::create_from_next(prev, self);
    }

    node_itr append(const int element)
    {
        node_t *new_node = new node_t;
        new_node->element = element;

        next = new_node;
        self->both = x(prev, next);
        new_node->both = self;

        return node_itr::create_from_prev(new_node, self);
    }

private:
    node_itr(node_t *_self,
             node_t *_prev,
             node_t *_next) :
        self(_self),
        prev(_prev),
        next(_next)
    {}

    node_t *self {nullptr};
    node_t *prev {nullptr};
    node_t *next {nullptr};
};

class list
{
public:
    void add(const int element)
    {
        if (!tail)
        {
            node_t *new_node = new node_t;
            new_node->element = element;
            head = tail = node_itr::create_from_next(new_node, nullptr);
        }
        else if (head == tail)
        {
            tail = head.append(element);
        }
        else
        {
            tail = tail.append(element);
        }
    }

    node_itr get(const size_t index)
    {
        node_itr retval = head;
        for (size_t i = 0; i < index; i++)
        {
            if (!retval) break;
            retval = retval.get_next();
        }
        return retval;
    }

private:
    node_itr head;
    node_itr tail;
};

int main()
{
    list l;
    assert(!l.get(0));
    for (size_t i = 0; i < 10; i++)
    {
        l.add(i + 100);

        for (size_t j = 0; j <= i; j++)
        {
            assert((bool)l.get(j));
            assert(l.get(j).get_element() == j + 100);
        }
        for (size_t j = i + 1; j < 10; j++)
        {
            assert(!l.get(j));
        }
    }

    assert(l.get(7).get_prev().get_prev().get_element() == 105);

    return 0;
}
