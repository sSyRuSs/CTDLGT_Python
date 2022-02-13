
class MonHoc:
    def __init__(self  ,  mmh=None , tmh=None , lmh=None , stc=None , hdt=None):
        self.mmh = mmh
        self.tmh = tmh
        self.lmh = lmh
        self.stc = stc
        self.hdt = hdt
    def get_mmh(self):
        return self.mmh
    def XuatThongTinMonHoc(self):
        print(self.mmh," - ",self.tmh," - ",self.lmh," - ",self.stc," - ",self.hdt)
    def NhapThongTinMonHoc(self):
        self.mmh=input("Nhap ma mon hoc: ")
        self.tmh=input("Nhap ten mon hoc: ")
        self.lmh=input("Nhap loai mon hoc: ")
        self.stc=int(input("Nhap so tin chi cua mon hoc: "))
        self.hdt=input("Nhap he dao tao cua mon hoc: ")
#class  
class Node:
    def __init__(Self, MonHoc=None):
        Self.MonHoc=MonHoc
        Self.left = None
        Self.right = None
    #def    
    def Add(self ,Monhoc=None):
        if self is None:
            y=Node(MonHoc)
            self = y
            return
        x=Monhoc.tmh
        y=self.MonHoc.tmh
        if x<y:
            if self.left==None:
                self.left=Node(Monhoc)
            else:
                self.left.Add(Monhoc)
        elif x>y:
            if self.right==None:
                self.right=Node(Monhoc)
            else:
                self.right.Add(Monhoc)
        else:
            return None #trung lap
class NPTK:
    def __init__(self, NodeCha=None):
        if NodeCha == None:
            self.root = None
        else:
            self.root = NodeCha
    def add(self, Node):
        if  self.root == None:
            self.root = Node
        else:
            self.root.Add(Node.MonHoc)
    def delete(self, khoa):
        nut_cha = None
        cha_con = None
        Node_p = self.root

        while Node_p != None:
            if Node_p.MonHoc.tmh > khoa:
                nut_cha = Node_p
                Node_p = Node_p.left
                cha_con = 'left'
            elif Node_p.MonHoc.tmh < khoa:
                nut_cha = Node_p
                Node_p = Node_p.right
                cha_con = 'right'
            else: #tim thay
                if nut_cha == None:
                    #Xoa nut goc
                    if Node_p.left == None and Node_p.right == None:
                        #nut goc khong co 2 con
                        self.root = None
                    elif Node_p.left == None:
                        #xoa nut goc mot con ben phai
                        self.root = Node_p.right
                    elif Node_p.right == None:
                        self.root = Node_p.left
                    else:
                        self.root = Node_p.right
                        #goc co du 2 con
                        temp =self.root
                        while temp.left != None:
                            temp =temp.left
                        temp.left = Node_p.left
                # Xoa nut la
                elif Node_p.left == None and Node_p.right ==None:
                    if cha_con == 'left':
                        nut_cha.left = None
                    else:
                        nut_cha.right = None
                elif Node_p.left == None:
                    if cha_con == 'left':
                        nut_cha.left = Node_p.right
                    else:
                        nut_cha.right = Node_p.right
                elif Node_p.right == None:
                    if cha_con == 'left':
                        nut_cha.left = Node_p.left
                    else:
                        nut_cha.right = Node_p.right
                else:
                    if cha_con == 'left':
                        nut_cha.left = Node_p.right
                    else:
                        nut_cha.right = Node_p.right
                    if Node_p.right.left == None:
                        #nhanh trai cua ben phai bi rong
                        Node_p.right.left = Node_p.left
                    else:
                        temp = Node_p.right
                        while temp.left != None:
                            temp = temp.left
                        temp.left = Node_p.left
                del Node_p
                break
    def Sreach(self,TenMon):
        Node_p=self.root
        while Node_p!=None:
            if Node_p.MonHoc.tmh==TenMon:
                return True
            elif Node_p.MonHoc.tmh < TenMon:
                Node_p=Node_p.right
                continue
            else:
                Node_p=Node_p.left
    
def TinhTongSoTinChi(root):
    if root==None:
        return 0
    return TinhTongSoTinChi(root.left)+TinhTongSoTinChi(root.right)+root.MonHoc.stc

# def DemSoLuongMonHocTheoTungLoai(root):
def ThongKeMonHocTheoChi(root):
    if root!=None:
        ThongKeMonHocTheoChi(root.left)
        print(root.MonHoc.tmh,"  |   ",root.MonHoc.stc )
        
        ThongKeMonHocTheoChi(root.right)    
         



