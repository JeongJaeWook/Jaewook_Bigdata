first_name = "bumky"
last_name = "wook"

a = 2
b =3

#print(first_name + a) '숫자 + 문자형이기 때문에 에러가 뜸'


a_list = ['사과','감','배']
b_list = ['영희','철','재욱']

print(b_list)
print(b_list[0])
a_list.append('수박')
a_list.append(3)
print(a_list)

#dictionary
a_dict = {'name':'bob', 'age':24}
a_dict['height'] = 183 #추가'#'
print(a_dict)

a_dict['fruit'] = a_list
print(a_dict)

for fff in a_list:
    if fff=='사과' :
        print(fff)