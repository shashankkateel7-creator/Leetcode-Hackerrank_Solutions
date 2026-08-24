int romanvalue(char c)
{   switch(c)
    {    case 'I': return 1;
        case 'V': return 5;
        case 'X': return 10;
        case 'L': return 50;
        case 'C': return 100;
        case 'D': return 500;
        case 'M': return 1000;
        default: return 0;}
}
int romanToInt(char* s) {
    int total=0;
    for(int i=0;s[i]!='\0';i++)
    {   int currentvalue=romanvalue(s[i]);
        int nextvalue=romanvalue(s[i+1]);

        if(currentvalue<nextvalue)
        {   total-=currentvalue;}
        else
        {   total+=currentvalue;}}
    return total;    

}