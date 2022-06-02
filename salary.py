open_tabs = int(input())
salary = int(input())


for tabs in range(open_tabs + 1):
    website_name = input()
    if website_name == "Facebook":
     salary - 150
    elif website_name == "Instagram":
      salary - 100
    elif website_name == "Reddit":
        salary - 50
    if salary <= 0:
           break
           print("You have lost your salary")
    else:
          print(salary)