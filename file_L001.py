for i in range(1,11):
    file = open('{}.txt'.format(i), 'w')
    file.write('hello ,ricky{}'.format(i))
    file.close()