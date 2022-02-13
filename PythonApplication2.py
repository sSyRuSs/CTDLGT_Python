class Nut:#lop Node
    def __init__(self, khoa=None):
        self.khoa = khoa
        self.left = None
        self.right = None

    def add(self, khoa):
        if self is None:
            nut = Nut(khoa)
            self = nut
            return

        if khoa < self.khoa:
            if self.left == None:
                self.left = Nut(khoa)
            else :
                self.left.add(khoa)
        elif khoa > self.khoa:
            if self.right == None:
                self.right = Nut(khoa)
            else:
                self.right.add(khoa)
        else:
            print(f'Loi trung lap {khoa}')

class BST:#lop BST
    def __init__(self, khoa = None):
        if khoa == None:
            self.root = None
        else:
            self.root = Nut(khoa)

    def add(self, khoa):
        if self.root == None:
           self.root = Nut(khoa)
        else:
            self.root.add(khoa)
            #chen khoa vao node dau
    def delete(self, khoa):
        nut_cha = None
        cha_con = None
        Node_p = self.root

        while Node_p != None:
            if Node_p.khoa > khoa:
                nut_cha = Node_p
                Node_p = Node_p.left
                cha_con = 'left'
            elif Node_p.khoa < khoa:
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
                            #truy lung den tan cung ben trai
                        temp.left = Node_p.left
                # Xoa nut la
                elif Node_p.left == None and Node_p.right ==None:
                    #ko phai nut goc
                    if cha_con == 'left':
                        nut_cha.left = None
                    else:
                        nut_cha.right = None
                elif Node_p.left == None:#xoa nut la co con ben phai
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
                        #truy lung den tan cung ben trai
                        while temp.left != None:
                            temp = temp.left
                        temp.left = Node_p.left
                del Node_p
                break

    def LNR(self, root = 0):
        Node_p = root
        if root == 0:
            Node_p = self.root
        if Node_p == None:
            return []
        else:
            result = []

            result_left = self.LNR(Node_p.left)
            for i in result_left:
                result.append(i)

            result.append(Node_p.khoa)

            result_right = self.LNR(Node_p.right)
            for i in result_right:
                result.append(i)
            return result
        return LNR

    def LRN(self, root = 0):
        Node_p = root
        if root == 0:
            Node_p = self.root
        if Node_p == None:
            return []
        else:
            result = []

            result_left = self.LRN(Node_p.left)
            for i in result_left:
                result.append(i)

            result_right = self.LRN(Node_p.right)
            for i in result_right:
                result.append(i)

            result.append(Node_p.khoa)
            return result
        return LRN

    def NLR(self, root = 0):
        Node_p=root
        if root == 0:
            Node_p = self.root
        if Node_p ==None:
            return []
        else:
            result = []
            result.append(Node_p.khoa)

            result_left = self.NLR(Node_p.left)
            for i in result_left:
                result.append(i)

            result_right = self.NLR(Node_p.right)
            for i in result_right:
                result.append(i)
            return result
        return NLR

    def NRL(self, root = 0):
        Node_p=root
        if root == 0:
            Node_p = self.root
        if Node_p ==None:
            return []
        else:
            result = []
            result.append(Node_p.khoa)
            result_right = self.NRL(Node_p.right)
            for i in result_right:
                result.append(i)

            result_left = self.NRL(Node_p.left)
            for i in result_left:
                result.append(i)

            return result
        return NRL

    def RNL(self, root = 0):
        Node_p=root
        if root == 0:
            Node_p = self.root
        if Node_p ==None:
            return []
        else:
            result = []
            result_right = self.RNL(Node_p.right)
            for i in result_right:
                result.append(i)
            result.append(Node_p.khoa)

            result_left = self.RNL(Node_p.left)
            for i in result_left:
                result.append(i)

            return result
        return RNL
    def RLN(self, root = 0):
        Node_p=root
        if root == 0:
            Node_p = self.root
        if Node_p ==None:
            return []
        else:
            result = []
            result_right = self.RLN(Node_p.right)
            for i in result_right:
                result.append(i)

            result_left = self.RLN(Node_p.left)
            for i in result_left:
                result.append(i)

            result.append(Node_p.khoa)
            return result
        return RLN

    #tim
    def search(self, khoa):
        if self.root == None:
            return
        Node_p = self.root
        result = ''
        while(Node_p != None and Node_p.khoa != khoa):
            result = result + f'{Node_p.khoa} -> '
            if khoa <= Node_p.khoa:
                Node_p = Node_p.left
            else:
                Node_p = Node_p.right

        if Node_p == None:
            return None
        else:
            result = result + f'{Node_p.khoa}'
            return result
        return search
        

def main():
        So_Phan_Tu = 10
        cay = BST()
        tap_gia_tri = set()
        from random import randint
        while len(tap_gia_tri)< So_Phan_Tu:
            gt = randint(1, 100)
            tap_gia_tri.add(gt)
        tap_gia_tri = list(tap_gia_tri)
        #tap_gia_tri = [1,9,7,6,12,56,78,22,45,63]
        tap_gia_tri = [66,46,84,11,81,99,36,77,83,87,100,86,85]
        print('Chen lan luot', tap_gia_tri)
        for i in tap_gia_tri:
            cay.add(i)
        
        result = cay.LNR()
        print("Duyet LNR: ", result)

        result = cay.LRN()
        print("Duyet LRN: ", result)

        result = cay.NLR()
        print("Duyet NLR: ", result)

        result = cay.NRL()
        print("Duyet NRL: ", result)

        result = cay.RLN()
        print("Duyet RLN: ", result)

        result = cay.RNL()
        print("Duyet RNL: ", result)

        gt = int(input("Nhap gia tri can xoa: "))
        print(f'Xoa {gt}')
        cay.delete(gt)

        #gt = int(input("Nhap khoa can them: "))
        #print(f'Chen them {gt}')
        #for i in tap_gia_tri:
         #   cay.add(i)
        #print('cay sau khi chen: ', tap_gia_tri)

        while True:
           nhap = input("Nhap khoa can tim: ")
           if nhap == '':
               break

           gt = int(nhap)
           result = cay.search(gt)
           if result == None:
               print(f'khong tim thay {gt}')
           else:
               print(f'Tim thay {gt}: {result}')
               break
if __name__ == "__main__":
    main()

