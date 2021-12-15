def template(lang):
    if lang == "py":
        return """def main():
    print("Hello, user or some guy")

if __name__ == "__main__":
    main()
 """
    elif lang == "csharp":
        return """using System;

namespace MainFile {
    public static class Program{
        public staic void Main(string[] args){
            Console.Write("Why do java devs wear glasses?, Cause they can't C#");
        }
    }
}
"""
    elif lang == "cpp":
        return """#include <iostream>
int main(){
    return 0;
}
"""
    elif lang == "java":
        return """public class Main{
    public static void main(string[] args){
        System.out.println("Coffee");
    }
}
"""
    elif lang == "c":
        return """#include <stdio.h>
int main(){
    return 0;
}
"""
    elif lang == "html":
        return """<!DOCTYPE html>
<html>
    <head>
        <title> Document </title>
        <style></style>
    </head>
    <body>
        <h1>A Spider is the only web developer that likes bugs.</h1>
        <script></script>
    </body>
</html>
"""
    elif lang == "golang":
        return """package main

import "fmt"

func main(){
    
}
"""