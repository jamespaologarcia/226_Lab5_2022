from django.shortcuts import render
from django.http import HttpResponse
BOARD_SIZE = 4
board =  [[['_' for _ in range(BOARD_SIZE)]  for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
def showBoard(result):
    global board
    result = ''
    for row in board :
        result += '<table border=1>'
        for ro in row:
            result += '<tr>'
            for r in ro:
                result += '<td>'+str(r)+'</td>'           
            result +='<tr>'
        result += '</table>'
    return result
def index(request):
    return HttpResponse(showBoard(''))