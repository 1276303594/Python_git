for i in range(100, 1000):
    first_number, second_number, third_number = map(int, str(i))
    if i == (
            first_number**3
            + second_number**3
            + third_number**3):
        print(i)


data = [['张*', '赵*', '康*', '卫*', '梁*']
          ['苏*', '李*', '程*', '董*2', '耿*2']
         ['郝*', '耿*1', '杨*', '熊*', '赵*2']
         ['董*', '李*', '程*2', '何*', '杨*2']]