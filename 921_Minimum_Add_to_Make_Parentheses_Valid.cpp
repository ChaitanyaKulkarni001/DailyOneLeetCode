int count = 0;
    stack<string> stackObj;
    for (char c : s)
    {
        if (c == '(')
        {
            stackObj.push("(");
        }
        else
        {

            if (stackObj.empty())
            {
                count++;
            }
            else
            {
                stackObj.pop();
            }
        }

    }
    return count + stackObj.size();
