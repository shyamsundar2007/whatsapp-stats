# import files
import re
from datetime import date, time, timedelta, datetime
from pprint import pprint
import operator
import sys

# global vars
file_name = ''
regex_string = '^(\d{1,2})[.,/](\d{1,2})[.,/](\d{1,4}).*?(\d{1,2}):(\d{1,2})(?:\:(\d{1,2}))?.*?[:-]\s(.*?):(.*)$'
messageList = []
userDict = {}


# class definitions
class Message:
    def __init__(self, msg_date, msg_time, msg_message):
        self.msg_date = msg_date
        self.msg_time = msg_time
        self.msg_message = msg_message

    def add_user_obj(self, usr_obj):
        self.msg_user = usr_obj


class User:
    def __init__(self, name):
        self.name = name
        self.messageList = []

    def add_msg_obj(self, msg_obj):
        self.messageList.append(msg_obj)

# function definitions


def conversation_stats():
    count = 0
    for user in userDict:
        count = count + len(userDict[user].messageList)
        print ('%s initiations: %d' % (user, len(userDict[user].messageList)))
    print ('Total conversations: %d' % count)


def date_stats():
    date_range_dict = {}
    start_date = date(3000, 1, 1)
    end_date = date(1, 1, 1)

    for msg_obj in messageList:
        if start_date > msg_obj.msg_date:
            start_date = msg_obj.msg_date
        if end_date < msg_obj.msg_date:
            end_date = msg_obj.msg_date

    d = date(start_date.year, start_date.month, 1)
    while d <= end_date:
        date_range_dict[d] = 0
        d = date(d.year + (d.month / 12), ((d.month % 12) + 1), 1)

    for msg_obj in messageList:
        date_range_dict[date(msg_obj.msg_date.year,
                             msg_obj.msg_date.month, 1)] += 1

    it = iter(sorted(date_range_dict.iteritems()))
    for month_obj in it:
        print ('Month: %2s/%4s chats: %d' %
               (month_obj[0].month, month_obj[0].year, month_obj[1]))


def day_stats():
    day_dict = {}

    for msg_obj in messageList:
        if msg_obj.msg_date in day_dict:
            day_dict[msg_obj.msg_date] = day_dict[msg_obj.msg_date] + 1
        else:
            day_dict[msg_obj.msg_date] = 1

    it = iter(sorted(day_dict.iteritems()))
    for day_obj in it:
        print ('Date: %s chats: %d' % (day_obj[0], day_obj[1]))


def message_stats():

    for user in userDict:
        avg_count = 0
        wordsDict = {}
        for message in userDict[user].messageList:
            avg_count += message.msg_message.count(' ') + 1
            wordsList = re.compile('\w+').findall(message.msg_message)
            for word in wordsList:
                if word in wordsDict:
                    wordsDict[word] += 1
                else:
                    wordsDict[word] = 1
        avg_count = avg_count / len(userDict[user].messageList)
        print ('Average number of words by %s: %d' % (user, avg_count))
        sorted_x = sorted(wordsDict.items(),
                          key=operator.itemgetter(1), reverse=True)
        print ('Words commonly used: %s' % sorted_x[:20])
        print (' ')


def testFunc():
    return True


def main(file_name):
    global messageList
    global userDict
    messageList = []
    userDict = {}
    with open(file_name) as file_text:
        for line in file_text:
            # print line
            match = re.search(regex_string, line)
            if match:
                # print match.group(0)

                # create message class instance
                # check if android (date is stored as 20xx)
                if int(match.group(3)) > 2000:
                    msg_obj = Message(date(int(match.group(3)), int(match.group(2)), int(match.group(
                        1))), time(int(match.group(4)), int(match.group(5)), 0, 0), match.group(8))
                else:
                    msg_obj = Message(date(int(match.group(3)) + 2000, int(match.group(2)), int(
                        match.group(1))), time(int(match.group(4)), int(match.group(5)), 0, 0), match.group(8))
                messageList.append(msg_obj)

                # create user instance if necessary
                if match.group(7) not in userDict:
                    # print 'User %s not in dict' % match.group(7)
                    userDict[match.group(7)] = User(match.group(7))

                # point user class to current message instance
                userDict[match.group(7)].add_msg_obj(msg_obj)
                # point message instance to user instance
                msg_obj.add_user_obj(userDict[match.group(7)])

            #else:
                #print line
                #print 'No match'

def printStats():
    print (' ')
    conversation_stats()
    print (' ')
    date_stats()
    print (' ')
    day_stats()
    print (' ')
    message_stats()
