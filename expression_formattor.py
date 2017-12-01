class ExpressionFormattor:
    def format(self,exp):
        exp = exp.replace("\n"," ")
        return self._convert_to_list(exp)
    def _convert_to_list(self,exp):
        if exp.find("(") == -1:
            return exp != "" and [exp] or []
        exp_list = []
        word = ""
        i = 1
        while i < len(exp)-1:
            if exp[i].isspace():
                if word != "":
                    exp_list.append(word)
                    word = ""
                i += 1
            elif exp[i] == "'":
                i += 1
            elif exp[i] == "(":
                right_par_index = self._find_right_parenthesis(exp,i)
                exp_list.append(self._convert_to_list(exp[i:right_par_index+1]))
                i = right_par_index + 1
            else:
                word += exp[i]
                i += 1
        if word != "":
            exp_list.append(word)
        return exp_list
    def _find_right_parenthesis(self,exp,left_index):
        count = 0
        for i in range(left_index,len(exp) - 1):
            if exp[i] == "(":
                count += 1
            elif exp[i] == ")":
                count -= 1
                if count == 0:
                    return i
        return -1
    
