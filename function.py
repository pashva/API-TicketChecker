from flask_restful import Resource, reqparse
import re
import datetime


def removeSpaces(q):
    z = q.replace(' ', '')
    return z


def gettinglocation(string):
    allplace = ['dadar', 'Matunga', 'Mahim', 'bandra', 'Khar', 'Santacruz', 'Vileparle', 'ANDHERI', 'Jogeshwari',
                'Goregaon', 'Malad', 'Kandivali', 'borivali']
    List = []
    y = string
    for s in y:
        if (s == " "):
            a = removeSpaces(y)

            List.append(a)

            y = ''
        y += s
    for i in range(len(List)):
        if List[i] == 'TO' or List[i] == 'To':
            entry_index = 0
            exit_index = 0
            for j in range(len(allplace)):
                if allplace[j].upper() == List[i - 1]:
                    entry_index = j

                if allplace[j].upper() == List[i + 1]:
                    exit_index = j
                    exit_index = exit_index + 1
            entryallowedplace = allplace[entry_index]

            exitallowedplaces = allplace[entry_index:exit_index]
    return entryallowedplace, exitallowedplaces


class Fun(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('stringt',
                        type=str,
                        required=True,
                        help="This field cannot be left blank.")
    parser.add_argument('checker',
                        type=str,
                        required=True,
                        help="This field cannot be left blank.")
    parser.add_argument('entry_point',
                        type=str,
                        required=False,
                        help="This field cannot be left blank.")

    def post(self):
        data = Fun.parser.parse_args()
        match = re.search('\d{2}/\d{2}/\d{4}', data["stringt"])
        if match == None:
            return "No Date Found on ticket", 200

        date = datetime.datetime.strptime(match.group(), '%d/%m/%Y').date()
        final = str(date)
        year = ''
        month = ''
        date = ''
        check = 0
        for i in final:
            if check == 0:
                year = year + i
            if i == '-':
                check = check + 1
            if check == 1:
                month = month + i
            if check == 2:
                date = date + i
        date = date[1:]
        month = month[1:]
        year = year[:-1]

        pashva = date + '/' + month + '/' + year

        if pashva == data["checker"]:
            entry, exit = gettinglocation(string=data["stringt"])

            if entry.upper() == data['entry_point'].upper():
                return "Perfect entry point and date", 200
            return "Wrong entry point", 200
        return "Invalid Date", 200
