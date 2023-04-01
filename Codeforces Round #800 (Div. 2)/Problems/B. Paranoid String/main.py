"""
Accomplished using the EduTools plugin by JetBrains https://plugins.jetbrains.com/plugin/10081-edutools

To modify the template, go to Preferences -> Editor -> File and Code Templates -> Other
"""

if __name__ == "__main__":
    # Write your solution here
    for _ in range(int(input())):
        n = int(input())
        s = input()
        ans = 0
        if n > 1:
            for i in range(n - 1):
                if s[i] == s[i + 1]:
                    ans += i + 1
            total = int((n * (n + 1)) / 2)
            print(total - ans)
        else:
            print(1)
