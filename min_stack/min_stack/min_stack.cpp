// min_stack.cpp : This file contains the 'main' function. Program execution begins and ends there.
// https://leetcode.com/problems/min-stack/

#include <iostream>
#include <stack>
#include <stdexcept>
#include <string>

class MinStack {
    /*
    Algorithm: Keep track of 2 stacks. When adding an element to the main stack, 
    check if that element is less than or equal the current top of the minimum stack. If it
    is, add it to the min stack.
    When popping from the main stack, see if what we're popping is the top of the min stack.
    If so, pop that stack as well
    */
private:
    std::stack<int> regular_stack;
    std::stack<int> minimum_stack;

public:
    
    MinStack() {
    }

    void push(int val) {
        regular_stack.push(val);
        
        if (minimum_stack.empty()) {
            minimum_stack.push(val);
        }
        else if(val <= minimum_stack.top()) {
            // Check LEQ b/c when popping we check if the value equals
            // possible chain of numbers (5, 5, 4)
            minimum_stack.push(val);
        }
    }

    void pop() {
        if (minimum_stack.empty() || regular_stack.empty()) {
            throw(std::logic_error("Attempted to pop an empty stack"));
            return; //unreachable
        }

        int regular_top = regular_stack.top();
        regular_stack.pop();

        if (minimum_stack.top() == regular_top) {
            minimum_stack.pop();
        }
    }

    int top() {
        return regular_stack.top();
    }

    int getMin() {
        return minimum_stack.top();
    }

    bool empty() {
        return regular_stack.empty();
    }

    bool min_empty() {
        //shouldn't be required since the first element pushed is always the last minimum
        return minimum_stack.empty();
    }
};

int main() {

    MinStack* minStackPtr = new MinStack();
    minStackPtr->push(10);
    minStackPtr->push(11);
    minStackPtr->push(-2);
    minStackPtr->push(-3);
    minStackPtr->push(5);
    minStackPtr->push(10);
    minStackPtr->push(-20);

    while (!minStackPtr->empty()) {
        std::cout << "MinStack Top=" << minStackPtr->top() << ", min=" << std::string(minStackPtr->min_empty() ? "{empty}" : std::to_string(minStackPtr->getMin())) << std::endl;
        minStackPtr->pop();
    }


}