def LNR(root):
    if root!=None:
        LNR(root.left)
        root.MonHoc.XuatThongTinMonHoc()
        LNR(root.right)
def RNL(root):
    if root!=None:
        RNL(root.right)
        root.MonHoc.XuatThongTinMonHoc()
        RNL(root.left)
def NLR(root):
    if root!=None:
        root.MonHoc.XuatThongTinMonHoc()
        NLR(root.left)
        NLR(root.right)
def NRL(root):
    if root!=None:
        root.MonHoc.XuatThongTinMonHoc()
        NRL(root.right)
        NRL(root.left)
def LRN(root):
    if root!=None:
        LRN(root.left)
        LRN(root.right)
        root.MonHoc.XuatThongTinMonHoc()
def RLN(root):
    if root!=None:
        RLN(root.right)            
        RLN(root.left)
        root.MonHoc.XuatThongTinMonHoc()
# def DemSoLuongMonHocTheoTungLoai(self):

sv1=MonHoc("AC12","Anh Van","Bat buoc",3,"Chinh Quy")
sv2=MonHoc("LS2","Ly","Bat buoc",3,"Chinh Quy")
sv3=MonHoc("HH2","Hoa","Tu Chon",2,"Chinh Quy")
sv4=MonHoc("BSV1","Su","Tu Chon",1,"Cao Dang")
sv5=MonHoc("FAA","Dia","Bat buoc",1,"Cao Dang")
sv6=MonHoc("GGD","GDCD","Tu Chon",2,"Cao Dang")
sv7=MonHoc("DDF2","CNXH","Tu Chon",2,"Chinh Quy")
sv8=MonHoc("FSC1","Triet","Bat buoc",2,"Chinh Quy")
sv9=MonHoc("KA34","CTDL","Bat buoc",2,"Chinh Quy")
sv10=MonHoc("KK32","MMT","Tu Chon",2,"Chinh Quy")
x=Node(sv1)
y=Node(sv2)
z=Node(sv3)
j=Node(sv4)
q=Node(sv5)
a=Node(sv6)
b=Node(sv7)
c=Node(sv8)
d=Node(sv9)
e=Node(sv10)

BST=NPTK(x)
BST.add(y)
BST.add(z)
BST.add(q)
BST.add(j)
BST.add(a)
BST.add(b)
BST.add(c)
BST.add(d)
BST.add(e)


def Menu():
    
    print("1.Duyet Cay bang cach NLR-NRL-LNR ")
    print("2.Duyet Cay bang cach LRN-RLN-RNL ")
    print("3.Xoa mon hoc ra khoi cay ")
    print("4.Them mot mon hoc vao cay ")
    print("5.Tim mon hoc trong cay ")
    print("6.Thong ke mon hoc theo so tin chi")
    print("7.Dem so luong mon hoc theo tung loai")
    print("8.Tinh tong so tin chi  cac mon hoc")
    print("0. thoat ")
    while True:
        luachon=int(input("Nhap lua chon: "))
        if luachon==0:
            break
        elif luachon==1:

           print("-----------------Duyet cay theo NLR---------------------")
           NLR(BST.root)
           print("-----------------Duyet cay theo NRL-----------------")
           NRL(BST.root)
           print("-----------------Duyet cay theo LNR-----------------")
           LNR(BST.root)
        elif luachon==2:
           print("-----------------Duyet cay theo LRN-----------------")
           LRN(BST.root)
           print("-----------------Duyet cay theo RLN-----------------")
           RLN(BST.root)
           print("-----------------Duyet cay theo RNL-----------------")
           RNL(BST.root)
        elif luachon==3:
            khoa=input("Nhap ten mon hoc can xoa: ")
            BST.delete(khoa)
            print("Sau khi xoa cay con lai nhu sau duyet theo LNR")
            LNR(x)

        elif luachon==4:
            mh=MonHoc()
            print("Nhap thong tin mon hoc moi ")
            mh.NhapThongTinMonHoc()
            p=Node(mh)
            BST.add(p)
            print("Sau khi them mon hoc moi vao nhu sau   duyet theo LNR")
            LNR(BST.root)

        elif luachon==5:
            info=input("Nhap ten mon hoc can tim: ")
            h= BST.Sreach(info)
            if h==True:
                print("Trong cay co ton tai mon",info)
            else:
                print("Trong cay khong ton tai mon",info)

        elif luachon==6:
            print("Ten Mon |So Tin Chi")
            ThongKeMonHocTheoChi(BST.root)

        # elif luachon==7:

        elif luachon==8:
            print("Tong So tin chi trong cay la:",TinhTongSoTinChi(BST.root))    
Menu()