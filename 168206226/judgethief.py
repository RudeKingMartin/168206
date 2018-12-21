flag=0
for i in range(ord('A'),ord('D')+1):#从A到D一个一个假设是小偷
	print("假设",chr(i),
	"偷了钻石，那么：")
	if i!=ord('A'):
		print("A说了真话")
	else:
		print("A说了假话")
	if i==ord('D'):
		print("B说了真话")
	else:
		print("B说了假话")
	if i==ord('B'):
		print("C说了真话")
	else:
		print("C说了假话")
	if i!=ord('D'):
		print("D说了真话")
	else:
		print("D说了假话")
	turenumber=(i!=ord('A'))+(i==ord('D'))+(i==ord('B'))+(i!=ord('D'))#turenumber的值表示说真话人数
	print("这时共有",turenumber,"个人说了真话")
	if turenumber==1:#只有一个人说真话
		print("符合题意，假设成立，说明是",chr(i),"偷走了钻石\n\n")
		flag=1

if(flag==0):
	print("没有找到小偷")