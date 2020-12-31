class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        mod_log = [item.split(" ") for item in logs]
        letter_log = []
        digit_log = []
        output = []

        for log in mod_log:
            if log[1].isdigit():
                digit_log.append(log)
            else:
                letter_log.append(log)

        #insertion Sort for Letter_log
        for i in range(len(letter_log)):
            mini = letter_log[i]
            for j in range(i,len(letter_log)):
                temp = letter_log[j][1:]
                if temp < mini[1:]:
                    letter_log[i] , letter_log[j]  = letter_log[j] , letter_log[i]
                    mini = letter_log[i]
                elif temp==mini[1:]:
                    if letter_log[j] < letter_log[i]:
                        letter_log[i] ,letter_log[j]  =letter_log[j] , letter_log[i]
                        mini = letter_log[i]


        for i in range(len(letter_log)):
            s = " ".join(letter_log[i])
            output.append(s)
        for i in range(len(digit_log)):
            s = " ".join(digit_log[i])
            output.append(s)

        return output
